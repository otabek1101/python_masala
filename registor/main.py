from cmath import phase
from read.read_kun import read_kun
from add.add import add_baza
from read.read_oraliq import read_oraliq
from read.read_gender import read_gender
from read.read_adress import read_adress
from read.read_country import read_country
from read.read_children import read_children
from read.read_id import read_id
from read.read_first_name import read_first_name

def main():
    sorov = input("Bzaga malumot qoshish uchun -> 1:\nBazadab malumot oqish uchun -> 2:\n>>>")
    if sorov == '1':
        id = int(input('ID kiriting: '))
        first_name = input('Ism kiriting: ')
        last_name = (input("Familiya kiriting: "))
        email = input("email kiriting: ")
        gender = input("Jinsingizni kiriting kiriting (Erkak -> Male; Ayol-> Female): ")
        phone = int(input("Telifon nomerizdi kiriting: "))
        adress = input("Manzilingizni kiriting: ")
        data = input("Tug`ilgan kunizni kiriting (Mana bu tarzda-> 08/11/1962): ")
        children = int(input("Farzandlariz soni: "))
        language = input("Qaysi tilni bilasiz(mislo-> Uzbek): ")
        country = input("Yasahaydigan davlatingizni kiriting: ")
        add_baza(id,first_name,last_name,email,gender,phone,adress,data,children,language,country)
    elif sorov == '2':
        sorov1 = str(input("""
        Malumotni qay usulda qidirmoqchisiz:
        ID bo`yicha qidiruv -> 1
        Ism bo`yicha qidirov -> 2
        Jinsi bo`yicha qidirish uchun -> 3
        Adress bo`yicha qidiruv -> 4
        Tug`ilgan kun bo`yicha qidiruv-> 5
        Farzandlar soni -> 6 
        Davlat bo`yicha qidiruv -> 7
        Tug`ilgan kunlarni oraliq bo`yicha qidiruv-> 8
        >>> """))
        if sorov1 == "1":
            k = int(input("ID bo`yicha qidiruv: "))
            read_id(k)
        elif sorov1 == "2":
            o = str(input("Ism bo`yicha qidiruv: "))
            read_first_name(o)
        elif sorov1 == "3":
            o = str(input("Erkak uchun -> 1\nAyyolar uchun -> 2\n>>>"))
            read_gender(o)
        elif sorov1 == "4":
            o = str(input("Adress bo`yicha qidiruv:"))
            read_adress(o)
        elif sorov1 == "5":
            k = int(input("Kun kiriting: "))
            o = int(input("Oy kiriting: "))
            read_kun(k, o)
        elif sorov1 == "6":
            k = int(input("Min farzandlar soni: "))
            l = int(input("Max farzandlar soni: "))
            read_children(k,l)
        elif sorov1 == "7":
            o = str(input("Davlat bo`yicha qidiruv: "))
            read_country(o)
        elif sorov1 == "8":
            k = int(input("1-Kun kiriting: "))
            l = int(input("2-Kun kiriting: "))
            o = int(input("Oy kiriting: "))
            read_oraliq(k,l,o)  
    else:
        print('Siz notogri buyruq tanladiz iltimos tekshirib qaytadan tanlang!!!')
        main()
main()