def my_funcsion():
    i = 0   
    while True:
        a = 0
        i+=1
        for k in range(1,i):
            if i % k ==0:
                a+=k
        if a==i :
            print(i)

my_funcsion()        
