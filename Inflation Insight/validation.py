# validation.py

def validate_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Please enter a non-empty value.")

def validate_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid numeric value.")
