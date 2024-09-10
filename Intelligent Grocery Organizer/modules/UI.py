import tkinter as tk
from tkinter import messagebox

def create_ui(add_item_func):
    # Create the main application window
    root = tk.Tk()
    root.title("Intelligent Grocery List Organizer")
    root.geometry("400x300")

    # User input list
    items_list = []

    # Function to add items to the list
    def add_item():
        item = item_entry.get().strip()
        if item:
            add_item_func(item)
            listbox.insert(tk.END, item)
            item_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter an item.")

    # Create UI elements
    item_label = tk.Label(root, text="Enter Grocery Item:")
    item_label.pack()

    item_entry = tk.Entry(root)
    item_entry.pack()

    add_button = tk.Button(root, text="Add Item", command=add_item)
    add_button.pack()

    listbox_label = tk.Label(root, text="Grocery List:")
    listbox_label.pack()

    listbox = tk.Listbox(root)
    listbox.pack()

    return root
