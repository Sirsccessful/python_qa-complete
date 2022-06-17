# EXERCISE NO 3:
# Exercise 3: Print characters from a string that are present at an even index number 
# Write a program to accept a string from the user and display characters that are present at an even index number. 
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

x = input("Enter the word ")
char_list = []
for i in range(0,len(x)):
    if i % 2 == 0:
        char_list.append(x[i])
print(char_list)