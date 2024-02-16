import random

print("Taş Kağıt Makas Oyununa Hoşgeldiniz :)")
print("---"*20)

game = ["taş", "kağıt", "makas"]

def take_user_move():
    user_move = str(input("Taşmı Kağıtmı Makasmı: "))
    print("---"*20)
    return user_move.lower()

def take_pc_move(game):
    pc_move = random.choice(game)
    return pc_move

def result(user_move, pc_move):
    print("Oyuncu: ", user_move)
    print("Bilgisayar : ", pc_move)

    if user_move == pc_move:
        print("Berabere")
        print("---"*20)

    elif (((user_move == "taş" or user_move == "Taş") and pc_move == "Makas") or((user_move == "Kağıt" or user_move == "kağıt") and pc_move == "Taş") or((user_move == "makas" or user_move == "Makas") and pc_move == "Kağıt")):
        print("Oyuncu Kazandı")
        print("---"*20)

    else:
        print("Bilgisayar Kazandı")
        print("---"*20)

while True:
   user_move = take_user_move()
   pc_move = take_pc_move(game)
   result(user_move, pc_move)

   retry = str(input("Tekrar oynamak istermisiniz E/H:  "))

   if retry == "E" or retry == "e":
       continue

   elif retry == "H" or retry == "h":
       print("Çıkış yapılıyor...")
       break