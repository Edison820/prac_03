"""
CP1404 - Practical
Answer the following questions:
1. When will a ValueError occur? When a function receives data of the correct type but incorrect value.
2. When will a ZeroDivisionError occur? When a number is divided by 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print(0)
print("Finished.")