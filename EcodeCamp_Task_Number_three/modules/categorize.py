import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datasets.grocery_categories import grocery_categories


def categorize_items(item_list):
    categorized_items = {}
    for item in item_list:
        category = grocery_categories.get(item.lower(), 'miscellaneous')
        if category not in categorized_items:
            categorized_items[category] = []
        categorized_items[category].append(item)
    return categorized_items
