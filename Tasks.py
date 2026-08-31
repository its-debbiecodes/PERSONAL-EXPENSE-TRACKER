import datetime
from storage import expense_tracker,json
def add_expenses():
    while True:
        description= input("Add expense: ").title()
        price= valid_input("Enter price: ")
        category= input("Enter category: ").title()
        date= datetime.datetime.now().strftime("%d-%m-%y")

        expense_tracker.append({
            "description": description, "price": price, "category": category, "date": date
        })
        print(f"{description}, has been added to the expense tracker")
        end_input= input("Do you want to add another expense? (y/n): ").lower()

        if end_input == "n":
            print("expenses added successfully")
            break
        else:
            continue

    with open("personal_expense_tracker.json", "w") as file:
        json.dump(expense_tracker,file, indent=2)

def find_expenses():
    expense_lookup=input("Enter expense description: ").title()
    for expense in expense_tracker:
        if expense_lookup == expense["description"]:
            return expense
    print(f"can't seem to find {expense_lookup} in your tracker")
    return None

def view_expenses():
    print("-" * 60)
    print(f"{'description':<18} {'price':<15} {'category':<18} {'date':<15} ")
    print("-" * 60)
    for expense in expense_tracker:
        print(f"{expense['description']:<18} £{expense['price']:<15} {expense['category']:<18} {expense['date']}")


def calculate_expenses():
    total_expense = 0
    for expense in expense_tracker:
        total_expense += expense["price"]
    if  total_expense > 0:
        print(f"Your total expenses is: {total_expense}")
    else:
        print("You have no expenses yet, try adding. We won't judge ;)")

def search_expenses():
   category_search= input("Enter category:").title()
   print("-" * 60)
   print(f"{'description':<18} {'price':<15} {'category':<18} {'date':<15} ")
   print("-" * 60)
   for expense in expense_tracker:
       if expense["category"] == category_search:
           print(f"{expense['description']:<18} £{expense['price']:<15} {expense['category']:<18} {expense['date']:<18}")
           continue

   print(f"cant seem to find {category_search} in your tracker")
   return None

def delete_expenses():
    expense_to_delete=find_expenses()
    if expense_to_delete:
        expense_tracker.remove(expense_to_delete)
        print(f"{expense_to_delete['description']} has been removed from the expense tracker")
    else:
        print(f"Cant seem to find expense in your tracker")

    with open("personal_expense_tracker.json", "w") as file:
        json.dump(expense_tracker,file, indent=2)

def valid_input (prompt:str)-> float:
    while True:
        try:
            price= float(input(prompt))
            if 0 <= price <= 10000:
                return price
            else:
                print(f"{prompt} is not a valid price, might want to try again.")
        except ValueError:
            print("Not a valid number, try a number between 0 and 10000")

def exit_program():
    print("Goodbye.. But dont forget to track your expenses this week.\nI will be watching!")
    exit()