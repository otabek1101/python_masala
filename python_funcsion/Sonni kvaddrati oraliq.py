def my_funcsion():
    x = []
    q = int(input("1 -oraliqni kiriting: "))
    w = int(input("2 -oraliqni kiriting: "))
    for i in range(q , w+1):
        y = i**2
        x.append(y)
    print("Kiritilgan oraliqdagi sonlarning kvadrati")
    for k in x:
        print(k)
my_funcsion()
