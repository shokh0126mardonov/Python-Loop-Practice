from random import randint

number = randint(100,999)

print(number) # sinov uchun chiqarilyabti
count = 0

while True:
    number_tax = int(input("Taxmin qilinayotgan raqamni kiriting:"))
    count+=1
    
    if number != number_tax:
        print("yana urinib ko'ring!")
    else:
        print(f"tabriklayman siz {count}-martada to'g'ri topdingiz")
        break