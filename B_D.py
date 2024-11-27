B_D

decimal_list = []

# Input the binary number in dotted format
binary_number = input("Enter a binary number (e.g., 11000000.10101000.00000001.00000001): ")

# Split the input string into parts based on "."
for part in binary_number.split("."):
    # Convert each binary part to a decimal integer
    decimal_part = int(part, 2)
    
    # Append the decimal part to the list
    decimal_list.append(decimal_part)

# Join the decimal parts with a '.' and display the result
decimal_result = ".".join(map(str, decimal_list))
print(f"The decimal number is: {decimal_result}")

D_B
binary_list = []

# Input the dotted decimal number
decimal_number = input("Enter a dotted decimal number (e.g., 192.168.1.1): ")

# Split the input string into parts based on "."
for part in decimal_number.split("."):
    # Convert each part to an integer
    part_as_int = int(part)
    
    # Convert the integer to binary and pad it to 8 bits
    binary_part = format(part_as_int, '08b')
    
    # Append the 8-bit binary part to the list
    binary_list.append(binary_part)

# Join the binary parts with a '.' and display the result
binary_result = ".".join(binary_list)
print(f"The 8-bit binary number is: {binary_result}")

