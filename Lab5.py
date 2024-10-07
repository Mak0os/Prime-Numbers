# Program Name: Lab5.py
# Course: IT1114/Section XXX
# Student Name: Daniel Urdaneta
# Assignment Number: Lab5
# Due Date: 10/6/24
# Purpose: This program prompts the user for a starting and ending number, then prints all the prime numbers between that range.

# Function to check if a number is prime
def is_prime(n):
    # Prime numbers are greater than 1
    if n < 2:
        return False
    # Check for divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:  # If divisible by any number other than 1 and itself, it is not prime
            return False
    return True

# Main function to get input and print prime numbers
def main():
    # Prompt user for starting and ending numbers
    start = int(input("Starting Number: "))
    end = int(input("Ending Number: "))

    # Print prime numbers in the given range inclusively
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

# Call the main function
main()
