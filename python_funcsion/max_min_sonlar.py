import math
son = []
def my_funcsion():
    while True:
        z = int(input("Son kiriting: "))
        son.append(z)
        x = str(input("Son kiritasizmi (ha->1/yuq->2): "))
        if x == "1":
            continue
        elif x =="2":
            y = input("Max sonlar -> 1\nmin sonlar-> 2\nMax va Min sonlarni ko`rish uchun -> 3\n>>>  ")
            if y == "1":
                r = max(son)
                print(f"Kiritgan sonlaringiz ichidan eng kattasi -> {r}")
            elif y == "2":
                t = min(son)
                print(f"Kiritgan sonlaringiz ichidan eng kichigi -> {t}")
            elif y == "3":
                print(f"Max son: {max(son)}\nMin son: {min(son)}")
            else:
                print("Bunday bulim yuq!!!")
my_funcsion()
    
    