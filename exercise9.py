# Exercise 9: Check Palindrome Number Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

given_num = input(str("Enter the given number "))
new_num =given_num[::-1]
if new_num == given_num:
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")