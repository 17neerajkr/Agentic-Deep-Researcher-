# Agentic-Deep-Researcher-


LinkUp (Search Tool)




CrewAI (Agentic Design)




Deepseek R1 (LLM)




Streamlit (as the UI layer)




Here’s a clean, GitHub-ready README.md designed to look professional and visually engaging 👇





<div align="center">
  <h1>🧠 Agentic-Deep-Researcher-LinkUp</h1>
  <p><strong>AI-powered Agentic Research Framework</strong></p>

  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge" alt="Streamlit">
  <img src="https://img.shields.io/badge/LLM-Deepseek%20R1-blue?style=for-the-badge" alt="Deepseek">
  <img src="https://img.shields.io/badge/Agents-CrewAI-green?style=for-the-badge" alt="CrewAI">
  <img src="https://img.shields.io/badge/Search-LinkUp-orange?style=for-the-badge" alt="LinkUp">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</div>

---

## 🌟 Overview

**Agentic-Deep-Researcher-LinkUp** is an **agentic research assistant** built for performing **autonomous information discovery, retrieval, and summarization** using multi-agent reasoning and a modular AI design.

It combines:
- **🔍 LinkUp:** a powerful search & retrieval tool  
- **🧠 CrewAI:** the agentic framework for decision-making and orchestration  
- **💬 Deepseek R1:** a large language model for reasoning and content generation  
- **🖥️ Streamlit:** a sleek, interactive user interface  

Together, they form a unified research tool capable of finding, verifying, and summarizing knowledge efficiently.

---

## ⚙️ Core Features

- 🤖 **Agentic architecture:** multi-role agents (retriever, summarizer, verifier) working cooperatively  
- 🔍 **Smart search engine:** integrates with LinkUp for fast and accurate data retrieval  
- 🧩 **LLM-driven reasoning:** powered by Deepseek R1 for high-quality text synthesis and reasoning  
- 🧱 **Interactive UI:** Streamlit front-end for visual monitoring and agent control  
- 💾 **Reproducible results:** every run can be saved and replayed for transparency  

---

## 🧭 System Architecture




[ Streamlit UI ]

↓

[ CrewAI Orchestrator ] → [ Agents: Retriever | Synthesizer | Verifier ]

↓

[ LinkUp Search Tool ] → [ Web / PDFs / Local Sources ]

↓

[ Deepseek R1 LLM ] → [ Summaries / Insights / Reports ]





Each component plays a modular role — making the system flexible for research automation and educational or analytical use cases.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Agentic-Deep-Researcher-LinkUp.git
cd Agentic-Deep-Researcher-LinkUp



2️⃣ Setup Environment




python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt



3️⃣ Configure Environment Variables


Create a .env file:




DEESEEK_MODEL=deepseek-r1:latest
DEESEEK_HOST=http://localhost:11434
OLLAMA_NUM_GPU=1
OLLAMA_USE_CUDA=1
LINKUP_INDEX_PATH=./data/index
STREAMLIT_SERVER_PORT=8501



4️⃣ Launch the App




streamlit run app.py



Then visit 👉 http://localhost:8501
 in your browser.



🧪 Example Use Cases




🧠 Research assistant for academic writing




📰 News summarization and analysis




🔬 Literature review automation




🧾 Fact-checking and evidence synthesis




🌐 Knowledge discovery across domains





📂 Folder Structure




├── app.py                 # Streamlit UI logic
├── agents/                # CrewAI agent scripts
├── linkup/                # Search and retrieval modules
├── llm/                   # Deepseek integration and LLM clients
├── prompts/               # Prompt templates for agents
├── data/                  # Cached search results and indexes
└── README.md              # Project documentation




🧑‍💻 Contributing


Contributions are welcome!

To contribute:




Fork this repo




Create a new branch: git checkout -b feature/awesome-feature




Commit your changes: git commit -m "Add awesome feature"




Push your branch: git push origin feature/awesome-feature




Submit a Pull Request 🚀





🪪 License


This project is licensed under the MIT License — see the LICENSE
 file for details.



💡 Credits




LinkUp — Search & retrieval tool




CrewAI — Agentic orchestration framework




Deepseek R1 — Large language model for reasoning




Streamlit — Interactive interface




<div align="center">
  <strong>🌍 Empowering research with AI-driven, transparent, and reproducible intelligence.</strong>
</div>
```
