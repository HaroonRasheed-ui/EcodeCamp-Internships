import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datasets.grocery_categories import alternative_items


def suggest_alternatives(item_list):
    alternatives = {}
    for item in item_list:
        if item in alternative_items:
            alternatives[item] = alternative_items[item]
    return alternatives
