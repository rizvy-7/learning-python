# learning define and return
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to {name}!")


happy_birthday("bro", 30)


def display_invoice(customer_name, amount_due, due_date):
    print(f"Dear {customer_name}, your invoice amount is ${amount_due}")
    print(f"Please pay by {due_date}")


display_invoice("Rizvy", 1200, "30/12/2024")  # Example usage
