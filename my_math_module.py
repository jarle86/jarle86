def my_math (a,b):
    mult = a * b
    sum = a + b 
    rest = a - b
    div = a / b

    print('\n',mult, '\n' ,sum, '\n',rest,'\n',div)

if __name__ == "__main__":
    import sys
    my_math(int(sys.argv[1,2]))