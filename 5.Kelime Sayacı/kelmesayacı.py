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