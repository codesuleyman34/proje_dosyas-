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