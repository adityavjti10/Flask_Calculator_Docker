from calculator_core import Calculator

calc = Calculator()

print("Add:", calc.add(5, 3))
print("Subtract:", calc.subtract(10, 2))
print("Multiply:", calc.multiply(4, 3))
print("Divide:", calc.divide(8, 2))

print("\nHistory:")
for i, record in enumerate(calc.read_history()):
    print(f"{i}: {record}")

# Update a record
calc.update_record(0, {"result": 999})

# Delete a record
calc.delete_record(1)

print("\nUpdated History:")
for i, record in enumerate(calc.read_history()):
    print(f"{i}: {record}")
