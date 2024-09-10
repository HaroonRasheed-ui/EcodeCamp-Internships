# Intelligent Grocery List Organizer

## Overview

The **Intelligent Grocery List Organizer** is a Python-based application designed to help users manage their grocery shopping efficiently. The application allows users to input grocery items, categorizes them, suggests alternatives for unavailable items, and optimizes the shopping route within the store based on item categories.

## Features

- **User Input Interface**: Simple UI to add grocery items.
- **Category Assignment**: Automatically categorizes items into sections like produce, dairy, bakery, etc.
- **Suggestion System**: Provides alternative suggestions for items that are unavailable or based on user preferences.
- **Shopping Route Optimization**: Suggests an optimized shopping route within the store to minimize travel.

## Project Structure

The project is organized into the following directories and files:

intelligent_grocery_organizer/ │ ├── datasets/ │ ├── grocery_categories.py │ ├── modules/ │ ├── ui.py │ ├── categorize.py │ ├── suggestions.py │ ├── route_optimizer.py │ └── app.py


### File Descriptions

- **datasets/grocery_categories.py**: Contains the dataset for grocery categories and alternative items.
- **modules/ui.py**: Contains the code for creating the user interface using Tkinter.
- **modules/categorize.py**: Handles the categorization of grocery items.
- **modules/suggestions.py**: Provides alternative suggestions for grocery items.
- **modules/route_optimizer.py**: Optimizes the shopping route based on item categories.
- **app.py**: The main application file that integrates all modules and runs the application.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/intelligent_grocery_organizer.git


2. Navigate to the project directory:

bash
cd intelligent_grocery_organizer

3. Ensure you have Python installed (Python 3.6+ is recommended). 

    Install required packages:

   ```bash
   pip install tkinter

## Usage

1. Run the application:
   ```bash
   python app.py

2. The application window will open. Enter grocery items into the input field and click "Add Item" to add them to the list.

3. Click "Process List" to categorize the items, get suggestions for alternatives, and optimize the shopping route.

4. Results will be displayed in a pop-up window.

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or comments, please contact haroon941rasheed@gmail.com.
