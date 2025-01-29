#!/usr/bin/env python3

import argparse
import pandas as pd
import os
from datasets import Dataset
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

# Configuring the experiment
MODEL_ID = "tiiuae/falcon-7b"
OUTPUT_CSV = "falcon_results.csv"
BATCH_SIZE = 16  
MAX_NEW_TOKENS = 16

def preprocess_questions(csv_path: str) -> Dataset:
    """
    Load questions and preprocess them into a Hugging Face Dataset.
    """
    df = pd.read_csv(csv_path)
    return Dataset.from_pandas(df[["question"]])


def parse_number(response_text: str) -> str:
    """
    Extract only the first numeric value from the model's output. 
    As HuggingFace always starts the output with "Answer:", the code takes that into account.
    """
    import re

    # Handle BC years as negative numbers
    bc_pattern = re.compile(r"(\d+(\.\d+)?)\s?BC", re.IGNORECASE)
    match_bc = bc_pattern.search(response_text)
    if match_bc:
        return str(round(-float(match_bc.group(1)), 2))

    # New logic: Find the first numeric value with advanced regex
    numeric_pattern = re.compile(r"Answer:\s*[^\d]*(-?\d[\d,]*(?:\.\d+)?)")
    match_num = numeric_pattern.search(response_text)
    if match_num:
        # Remove commas for proper parsing and round the number
        numeric_value = match_num.group(1).replace(",", "")
        return str(round(float(numeric_value), 2))

    return ""



def main():
    parser = argparse.ArgumentParser(description="Run model inference on the questions.")
    parser.add_argument("--hf_token", type=str, default=os.getenv("HF_TOKEN"), help="Hugging Face login token (or set as environment variable HF_TOKEN)")
    parser.add_argument("--dataset_path", type=str, default="data/questions_only.csv", help="Path to the questions_only CSV (default: data/questions_only.csv)")
    args = parser.parse_args()

    # Logging into Hugging Face
    from huggingface_hub import login
    login(token=args.hf_token)

    # Preprocessing the dataset
    dataset = preprocess_questions(args.dataset_path)
    print(f"Loaded {len(dataset)} questions.")

# Configure quantization for 8-bit
    quant_config = BitsAndBytesConfig(load_in_8bit=True)

    # Loading model with quantization
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID, 
        trust_remote_code=True, 
        device_map="auto", 
        quantization_config=quant_config  # Enable 8-bit quantization
    )
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)

    # Initializing pipeline
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device_map="auto",
        
    )

    # Processing the questions in batches
    results = []
    for i in range(0, len(dataset), BATCH_SIZE):
        batch = dataset.select(range(i, min(i + BATCH_SIZE, len(dataset))))["question"]
        prompts = [
            f"Only provide a numeric answer, no extra details. "
            f"Do not repeat or rephrase the question. "
            f"If any year is BC, use a negative sign (e.g., 200 BC → -200).\n"
            f"Question: {question}\nAnswer:"
            for question in batch
        ]

        # Getting the answers
        outputs = pipe(prompts, max_new_tokens=MAX_NEW_TOKENS, do_sample=False)

        # Post-processing the answers
        for question, prompt, output in zip(batch, prompts, outputs):
            raw_output = output[0]["generated_text"]  # Access the first element of the output list
            answer_text = raw_output[len(prompt):].strip()  # Strip the prompt from the output
            numeric_output = parse_number(answer_text)
            results.append({
                "question": question,
                "raw_output": raw_output,
                "numeric_output": numeric_output
            })

        # Print progress
        print(f"Processed batch {i // BATCH_SIZE + 1}/{len(dataset) // BATCH_SIZE + 1}.", flush=True)

    # Saving the results
    df_results = pd.DataFrame(results)
    df_results.to_csv(OUTPUT_CSV, index=False)
    print(f"Results saved to {OUTPUT_CSV}.")


if __name__ == "__main__":
    main()