#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number
sign = 1
if last_digit < 0:
    last_digit = -1 * last_digit
    sign = -1
if last_digit >= 10:
    last_digit = last_digit % 10
last_digit = sign * last_digit
print(f"Last digit of {number} is {last_digit}", end="")
if last_digit > 5:
    print(" and is greater than 5", end="")
elif last_digit == 0:
    print(" and is 0", end="")
elif last_digit < 6:
    print(" and is less than 6", end="")
    if last_digit != 0:
        print(" and not 0", end="")

print()
