def my_funcsion(x, y,z):
    if x > y and x > z:
        print(f"{x} son katta")
    elif y > x and y > z:
        print(f"{y} son katta")
    elif z > x and z > y:
        print(f"{z} son katta")
x = int(input("X- sonni kiriting: "))
y = int(input("Y- sonni kiriting: "))
z = int(input("Z- sonni kiriting: "))
my_funcsion(x=x, y=y, z=z)
