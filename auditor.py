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
    
print(f"Total inventory: {inventory}")