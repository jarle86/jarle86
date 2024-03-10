'''
create a function to calculate the power of
a given number elevated to another given number
'''
 
def power(a, x, b):
    b = a**x
    return b

#request a number to the user
a = int(input('Insert a number: '))

#request a second number to elevate
x = int(input('Insert a number to elevate the power: '))

#calculate the power
print(f'{power(a,x)}')