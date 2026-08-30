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
        json.dump(expense_tracker,file, indent=4)

def find_expenses():
    expense_lookup=input("Enter expense: ").title()
    for expense in expense_tracker:
