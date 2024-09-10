import pandas as pd

def filter_by_budget(product_data, budget):
    """Filter products by budget."""
    return product_data[product_data['Price'] <= budget]

def filter_by_categories(product_data, categories):
    """Filter products by multiple categories."""
    return product_data[product_data['Category'].isin(categories)]
