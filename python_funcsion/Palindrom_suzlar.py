def my_funcsion(x):
    y = (x[::-1])
    if x.upper() == y.upper():
        print("Bu so`z palindrom: ")
    else:
        print("Bu so`z palindrom emas: ")
x = str(input("Palindrom so`zlarni kiriting: "))
my_funcsion(x)   
