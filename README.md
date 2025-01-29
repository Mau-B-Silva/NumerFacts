# NumerFacts: Evaluating Numerical Factuality in Large Language Models  

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)

## 📌 Overview  
NumerFacts is the first benchmark dataset designed to evaluate **numerical factuality** in large language models (LLMs). This study introduces a **question-answering** framework to systematically analyse how well pre-trained LLMs recall numerical facts without any enhancement techniques (e.g., retrieval-augmented generation or fine-tuning).

📄 **Thesis:** [Final Version](./NumerFacts.pdf)  
🔗 **GitHub Repository:** [NumerFacts](https://github.com/Mau-B-Silva/NumerFacts)

## 🚀 Key Contributions  
- **Novel benchmark dataset:** Over **3,900 numerical facts** across **eight domains**.  
- **Evaluation of six open-source LLMs** in a **zero-shot** setting.  
- **Quantitative assessment of LLM accuracy, domain variability, and numerical recall.**  
- **Findings:** Large LMs struggle with numerical precision, achieving only **27.14% exact matches** at best.

## 📂 Dataset  
The **NumerFacts** dataset is structured as follows:


### **Example Entry**
| rowID | entity | entityLabel | domain | property | propertyLabel | value | roundedValue | unitLabel | sitelinks | dateModified | entityType | question | fileName | sheetName | days_since_last_modified |
|--------|-----------------------------------|----------------------------------|----------------|------------------------------------------------|----------------|----------|--------------|------------------|-----------|---------------------|---------------|----------------------------------------------------------------------------------------------------|---------------------|------------|-----------------------|
| 1 | `http://www.wikidata.org/entity/Q26221172` | Enclosed Field with Ploughman | Art & Literature | `http://www.wikidata.org/prop/direct/P2284` | latest known price | 81312500 | 81312500 | United States dollar | 2 | 2024-10-12 15:34:49 | work of art | What is the latest known price of the Enclosed Field with Ploughman, by Vincent van Gogh, in United States dollars? | Art & Literature.xlsx | Art_price | 80 |

### **Key Features**
- **Over 3,900 numerical fact entries** spanning **eight domains** (e.g., Art & Literature, Geography, Sports).
- **Each entry includes a question-answer pair**, making it suitable for **question-answering LLM evaluation**.
- **Dates of last modification** (`dateModified`) allow analysis of how recency impacts numerical accuracy.
- **Unit labels included** (`unitLabel`), ensuring that LLMs are tested on proper unit consistency.

➡️ **The full dataset is available in the `data/` folder.**

---

## 📊 Results & Findings  

| Model    | Exact Match (%) | Approximate Match (%) |
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

📄 *For full results and statistical analysis, see the* [`NumerFacts.pdf`](./NumerFacts.pdf) *or the* [`results/`](./results/) *folder.*

---

## ⚙️ Installation & Usage  
To replicate the experiments, follow these steps:

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/Mau-B-Silva/NumerFacts.git
cd NumerFacts






