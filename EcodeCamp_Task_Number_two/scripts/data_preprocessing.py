import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load the dataset from CSV."""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """Preprocess the health data for analysis."""
    # Fill missing values (fixing the deprecation warning)
    data.ffill(inplace=True)
    
    # Standardize health metrics (e.g., weight, height)
    scaler = StandardScaler()
    health_metrics = ['weight', 'height', 'blood_pressure', 'cholesterol']

    # Check if the columns exist in the DataFrame before scaling
    available_columns = [col for col in health_metrics if col in data.columns]
    
    if not available_columns:
        raise KeyError("None of the specified health metrics are in the DataFrame!")
    
    # Standard scaling for available columns
    data[available_columns] = scaler.fit_transform(data[available_columns])
    
    return data

if __name__ == "__main__":
    data = load_data('data/personal_health_tracker_dataset.csv')
    processed_data = preprocess_data(data)
    processed_data.to_csv('data/processed_health_data.csv', index=False)
