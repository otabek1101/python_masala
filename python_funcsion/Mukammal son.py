i = 0
while True:
    i +=1
    a = 0
    for k in range(1, i):
        if i%k==0:
            a+=k
    if a==i:
        print(i)
