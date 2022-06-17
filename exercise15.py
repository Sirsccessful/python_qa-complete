# Exercise 15: Write a function called exponent(base, exp) 
# that returns an int value of base raises to the power of expre


def exponent(base,exp):
    result = 1
    for i in range(exp):
        result *= base
        
    return result

print(exponent(2,5))