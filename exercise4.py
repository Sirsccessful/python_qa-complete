# EXERCISE 4
def remove_char(x, n):
    # x = the string word; n = number of character to be removed starting from zero 
    if n > len(x):
        print(f"The slice number is higher than the length of {x} ")
    else:
        return(x[n:])
print(remove_char("antinterdenominationalism", 13))