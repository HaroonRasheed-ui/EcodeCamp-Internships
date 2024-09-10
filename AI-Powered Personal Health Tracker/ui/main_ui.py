import sys
import os
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pickle

# Add the 'scripts' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

def load_model():
    """Load the trained health recommendation model."""
    model_path = 'models/health_recommendation_model.pkl'
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def generate_recommendation(user_data):
    """Generate personalized health recommendations."""
    model = load_model()
    user_metrics = user_data[['activity_duration', 'calorie_intake', 'age', 'weight', 'height']]
    predicted_score = model.predict(user_metrics)
    
    if predicted_score > 75:
        return "You are in great health! Keep up the good work!"
    elif predicted_score > 50:
        return "You're doing well, but there's room for improvement. Focus on consistent exercise."
    else:
        return "Your health metrics need attention. Consider a more balanced diet and regular activity."

def generate_recommendation_action():
    """Generate a real-time recommendation based on user input."""
    # Collect user input from the UI fields
    activity_duration = int(duration_entry.get())
    calorie_intake = int(calories_entry.get())
    age = int(age_entry.get())
    weight = int(weight_entry.get())
    height = int(height_entry.get())
    
    # Create a dataframe with user inputs to pass to the model
    user_data = pd.DataFrame({
        'activity_duration': [activity_duration],
        'calorie_intake': [calorie_intake],
        'age': [age],
        'weight': [weight],
        'height': [height]
    })
    
    # Get health recommendation
    recommendation = generate_recommendation(user_data)
    
    # Display the recommendation
    messagebox.showinfo("Health Recommendation", recommendation)

# UI Setup
root = tk.Tk()
root.title("AI Health Tracker")

# User input fields
tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Weight (kg)").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (cm)").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Label(root, text="Activity Duration (minutes)").pack()
duration_entry = tk.Entry(root)
duration_entry.pack()

tk.Label(root, text="Calorie Intake").pack()
calories_entry = tk.Entry(root)
calories_entry.pack()

# Button to generate health recommendation
tk.Button(root, text="Get Health Recommendation", command=generate_recommendation_action).pack()

root.mainloop()
