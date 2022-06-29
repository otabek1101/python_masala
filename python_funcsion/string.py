katta_harflar = ['Q','E','R', 'T', 'Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','V','B','N','M']
kichik_harflar = ['q','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','v','b','n','m']
def my_funcsion():
    s = 0
    A = str(input("Ma`lumot yozing: "))
    for i in A:
        if i in katta_harflar:
            s+=1
        elif i in kichik_harflar:
            s+=1
    if len(A)==s :
        print('string')
    else:
        print('not string')
my_funcsion()      
    
