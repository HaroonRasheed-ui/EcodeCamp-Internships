
# AI Virtual Shopping Assistant

This project is an AI-powered virtual shopping assistant that allows users to interact using voice commands. The assistant can understand user preferences, set budgets, select product categories, and add items to the shopping cart based on the user's instructions.

## Features

- **Voice Interaction**: Users can interact with the assistant via voice commands for real-time shopping assistance.
- **Text-to-Speech**: The assistant speaks back to the user for confirmation and instructions.
- **Voice Commands**:
  - Set budget for shopping.
  - Select product categories.
  - Add products to the shopping cart using product IDs.
- **Real-Time Feedback**: The assistant listens to voice commands and provides real-time feedback to the user through speech.

## Requirements

To install the necessary dependencies for this project, use the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Project Structure

```
AI Virtual Shopping Assistant/
│
├── voice_interaction.py         # Main script to handle voice commands and interactions
├── requirements.txt             # Python dependencies required for the project
├── README.md                    # Project description and instructions
└── venv/                        # Python virtual environment (optional)
```

## How to Run

1. Install the necessary dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the `voice_interaction.py` script:
   ```bash
   python voice_interaction.py
   ```

## Usage

- **Start**: The assistant will ask for voice commands like setting a budget, choosing a product category, or adding items to the cart.
- **Example Commands**:
  - "Set my budget to 100 dollars."
  - "Select electronics category."
  - "Add product 3 to the cart."

## Dependencies

- `speech_recognition`
- `gtts`
- `sounddevice`
- `soundfile`

Make sure you have all the dependencies installed to ensure proper functionality of the virtual shopping assistant.

## Author

- Haroon Rasheed

## Notes

- The assistant uses Google Speech Recognition API for interpreting voice commands.
- The project is designed to work on Python 3.x.
