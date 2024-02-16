def hava_bilgisi(hava_listesi):
    for şehir, tarif in hava_listesi.items():
        print(f"{city}:")
        print(f"Sıcaklık: {process['sıcaklık']}")
        print(f"Hava Durumu: {process['hava_durumu']}")
        print()

def add_city(weaher_list):
    city= input("Şehir adını girin: ")
    celcius = input("Sıcaklık bilgisini girin: ")
    weather = input("Hava durumu bilgisini girin: ")

    weaher_list[city] = {
        'sıcaklık': celcius,
        'hava_durumu': weather
    }
def delete_city(weaher_list):
    city = input("Silmek istediğiniz şehir adını girin: ")
    if city in weaher_list:
        del weaher_list[city]
        print(f"{city} başarıyla silindi.")
    else:
        print(f"{city} listede bulunamadı.")

weaher_list = {}

while True:
    print("1. Yeni şehir eklemek")
    print("2. Hava durumu bilgilerini görmek")
    print("3. Şehir silmek")
    print("q veya Q. Çıkış")

    vote = input("Bir seçenek girin (1-4): ")

    if vote == "1":
        add_city(weaher_list)
    elif vote == "2":
        weather_information(weaher_list)
    elif vote == "3":
        delete_city(weaher_list)
    elif vote == "q" or vote == "Q":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçenek. Tekrar deneyin.")