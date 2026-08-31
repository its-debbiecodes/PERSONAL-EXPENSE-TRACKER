from Tasks import add_expenses,view_expenses,calculate_expenses,search_expenses,delete_expenses,exit_program
import os
options=[
        "Add expense (Press a)",
        "View expenses (Press v)",
        "Calculate expenses (Press c)",
        "Search expenses (Press s)",
        "Delete expenses (Press d)",
        "Exit program (Press e)"
    ]
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    while True:
        title= "====== 💰 Personal Expense Tracker =====".upper().center(100)
        print(f"\n\033[35m{title}\033[0m\n")

        for index, option in enumerate(options, start=1):
            print(f"\033[32m{index}. {option}\033[0m")

        user_choice= input("What would you like to do? ")
        if user_choice == "a":
            add_expenses()
        elif user_choice == "v":
            view_expenses()
        elif user_choice == "c":
            calculate_expenses()
        elif user_choice == "s":
            search_expenses()
        elif user_choice == "d":
            delete_expenses()
        elif user_choice == "e":
            exit_program()

if __name__ == "__main__":
    main()


