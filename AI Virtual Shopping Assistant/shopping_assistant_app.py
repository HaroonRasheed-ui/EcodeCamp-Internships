import streamlit as st
import time
import pandas as pd
from recommendation_engine import get_recommendations
from product_data_collection import load_product_data
from user_preference_modeling import filter_by_budget, filter_by_categories
from voice_interaction import listen_for_command, assistant_speak, interpret_command, interpret_add_to_cart, checkout


# Load product data
ecommerce_data = load_product_data('data/ecommerce_data.csv')

# Initialize shopping cart in session state
if 'shopping_cart' not in st.session_state:
    st.session_state['shopping_cart'] = []

# Streamlit UI
st.title("AI Virtual Shopping Assistant - Voice & Text Enabled")

# Select interaction mode: Voice or Text
interaction_mode = st.radio("Select Interaction Mode", ('Voice Assistant', 'Type Input'))

# Set a dynamic budget
budget = st.slider("Select Your Budget", min_value=50, max_value=10000, step=50, value=500)

# Multi-category selection
categories = st.multiselect("Select Categories", ecommerce_data['Category'].unique())

# Display current shopping cart
st.subheader("Current Cart:")
if st.session_state['shopping_cart']:
    for item in st.session_state['shopping_cart']:
        st.write(f"- {item['ProductName']} (Price: {item['Price']})")
else:
    st.write("Your cart is empty.")

# Voice or text-based interaction
if interaction_mode == 'Voice Assistant':
    if st.button("Give a voice command"):
        user_command = listen_for_command()
        if user_command:
            st.write(f"Command received: {user_command}")
            action = interpret_command(user_command)

            if action and 'budget' in action:
                budget = action['budget']
                st.write(f"Budget updated to: {budget}")

            if action and 'category' in action:
                if action['category'] not in categories:
                    categories.append(action['category'])
                st.write(f"Category added: {action['category']}")

            # Handle adding products via voice
            interpret_add_to_cart(user_command, st.session_state['shopping_cart'], ecommerce_data)

            # Checkout via voice
            if "checkout" in user_command:
                checkout(st.session_state['shopping_cart'])

else:
    st.write("Using Type Input Mode")

    # Filter products by categories and budget
    if categories:
        filtered_products = filter_by_categories(ecommerce_data, categories)
        filtered_products = filter_by_budget(filtered_products, budget)
        st.write(f"Products under {budget} in selected categories:")
        st.dataframe(filtered_products)

    # Add selected product to cart manually
    product_id = st.text_input("Enter Product ID to Add to Cart")
    if st.button("Add to Cart"):
        if product_id:
            try:
                product_id = int(product_id)
                selected_product = ecommerce_data[ecommerce_data['ProductID'] == product_id]
                if not selected_product.empty:
                    st.session_state['shopping_cart'].append({
                        "ProductName": selected_product['ProductName'].values[0],
                        "Price": selected_product['Price'].values[0]
                    })
                    st.write(f"Product {product_id} added to cart")

                    # Force a rerun to update the cart display
                    st.rerun()
                    
                else:
                    st.write(f"Product ID {product_id} not found")
            except ValueError:
                st.write("Invalid Product ID. Please enter a valid number.")

    # Checkout button
    if st.button("Checkout"):
        checkout(st.session_state['shopping_cart'])
