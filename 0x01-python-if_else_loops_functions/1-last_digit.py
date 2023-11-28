#!/usr/bin/python3
import random

def last_digit_check(number):
    last_digit = abs(number) % 10
    if last_digit > 5:
        return "negative"
    else:
        return "not negative"

number = random.randint(-10, 10)
result = last_digit_check(number)
print(f"Last digit of {number} is {result}")

