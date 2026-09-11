inventory = 0

while True:
    input_value = input("Enter the number of items to add to inventory (or type 'quit' to exit): ")
    if input_value == "quit":
        break

    try:
        val = int(input_value) #Accept stock as integer
    except ValueError:
        print("Please enter a valid number or 'quit' to exit.")
        continue

    if val < 0:
        print("Please enter a positive number.")
    elif inventory + val > 500:
        print("Overstock Alert! Inventory would exceed 500 units.")
        break
    else:
        inventory += val

print(f"Total inventory: {inventory}")