import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load your dataset
data = pd.read_csv('data/personal_health_tracker_dataset.csv')

# Define features and target variable
X = data[['activity_duration', 'calorie_intake', 'age', 'weight', 'height']]
y = data['health_score']  # Ensure this is a continuous variable

# Initialize and train the model
model = RandomForestRegressor()
model.fit(X, y)

# Save the trained model
with open('models/health_recommendation_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved successfully.")
