import pandas as pd

def load_product_data(filepath):
    """Loads product data from a CSV file."""
    return pd.read_csv(filepath)
