x = int(input('1- oraliqni kiriting: '))
y = int(input('2- oraliqni kiriting: '))
a = int(input('Biror son kiriting: '))

def my_funcsion(x,y,a):
    
    for i in range(x, y):
        if i==a:
            return('Bu kiritilgan son oraliqda bor!')
        
    return('Bu kiritilgan son oraliqda yo`q!')
         


 
print(my_funcsion(x,y,a))
