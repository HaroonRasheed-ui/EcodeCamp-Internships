import joblib
import pandas as pd

def load_model():
    """Load the trained health recommendation model."""
    with open('models/health_recommendation_model.pkl', 'rb') as file:
        model = joblib.load(file)
    return model

def generate_recommendation(user_data):
    """Generate personalized health recommendations."""
    model = load_model()
    
    # Ensure user_data is in the correct format
    if isinstance(user_data, pd.DataFrame):
        user_metrics = user_data[['activity_duration', 'calorie_intake', 'age', 'weight', 'height']]
    else:
        raise ValueError("user_data should be a pandas DataFrame.")
    
    # Make predictions
    predicted_score = model.predict(user_metrics)
    
    # Generate recommendation based on predicted score
    if predicted_score > 70:
        return "You are in great health! Keep up the good work!"
    elif predicted_score > 40:
        return "You're doing well, but there's room for improvement. Focus on consistent exercise."
    else:
        return "Your health metrics need attention. Consider a more balanced diet and regular activity."

if __name__ == "__main__":
    # Example user data
    user_data = pd.DataFrame({
        'activity_duration': [45],
        'calorie_intake': [2000],
        'age': [30],
        'weight': [75],
        'height': [175]
    })
    
    # Generate recommendation
    recommendation = generate_recommendation(user_data)
    print("Recommendation:", recommendation)
