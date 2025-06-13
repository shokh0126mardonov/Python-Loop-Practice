result = 'Toshkent'.lower()

count = 0

while True:
    savol = input('O\'zbekiston poytaxti nima?').lower()
    count+=1
    if result == savol: 
        print(f"Tabriklayman siz {count}-martada to'g'ri topdingiz!")   
        break
