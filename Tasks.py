import datetime
from file_handler import expense_tracker,json
def add_expenses():
    while True:
        description= input("Add expense: ").title()
        price= int(input("Enter price: "))
        category= input("Enter category: ")
        date= datetime.datetime.now()

        expense_tracker.append({
            "description": description, "price": price, "category": category, "date": date
        })
        print(f"{description}, has been added to the expense tracker")
        end_input= input("Do you want to add another expense? (y/n): ")

        if end_input == "y":
            continue
        else:
            print("Expenses added successfully")

    with open("expense_tracker.json", "w") as file:
        json.dump(expense_tracker,file, indent=2)

def find_expenses():
    expense_lookup=input("Enter expense description: ").title()
    for expense in expense_tracker:
        if expense_lookup == expense["description"]:
            return expense
    print(f"cant seem to find {expense_lookup} in your tracker")
    return expense_lookup

def view_expenses():
    print("-" * 60)
    print(f"{'description':<18} {'price':<15} {'category':<18} {'date':<15} ")
    print("-" * 60)
    for expense in expense_tracker:
        print(f"{expense['description']:<18} £{expense['price']:<15} {expense['category']:<18} {expense['date']}")
        break
    print("hmm.. cant seem to find expense in your tracker")

def calculate_expenses():
    total_expense = 0
    for expense in expense_tracker:
        total_expense += expense["price"]
    if  total_expense > 0:
        print(f"Your total expenses is: {total_expense}")
    else:
        print("You have no expenses yet, try adding. We won't judge ;)")

def search_expenses():
   category_search= input("Enter category:")
   print("-" * 60)
   print(f"{'description':<18} {'price':<15} {'category':<18} {'date':<15} ")
   print("-" * 60)
   for expense in expense_tracker:
       if expense["category"] == category_search:
           print(f"{expense['description']:<18} £{expense['price']:<15} {expense['category']:<18} {expense['date']:<18}")
           return expense
   print(f"cant seem to find {category_search} in your tracker")
   return None
