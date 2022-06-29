def my_funcsion(a):
    x = (a[::-1])
    if x.upper() == a.upper():
        print('bu so`z palindrom')
    else:
        print('bu so`z palindrom emas')
    
a = str(input("palindrom so`z kiriting: "))
my_funcsion(a)
    
