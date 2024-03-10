def factorial(num,total = 1):
    #validate if num is greater than 0.
    if num < 0:
        print("Please indicate a number greater than 0")
    else:
        #calcula factorial number if condition is meet
        while num > 0:
            total *= num
            num -= 1
    return total

#request the user a positive interger number
num = int(input('Indicate a number to get the factorial: '))

result = factorial(num)

print("The factorial number is:", result)

