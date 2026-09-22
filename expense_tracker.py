import csv
import os
from collections import defaultdict

FILE_NAME = "expenses.csv"


def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid amount.")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Category", "Description", "Amount"])

        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\n--- All Expenses ---")

        found = False
        for row in reader:
            found = True
            print(
                f"{row['Date']} | {row['Category']} | "
                f"{row['Description']} | ₹{row['Amount']}"
            )

        if not found:
            print("No expenses recorded.")


def filter_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    category = input("Enter category to filter: ").lower()

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print(f"\n--- Expenses in {category} ---")

        found = False

        for row in reader:
            if row["Category"].lower() == category:
                found = True
                print(
                    f"{row['Date']} | {row['Description']} | "
                    f"₹{row['Amount']}"
                )

        if not found:
            print("No expenses found for this category.")


def category_summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    totals = defaultdict(float)

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            totals[category] += amount

    print("\n--- Category Summary ---")

    if not totals:
        print("No expenses recorded.")
        return

    for category, total in totals.items():
        print(f"{category}: ₹{total:.2f}")


def main():
    while True:
        print("\n==============================")
        print("     PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
