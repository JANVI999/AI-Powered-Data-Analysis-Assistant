import chromadb
from chromadb.config import Settings
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def create_vector_store(schema_description: str, persist_directory: str = ".chroma"):
    """Create a vector store with schema and example queries."""
    
    # Documents to embed - schema info and example Q&A pairs
    documents = [
        schema_description,
        "Question: What is the total revenue? Answer: Sum the revenue column.",
        "Question: Top products by sales? Answer: Group by product, sum quantity, sort descending.",
        "Question: Revenue by region? Answer: Group by region, sum revenue.",
        "Question: Which category sells most? Answer: Group by category, sum quantity.",
        "Question: Average order value? Answer: Calculate mean of revenue column.",
        "Question: Monthly sales trend? Answer: Group by month from date, sum revenue.",
        "Question: Enterprise vs SMB revenue? Answer: Group by customer_type, sum revenue.",
    ]
    
    embeddings = OpenAIEmbeddings()
    
    vector_store = Chroma.from_texts(
        texts=documents,
        embedding=embeddings,
        persist_directory=persist_directory,
        collection_name="data_context"
    )
    
    return vector_store

def get_vector_store(persist_directory: str = ".chroma"):
    """Load existing vector store."""
    embeddings = OpenAIEmbeddings()
    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
        collection_name="data_context"
    )
