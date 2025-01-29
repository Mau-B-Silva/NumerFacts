# NumerFacts: Evaluating Numerical Factuality in Large Language Models  

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)

## 📌 Overview  
NumerFacts is the first benchmark dataset designed to evaluate **numerical factuality** in large language models (LLMs). This study introduces a **question-answering** framework to systematically analyse how well pre-trained LLMs recall numerical facts without any enhancement techniques (e.g., retrieval-augmented generation or fine-tuning).

📄 **Paper:** [NumerFacts](./NumerFacts.pdf)  
🔗 **GitHub Repository:** [NumerFacts](https://github.com/Mau-B-Silva/NumerFacts)

---

## 🚀 Key Contributions  
- **Novel benchmark dataset:** Over **3,900 numerical facts** across **eight domains**.  
- **Evaluation of six open-source LLMs** in a **zero-shot** setting.  
- **Quantitative assessment of LLM accuracy, domain variability, and numerical recall.**  
- **Findings:** Large LLMs struggle with numerical precision, achieving only **27.14% exact matches** at best.

---

## 📂 Dataset  
The **NumerFacts** dataset consists of factual numerical question-answer pairs extracted from **Wikidata** across multiple domains. 

### **Dataset Columns**
rowID, entity, entityLabel, domain, property, propertyLabel, value, roundedValue, unitLabel, sitelinks, dateModified, entityType, question, fileName, sheetName, days_since_last_modified


### **Example Entry**
| rowID | entity | entityLabel | domain | property | propertyLabel | value | roundedValue | unitLabel | sitelinks | dateModified | entityType | question | fileName | sheetName | days_since_last_modified |
|--------|-----------------------------------|----------------------------------|----------------|------------------------------------------------|----------------|----------|--------------|------------------|-----------|---------------------|---------------|----------------------------------------------------------------------------------------------------|---------------------|------------|-----------------------|
| 1 | `http://www.wikidata.org/entity/Q26221172` | Enclosed Field with Ploughman | Art & Literature | `http://www.wikidata.org/prop/direct/P2284` | latest known price | 81312500 | 81312500 | United States dollar | 2 | 2024-10-12 15:34:49 | work of art | What is the latest known price of the Enclosed Field with Ploughman, by Vincent van Gogh, in United States dollars? | Art & Literature.xlsx | Art_price | 80 |

📄 **Make sure `questions_only.csv` is inside the `data/` folder.**

---

## 📊 Results & Findings  

| Model    | Percentage Exact Match (%) | Percentage Within Tolerance (5%) (%) |
|----------|--------------|----------------|
| Mixtral  | **27.14%**   | **49.53%**     |
| Llama    | 21.59%       | 43.58%         |
| Gemma    | 20.78%       | 44.46%         |
| Qwen     | 17.27%       | 35.67%         |
| Falcon   | 11.85%       | 28.33%         |
| BLOOM    | **2.44%**    | **13.42%**     |

### **Key Insights**
✅ **Best model (Mixtral) achieved 27.14% exact matches**, while the worst (BLOOM) only reached 2.44%.  
✅ **Performance varies significantly across domains**, with **Art & Literature** and **Personalities** performing well, while **Geography and Sports** posed challenges.  
✅ **No significant correlation was found** between **accuracy and factors like entity popularity, recency, or verbosity**.  

📄 *For full results and statistical analysis, see the* [`NumerFacts.pdf`](./NumerFacts.pdf) .*

---

## ⚙️ Installation & Usage  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/Mau-B-Silva/NumerFacts.git
cd NumerFacts
```

### **2️⃣ Install Dependencies**
If you have pip, install dependencies with:
```sh
pip install -r requirements.txt
```

### **3️⃣ Running the Models**
The model scripts require:  
✅ **A Hugging Face API token for authentication**  
✅ **The dataset file questions_only.csv in the data/ folder**  

Running a Model
Run each model like this. Best to run one by one given computational cost. Should be easy to create a file to run them sequentially if needed. Using Llama as example:
```
python models/llama.py --hf_token YOUR_HF_TOKEN
```
If your dataset is in a different location, specify:
```
python models/model_1.py --hf_token YOUR_HF_TOKEN --dataset_path custom/path/to/questions_only.csv
```

### **📖 Citation**
If you use this dataset or research in your work, please cite:

```
@article{silva2025numerfacts,
  author = {Mauricio Bernardo da Silva},
  title = {Evaluating numerical factuality through question-answering in a zero-shot setting with NumerFacts as benchmark: The accuracy of large language models in numerical information recall},
  journal = {Master Thesis, University of Amsterdam},
  year = {2025},
  url = {https://github.com/Mau-B-Silva/NumerFacts}
}
```

### **🛠 License**
This repository is licensed under:

MIT License for code: See LICENSE.
Creative Commons Attribution 4.0 (CC BY 4.0) for the dataset and paper: CC BY 4.0.

### **🤝 Contributing**
We welcome contributions! To contribute:

1- Fork the repository 🍴

2- Create a new branch ```git checkout -b feature-new-analysis```

3- Make your changes and submit a pull request (PR)

### **📬 Contact**
For questions or collaborations, reach out via:

📧 Email: mauricio.bernardo.silva@student.uva.nl

📄 Website: https://www.linkedin.com/in/mauriciobernardodasilva/

---
