# Expense Tracker

A simple command-line expense tracking application built with Python that helps you manage and monitor your personal expenses.

## Description

This expense tracker allows users to record their daily expenses, categorise them, and view spending summaries. All data is stored in a CSV file for easy access and portability.

## Features

- **Add Expense**: Record new expenses with date, category, amount, and optional notes
- **View an Expense**: Filter and view expenses by specific category
- **View All Expenses**: Display a complete list of all recorded expenses
- **View Summary**: See total spending and breakdown by category
- **Persistent Storage**: All expenses are automatically saved to a CSV file

## Requirements

- Python 3.6 or higher
- No external libraries required (uses only Python standard library)

## Installation

1. Clone or download this repository to your local machine
2. Ensure Python 3.6+ is installed on your system
3. Navigate to the project directory

## File Structure

```
Python Project 1/
├── Project1.py      # Main application file
├── expenses.csv     # Data storage (created automatically)
└── README.md        # This file
```

## Usage

### Running the Application

Open a terminal/command prompt in the project directory and run:

```bash
python Project1.py
```

### Menu Options

When you run the application, you'll see the following menu:

```
=== Expense Tracker ===
1) Add Expense
2) View an Expense
3) View all Expenses
4) View Summary
5) Exit
```

### Adding an Expense

1. Select option `1` from the menu
2. Enter the date in `DD-MM-YY` format (e.g., 19-01-26)
3. Enter a category from the allowed options: **Food**, **Clothes**, **Rent**, or **Transport**
4. Enter the amount as a number (e.g., 25.50)
5. Optionally add a note describing the expense

**Note**: The application validates the date format and only accepts the four predefined categories.

### Viewing an Expense by Category

- Select option `2` to filter expenses by a specific category
- Enter one of the allowed categories: Food, Clothes, Rent, or Transport
- The system will display all expenses matching that category

### Viewing All Expenses

- Select option `3` to see a numbered list of all recorded expenses
- Each entry shows: date, category, amount (in £), and notes

### Viewing Summary

- Select option `4` to see spending statistics
- Displays total amount spent across all categories
- Shows breakdown of spending by category

### Exiting

- Select option `5` to exit the program safely

## Data Storage

- Expenses are stored in `expenses.csv` in the same directory as the program
- The CSV file is created automatically on the first expense entry
- Data format: `date,category,amount,note`
- The file can be opened with any spreadsheet application for additional analysis

## Example Session

```
=== Expense Tracker ===
1) Add Expense
2) View an Expense
3) View all Expenses
4) View Summary
5) Exit

Select an option: 1
Enter date (DD-MM-YY): 19-01-26
Enter category ["Food", "Clothes", "Rent", "Transport"]: Food
Enter amount: 15.50
Enter note (optional): Lunch at cafe

Expense added successfully.
```

## Notes

- Currency is displayed in British Pounds (£) by default
- All numeric amounts are stored with 2 decimal places
- The program validates numeric input for amounts
- Empty expenses.csv file will be created automatically if it doesn't exist

## Future Enhancements

Potential features for future versions:
- Edit or delete existing expenses
- Filter expenses by date range or category
- Export summaries to different formats
- Budget tracking and alerts
- Multiple currency support
- Data visualisation with charts

## License

This project is free to use and modify for personal or educational purposes.

## Author

Created as a personal finance management tool.

## Author

Created as a personal finance management tool.

