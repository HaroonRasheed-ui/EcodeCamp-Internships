import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  # Regression model
import joblib  # For saving the model

def train_health_model(data):
    """Train a health analysis model on the provided data."""
    
    # List of required columns
    required_columns = ['activity_duration', 'calorie_intake', 'age', 'weight', 'height']
    
    # Check if all required columns are present in the data
    available_columns = [col for col in required_columns if col in data.columns]
    
    if not available_columns:
        raise KeyError(f"None of the specified columns {required_columns} are present in the DataFrame!")

    if len(available_columns) < len(required_columns):
        missing_cols = set(required_columns) - set(available_columns)
        print(f"Warning: The following columns are missing and will be excluded: {missing_cols}")
    
    # Proceed with the available columns
    X = data[available_columns]

    # Assuming a continuous target variable exists, like 'health_score' (Adjust if necessary)
    if 'health_score' not in data.columns:
        raise KeyError("The target variable 'health_score' is not present in the DataFrame!")

    y = data['health_score']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a regression model (e.g., Random Forest Regressor)
    model = RandomForestRegressor()  # Use a regression model
    model.fit(X_train, y_train)
    
    # Save the trained model to a file
    model_filename = 'models/health_recommendation_model.pkl'
    joblib.dump(model, model_filename)
    print(f"Model saved to {model_filename}")
    
    return model

if __name__ == "__main__":
    # Load your data
    data = pd.read_csv('data/personal_health_tracker_dataset.csv')
    
    # Train the health model
    trained_model = train_health_model(data)
    print("Model training completed.")
