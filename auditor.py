inventory = 0

while True:
    input_value = input("Enter the number of items to add to inventory (or type 'quit' to exit): ")
    if input_value == "quit":
        break
    val = int(input_value)
    inventory += val

print(f"Total inventory: {inventory}")