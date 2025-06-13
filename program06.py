from random import randint

number = randint(1,100)
print(number)
count = 0

while True:
    tax_number = int(input("number = "))
    count += 1
    if number == tax_number and count < 4:
     print(f'Tabriklaymiz siz {count}-martada to\'g\'ri topdingiz')
     break
    elif count>=4:
        print("Urinishlar tugadi")
        break