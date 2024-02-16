# GitHub Projesi

# 1. Projede Kullanılan Dil
## Projede Python dili kullanılmıştır.

# 2. Yapılan Projenin Amacı
## Projenin amacı kendimi Python dilinde geliştirmek için yaptığım projeleri sizinde kendinizi geliştirmek için kullanabilecğiniz şekilde GitHub'da paylaşmak.

# 3. Paylaşılan Projelerden Örnekler
## Zar Atma Uygulaması
``` python
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
```

## Taş - Kağıt - Makas Uygulaması
``` python
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
```

##  Kim Milyoner Olmak İster Bilgi Yarışması Uygulaması
``` python
competition = [{"Soru":"Enderun Bilişim kaç yılında açılmıştır","Seçenekler":["A) 2023","B) 2021","C) 2022", "D) 1984",], "Doğru Cevap":"A"},
               {"Soru":"180 sayısının 20 faslasının %5 'i kaçtır?","Seçenekler":["A)20","B)30","C)40","D)10"],"Doğru Cevap":"D"},
               {"Soru":"İstiklal marşında en az geçen kelime nedir","Seçenekler":["A) Kan","B) Toprak","C) Vatan","D) Yurt", ],"Doğru Cevap":"B"},
               {"Soru":"Peygamber Efendimiz (S.A.V) kaç yılında doğmuştur","Seçenekler":["A) 632","B) 333","C) 571","D) 874", ],"Doğru Cevap":"C"}]

sayaç = 0

for i in range(len(competition)):
    for key,value in competition[i].items():
        if key == "Soru":
            print(value)
        elif key == "Seçenekler":
            print(value)
        elif key == "Doğru Cevap":
            user_answer = str(input(""))

            if user_answer == value:
                print("Doğru Bildiniz:)")
                sayaç += 1
            else:
                print("Cevap: ",value,"Yanlış Bildniz:(")

if sayaç == 4:
    print("Hepsini doğru bildiniz 1.000.000 TL'cik Kazandınız ")
elif sayaç < 4:
    print("Hepsini doğru bilemediniz")
```

## Metrik Dönüştürme Aracı Uygulaması
``` python
# Gramı kiloya çevirme
def kilo_gram(weight):
    return weight / 1000

weight = int(input("Kilonuzu Girermisiniz (Gram cinsinden giriniz): "))
sonuc = kilo_gram(weight)
print(sonuc)
print("---"*20)

# Santimi metreye çevirme

def santim_metre(size):
    return size / 1000

size = float(input("Boyunuzu Girermisiniz (Metre cinsinden giriniz):"))
sonuc2 = santim_metre(size)
print(sonuc2)
```

## Kelime Sayacı Uygulaması
``` python
sayac = 0
def take_text():
    text = str(input("Bir metin giriniz: "))
    return text
def find_word(text,sayac):
    for i in text:
        if i == " ":
            sayac += 1
    print("cümledeki kelime sayısı: ",sayac + 1)

text = take_text()
find_word(text,sayac)
```

## Film Kütüphanesi Uygulaması
``` python
movie_library = []

def movie_add():
    movie_the_title = input("Lütfen filmin adını girin:\n")
    movie_the_director = input("Lütfen filmin yönetmeninin adını girin:\n")
    movie_year = input("Lütfen filmin hangi yılda yayınlandığını girin:\n")

    movie = {
        "Başlık": movie_the_title,
        "Yönetmen": movie_the_director,
        "Yayın Yılı": movie_year
    }

    movie_library.append(movie)
    print(f"{movie_the_title} başlıklı film kütüphaneye eklendi.")

def show_movie_list():
    if not movie_library:
        print("Film kütüphanesi boş.")
    else:
        print("Film Kütüphanesi:")
        for movie in movie_library:
            print(f"Başlık: {movie['Başlık']}, Yönetmen: {movie['Yönetmen']}, Yayın Yılı: {movie['Yayın Yılı']}")

def movie_delete():
    movie_the_title_delete = input("Silmek istediğiniz film başlığını girin: ")
    delete_movie = None

    for movie in movie_library:
        if movie['Başlık'] == movie_the_title_delete:
            delete_movie = movie
            break

    if delete_movie:
        movie_library.remove(delete_movie)
        print(f"{movie_the_title_delete} başlıklı film kütüphaneden silindi.")
    else:
        print(f"{movie_the_title_delete} başlıklı film bulunamadı.")

def main_menu():
    while True:
        print("\nFilm Kütüphanesi Uygulaması")
        print("w. Film Ekle\n")
        print("a. Film Listesini Göster\n")
        print("s. Film Sil\n")
        print("q. Uygulamayı Kapat\n")

        choice = input("Seçiminizi yapın (w-a-s-q): ")

        if choice == "w":
            movie_add()
        elif choice == "a":
           show_movie_list()
        elif choice == "s":
            movie_delete()
        elif choice == "q":
            print("Uygulama kapatılıyor...")
            break
        else:
            print("Geçersiz seçenek. Tekrar deneyin.")

if __name__ == "__main__":
    main_menu()
```
