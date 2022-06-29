x = input('To`rt xonali son kiriting: ')
s = []
for i in x:
    s.append(i)
y = int(s[0]) + int(s[1])
a = int(s[2]) + int(s[3]) 

if a==y:
    print('Boshidan 2 raqam va oxirgi 2 raqam yig`indisi teng')
else:
    print('Boshidan 2 raqam va oxirgi 2 raqam yig`indisi teng emas')

print('Raqamlar yig`indisini 3 ga ko`pi: ',3 * (y + a))

q = int(s[0]) * int(s[1]) * int(s[2]) * int(s[3])

if q % 4==0:
    print('Raqamlar ko`paytmasi 4 ga karrali')
else:
    print('Raqamlar ko`paytmasi 4 ga karrali emas')
