import json
from datetime import datetime

FILE_NAME = "finance_data.json"


# ---------- LOAD DATA ----------
def load_data():
    try:
        file = open(FILE_NAME, "r")
        data = json.load(file)
        file.close()

        if type(data) != list:
            data = []
    except:
        data = []

    return data


# ---------- SAVE DATA ----------
def save_data(data):
    file = open(FILE_NAME, "w")
    json.dump(data, file, indent=4)
    file.close()


# ---------- ADD INCOME ----------
def add_income(data):
    amount = float(input("Enter income amount: "))

    entry = {}
    entry["type"] = "income"
    entry["amount"] = amount
    entry["category"] = "General"
    entry["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data.append(entry)
    save_data(data)

    print("Income added successfully.")


# ---------- ADD EXPENSE ----------
def add_expense(data):
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    entry = {}
    entry["type"] = "expense"
    entry["amount"] = amount
    entry["category"] = category
    entry["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data.append(entry)
    save_data(data)

    print("Expense added successfully.")


# ---------- VIEW TRANSACTIONS ----------
def view_transactions(data):
    print("\n------------------------------")

    if len(data) == 0:
        print("No transactions found.")
        return

    for t in data:
        print("Type:", t["type"])
        print("Amount:", t["amount"])
        print("Category:", t["category"])
        print("Date:", t["date"])
        print("------------------------------")


# ---------- VIEW SUMMARY ----------
def view_summary(data):
    total_income = 0
    total_expense = 0

    for t in data:
        if t["type"] == "income":
            total_income = total_income + t["amount"]
        else:
            total_expense = total_expense + t["amount"]

    balance = total_income - total_expense

    print("Total Income:", total_income)
    print("Total Expense:", total_expense)
    print("Balance:", balance)


# ---------- CATEGORY ANALYSIS ----------
def category_analysis(data):
    categories = {}

    for t in data:
        if t["type"] == "expense":
            cat = t["category"]

            if cat in categories:
                categories[cat] = categories[cat] + t["amount"]
            else:
                categories[cat] = t["amount"]

    if len(categories) == 0:
        print("No expense data available.")
        return

    for cat in categories:
        print(cat, ":", categories[cat])


# ---------- MAIN ----------
def main():
    data = load_data()

    while True:
        print("\n------ Personal Finance Manager ------")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Category Analysis")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            view_transactions(data)
        elif choice == "4":
            view_summary(data)
        elif choice == "5":
            category_analysis(data)
        elif choice == "6":
            print("Program exited.")
            break
        else:
            print("Invalid option.")



import matplotlib.pyplot as plt

# ---------- EXPENSE PIE CHART ----------
def show_expense_pie_chart(data):
    categories = {}

    for t in data:
        if t["type"] == "expense":
            cat = t["category"]
            if cat in categories:
                categories[cat] = categories[cat] + t["amount"]
            else:
                categories[cat] = t["amount"]

    if len(categories) == 0:
        print("No expense data to plot.")
        return

    labels = []
    values = []

    for cat in categories:
        labels.append(cat)
        values.append(categories[cat])

    plt.figure()
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.show()


# ---------- UPDATED MAIN WITH PIE CHART ----------
def main():
    data = load_data()

    while True:
        print("\n------ Personal Finance Manager ------")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Category Analysis")
        print("6. Show Expense Pie Chart")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            view_transactions(data)
        elif choice == "4":
            view_summary(data)
        elif choice == "5":
            category_analysis(data)
        elif choice == "6":
            show_expense_pie_chart(data)
        elif choice == "7":
            print("Program exited.")
            break
        else:
            print("Invalid option.")


main()
