import datetime

# Declaring global variables
expenses = {}
categories = set()
budget = 0

# Add the expenses
def add_expense(amount, description, category):
    global budget
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
    except ValueError:
        print("Invalid amount. Please enter a valid positive number.")
        return
    if not description:
        print("Description cannot be empty.")
        return
    if category.strip() == "":
        category = "Uncategorized"
    if category not in expenses:
        expenses[category] = []
    expenses[category].append({"amount": amount, "description": description, "date": datetime.datetime.now().strftime("%Y-%m-%d")})
    categories.add(category)
    print("Expense added successfully!")
    # Deduct the expense from budget
    budget -= amount

# Set budget
def set_budget():
    global budget
    budget = float(input("Enter your budget for this month: "))

# Get monthly summary
def get_monthly_summary(month, year):
    try:
        month = int(month)
        year = int(year)
    except ValueError:
        print("Invalid month or year.")
        return
    if month < 1 or month > 12:
        print("Invalid month. Month must be between 1 and 12.")
        return
    total_expense = 0
    monthly_expenses = {}
    for i, j in expenses.items():
        monthly_expenses[i] = 0
        for k in j:
            expense_date = datetime.datetime.strptime(k["date"], "%Y-%m-%d")
            if expense_date.month == month and expense_date.year == year:
                monthly_expenses[i] += k["amount"]
                total_expense += k["amount"]
    return total_expense, monthly_expenses

# Get category-wise summary
def get_category_summary(category):
    category_expenses=[]
    if category in expenses:
        for i in expenses[category]:
            category_expenses.append({"date": i["date"], "amount": i["amount"]})
        return category_expenses
    else:
        return None

# Function to take user input for adding an expense
def take_user_input():
    amount = input("Enter amount spent: ")
    description = input("Enter a brief description: ")
    category = input("Enter expense category ").strip()
    add_expense(amount, description, category)

# Take user input for adding expenses
def add_expenses():
    while True:
        take_user_input()
        another_expense = input("Would you like to add another expense? (yes/no): ").lower()
        if another_expense != "yes":
            break

set_budget()
add_expenses()
# Get monthly summary
month = input("Enter month (1-12): ")
year = input("Enter year: ")
total_expense, monthly_expenses = get_monthly_summary(month, year)
if total_expense:
    print("Total expense for {}/{}: {}".format(month, year, total_expense))
    print("Monthly expenses: ", monthly_expenses)
# Get category-wise summary
category = input("Enter category to get summary: ")
category_expense = get_category_summary(category)
if category_expense:
    for i in category_expense:
        print("Date:", i["date"], "Amount:", i["amount"])
else:
    print("No expenses found for category:", category)