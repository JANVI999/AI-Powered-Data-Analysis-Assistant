# AI-Powered-Data-Analysis-Assistant
Built a GenAI Q&amp;A system using OpenAI, LangChain &amp; Python to let non-technical teams query data in English. Used RAG &amp; Vector DBs on Streamlit to cut SQL requests by 60% and slash insight turnaround from hours to &lt;2 mins. Optimized decision-making across 3 functions by automating complex data analysis and real-time reporting.
# Architecture Breakdown
1. Data Layer (pandas, NumPy)
Loads and processes structured business data (CSVs, databases, Excel files)
Cleans, transforms, and prepares data for querying
2. RAG (Retrieval-Augmented Generation) Pipeline
Vector Database: Stores embeddings of your data schema, column descriptions, and sample queries
LangChain: Orchestrates the flow—takes the user's question, retrieves relevant context from the vector DB, and constructs a prompt for the LLM
OpenAI API: The LLM interprets the question, generates SQL or pandas code, executes it, and returns a natural language answer
3. Frontend (Streamlit)
Simple web interface where users type questions and see results
Displays charts, tables, or text answers

# Project Structure
ai-data-analyst/
├── app.py                 # Streamlit frontend
├── src/
│   ├── __init__.py
│   ├── data_loader.py     # Load and prep data
│   ├── embeddings.py      # Vector DB setup
│   ├── qa_chain.py        # LangChain RAG pipeline
│   └── utils.py           # Helper functions
├── data/
│   └── sample_sales.csv   # Sample dataset
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

