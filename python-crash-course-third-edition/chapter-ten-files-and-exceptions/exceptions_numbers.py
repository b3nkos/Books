print("The sum of two number")

while True:

    try:
        number_one = int(input("Enter the first number: "))
        number_two = int(input("Enter the second number: "))
    except ValueError:
        print("[x] Please enter valid number")
    else:
        print(f"[+] The sum of the number is: {number_one + number_two}")
        break