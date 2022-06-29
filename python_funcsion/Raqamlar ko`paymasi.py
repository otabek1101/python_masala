def my_funcsion():
    global s,a
    for i in s:
      a*=i
    print(a)

a=0
s=[]
while True:
    x = int(input('Raqam kiriting: '))
    if x <= 9:   
        s.append(x)
        y = str(input('Yana kiritasizmi: (ha/yuq)'))
        if 'ha'==y :
            continue
        else:
            break
    else:
        print("Iltimos raqam kiriting!!!")
        continue
    
my_funcsion()    
