import csv
from pathlib import Path


FILE_PATH = Path("expenses.csv")
FIELDNAMES = ["date", "category", "amount", "note"]



def show_menu():
    print("\n=== Expense Tracker ===")
    print("1) Add Expense")
    print("2) View an Expense")
    print("3) View all Expenses")
    print("4) View Summary")
    print("5) Exit")


def add_expense(expenses):
    
    while True:
        date = input("Enter date (DD-MM-YY): ").strip()
        if len(date) == 8 and date[2] == "-" and date[5] == "-":
            break
        else:
         print("Invalid date format! Please use DD-MM-YY format (e.g., 19-01-26).")
    
  
    allowed_categories = ["Food", "Clothes", "Rent", "Transport"]
    while True:
        category = input(f"Enter category {allowed_categories}: ").strip()
        if category in allowed_categories:
            break
        else:
         print(f"Invalid category! Please choose from: {allowed_categories}")
    
    amount = float(input("Enter amount: ").strip())
    note = input("Enter note (optional): ").strip()

    expense = {
        "date": date,
        "category": category,
        "amount": amount, 
        "note": note
    }

    expenses.append(expense)
    append_expense_to_csv(expense)
    print("\nExpense added successfully.")


def view_expenses_by_category(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    category = input("which expense??: [\"Food\", \"Clothes\", \"Rent\", \"Transport\"] ").strip()
    for i in expenses:
        if i["category"]== category:
            print(i)
        else:
            print("no expenses in this category")
    

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. "
            f"Date: {expense['date']} | "
            f"Category: {expense['category']} | "
            f"Amount: £{expense['amount']:.2f} | "
            f"Note: {expense['note']}"
        )


def view_summary(expenses):
    if not expenses:
        print("No expenses to summarize yet.")
        return

    total = 0.0
    totals_by_category = {}

    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]

        total += amount
        totals_by_category[category] = totals_by_category.get(category, 0.0) + amount

    print("\n--- Summary ---")
    print(f"Total spent: £{total:.2f}")
    print("By category:")
    for category, amount in sorted(totals_by_category.items()):
        print(f"- {category}: £{amount:.2f}")



def load_expenses_from_csv():
    expenses = []

    if not FILE_PATH.exists():
        return expenses

    with FILE_PATH.open("r", newline="", encoding="utf-8") as F:
     reader = csv.DictReader(F)
     for row in reader:
            # Convert amount from string to float
            try:
                row["amount"] = float(row["amount"])
            except (ValueError, TypeError):
                row["amount"] = 0.0

            # Ensure keys exist even if missing in file
            row.setdefault("date", "")
            row.setdefault("category", "")
            row.setdefault("note", "")

            expenses.append(row)

    return expenses


def append_expense_to_csv(expense):
    file_exists = FILE_PATH.exists()

    with FILE_PATH.open("a", newline="", encoding="utf-8") as F:
     writer = csv.DictWriter(F, fieldnames=FIELDNAMES)

     if not file_exists or FILE_PATH.stat().st_size == 0:
            writer.writeheader()

     writer.writerow(expense)




def main():
 expenses = load_expenses_from_csv()

 while True:
        show_menu()
        choice = input("\nSelect an option: ").strip()
        if choice == "1":
          add_expense(expenses) 
        
        elif choice == "2":
          view_expenses_by_category(expenses) 

        elif choice == "3":
          view_expenses(expenses)

        elif choice == "4":
          view_summary(expenses)

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()