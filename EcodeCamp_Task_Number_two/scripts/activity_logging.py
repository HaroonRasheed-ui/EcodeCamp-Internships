import pandas as pd
from datetime import datetime

def log_activity(user_id, activity, duration):
    """Log daily physical activities."""
    log_entry = {'user_id': user_id, 'activity': activity, 'duration': duration, 'date': datetime.now()}
    log_df = pd.DataFrame([log_entry])
    log_df.to_csv(f'data/activity_log_{user_id}.csv', mode='a', header=False, index=False)
    print("Activity logged successfully.")

def log_diet(user_id, food_item, calories):
    """Log daily diet."""
    log_entry = {'user_id': user_id, 'food_item': food_item, 'calories': calories, 'date': datetime.now()}
    log_df = pd.DataFrame([log_entry])
    log_df.to_csv(f'data/diet_log_{user_id}.csv', mode='a', header=False, index=False)
    print("Diet logged successfully.")

if __name__ == "__main__":
    log_activity(1, 'Running', 30)
    log_diet(1, 'Salad', 150)
