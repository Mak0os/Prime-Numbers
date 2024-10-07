# Program Name: Lab5.py
# Course: IT1114/Section XXX
# Student Name: Daniel Urdaneta
# Assignment Number: Lab5
# Due Date: 10/6/24
# Purpose: This program prompts the user for a starting and ending number, then prints all the prime numbers between that range.

# Function to check if a number is prime
def is_prime(n):
    if n < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to the square root of n
        if n % i == 0:
            return False
    return True

# Main function to prompt user input and print prime numbers
def main():
    # Prompt the user for the starting and ending numbers
    start = int(input("Starting Number: "))
    end = int(input("Ending Number: "))

    # Iterate over the range and print prime numbers
    for num in range(start, end + 1):
        if is_prime(num) or num == 1:  # Include 1 in the output as per the given example
            print(num)
