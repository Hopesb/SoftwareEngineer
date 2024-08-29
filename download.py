# Get input from the user.
number = int(input("Enter a number:"))
# Check if the input is a prime number
for num in range(2, number):
    if number % num > 1:
        print(f"{number} is divisible by {num}")
    else:
        print(f"{number} is not divisble")