# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
#  For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
# Example: 1284734

number =  1284734
new_number = str(1284734)
print(" " .join(new_number[::-1]))