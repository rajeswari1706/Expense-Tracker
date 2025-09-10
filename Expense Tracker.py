# Expense Tracker System
# By Raje

import os
from datetime import datetime

FILE_NAME = "expenses.txt"

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter Category (Food/Travel/Shopping/Other): ")
    amount = input("Enter Amount: ")
    note = input("Enter Note (optional): ")
    record = f"{date},{category},{amount},{note}\n"
    with open(FILE_NAME, "a") as f:
        f.write(record)
    print("✅ Expense added successfully!\n")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No expenses found.\n")
        return
    print("\n--- All Expenses ---")
    with open(FILE_NAME, "r") as f:
        for line in f:
            date, category, amount, note = line.strip().split(",", 3)
            print(f"{date} | {category} | ₹{amount} | {note}")
    print()

def monthly_summary():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No expenses found.\n")
        return
    
    summary = {}
    with open(FILE_NAME, "r") as f:
        for line in f:
            date, category, amount, note = line.strip().split(",", 3)
            month = date[:7]  # YYYY-MM
            summary[month] = summary.get(month, 0) + float(amount)
    
    print("\n--- Monthly Summary ---")
    for month, total in summary.items():
        print(f"{month}: ₹{total}")
    print()

def main():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print("🚪 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
1