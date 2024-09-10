# AI-Powered Personal Health Tracker

## Overview

The AI-Powered Personal Health Tracker is a project that helps users monitor their health metrics and provides personalized recommendations based on their activity, diet, age, weight, and height. The application uses a machine learning model to analyze user data and offer insights to improve health.

## Project Structure

AI-Powered Personal Health Tracker/ │ ├── data/ │ ├── train.csv # Training data for the model │ ├── models/ │ ├── health_recommendation_model.pkl # Trained model │ ├── scripts/ │ ├── activity_logging.py # Functions to log activity and diet │ ├── recommendation.py # Functions to generate health recommendations │ ├── ui/ │ ├── main_ui.py # Main user interface script │ ├── requirements.txt # Project dependencies ├── README.md # Project overview and instructions └── train_model.py # Script to train and save the model

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd AI-Powered Personal Health Tracker

2. Install the dependencies:
   ```bash   
   pip install -r requirements.txt

## Training the Model

To train the model using the dataset, run the train_model.py script:
   ```bash
   python train_model.py
   ```
This script will train a RandomForest model and save it to the models/ directory

## Running the Application

To run the user interface, execute:
   ```bash
   python ui/main_ui.py
   ```
This will start the Tkinter application where you can log activities and diets and get health recommendations.

## Usage

- Log Activity: Enter activity details and duration to log it.
- Log Diet: Enter food items and calorie counts to log them.
- Get Health Recommendation: Enter your health metrics to get a personalized health recommendation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Haroon Rasheed


