# EXERCISE 5
# Exercise 5: Check if the first and last number of a list is the same 
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def num_check(list):
    if (list[0] == list[-1]):
        print("True")
    else:
        print("False")


num_check([10, 20, 30, 40, 10])     
num_check([75, 65, 35, 75, 30])
#