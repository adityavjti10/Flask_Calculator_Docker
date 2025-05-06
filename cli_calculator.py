from calculator_core import Calculator

calc = Calculator()

def menu():
    print("\n----- Calculator Menu -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Update Record")
    print("7. Delete Record")
    print("8. Exit")

def get_input():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

while True:
    menu()
    choice = input("Select an option (1-8): ")

    if choice == '1':
        a, b = get_input()
        print("Result:", calc.add(a, b))
    elif choice == '2':
        a, b = get_input()
        print("Result:", calc.subtract(a, b))
    elif choice == '3':
        a, b = get_input()
        print("Result:", calc.multiply(a, b))
    elif choice == '4':
        a, b = get_input()
        print("Result:", calc.divide(a, b))
    elif choice == '5':
        print("\n--- History ---")
        for i, record in enumerate(calc.read_history()):
            print(f"{i}: {record}")
    elif choice == '6':
        idx = int(input("Enter record index to update: "))
        new_result = float(input("Enter new result value: "))
        if calc.update_record(idx, {"result": new_result}):
            print("Updated successfully.")
        else:
            print("Invalid index.")
    elif choice == '7':
        idx = int(input("Enter record index to delete: "))
        if calc.delete_record(idx):
            print("Deleted successfully.")
        else:
            print("Invalid index.")
    elif choice == '8':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
