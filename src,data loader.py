import pandas as pd
from pathlib import Path

def load_data(file_path: str = "data/sample_sales.csv") -> pd.DataFrame:
    """Load and prepare the dataset."""
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df['revenue'] = df['quantity'] * df['unit_price']
    return df

def get_schema_description(df: pd.DataFrame) -> str:
    """Generate a natural language description of the dataframe schema."""
    schema_parts = ["Dataset: Sales Orders\n\nColumns:"]
    
    for col in df.columns:
        dtype = str(df[col].dtype)
        sample_values = df[col].dropna().unique()[:3]
        samples = ", ".join([str(v) for v in sample_values])
        schema_parts.append(f"- {col} ({dtype}): e.g., {samples}")
    
    schema_parts.append(f"\nTotal rows: {len(df)}")
    schema_parts.append(f"Date range: {df['date'].min()} to {df['date'].max()}")
    
    return "\n".join(schema_parts)
