import random
def dice():
    while True:
        choise = int(input("Zarı kaç kere atmak istersiniz: "))
        return choise

def process(choise):
    if choise == 0:
        print("Öyle bir sonuç yok!")

    else:
        for dice in range(1,choise + 1):
            result = random.randint(1,6)
            print(result)

a = dice()
process(a)