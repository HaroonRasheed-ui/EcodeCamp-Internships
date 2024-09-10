from modules.UI import create_ui
from modules.categorize import categorize_items
from modules.suggestions import suggest_alternatives
from modules.route_optimizer import optimize_shopping_route
import tkinter as tk
from tkinter import messagebox

# List to hold grocery items
items_list = []

# Function to add items to the list
def add_item_to_list(item):
    items_list.append(item)

# Function to process the grocery list
def process_list():
    categorized = categorize_items(items_list)
    alternatives = suggest_alternatives(items_list)
    optimized_route = optimize_shopping_route(categorized)

    # Display categorized items
    categorized_text = "Categorized Items:\n" + "\n".join([f"{cat}: {', '.join(items)}" for cat, items in categorized.items()])

    # Display suggestions
    alternatives_text = "Suggested Alternatives:\n" + "\n".join([f"{item}: {', '.join(alt)}" for item, alt in alternatives.items()])

    # Display optimized route
    route_text = "Optimized Shopping Route:\n" + " -> ".join(optimized_route)

    result_text = f"{categorized_text}\n\n{alternatives_text}\n\n{route_text}"

    messagebox.showinfo("Grocery List Processed", result_text)

# Create and run the UI
root = create_ui(add_item_to_list)

# Add process button to run the categorization, suggestion, and route optimization
process_button = tk.Button(root, text="Process List", command=process_list)
process_button.pack()

root.mainloop()
