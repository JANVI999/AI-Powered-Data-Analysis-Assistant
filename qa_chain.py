import pandas as pd
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

def create_qa_chain(vector_store, df: pd.DataFrame):
    """Create the RAG-powered Q&A chain."""
    
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    prompt = ChatPromptTemplate.from_template("""
You are a data analyst assistant. Answer questions about the sales dataset.

Context from knowledge base:
{context}

Current dataframe info:
- Shape: {df_shape}
- Columns: {columns}

User question: {question}

Instructions:
1. Write Python pandas code to answer the question
2. The dataframe is available as `df`
3. Store the final result in a variable called `result`
4. After the code block, explain the answer in plain English

Respond in this format:
```python
# Your pandas code here
result = ...
