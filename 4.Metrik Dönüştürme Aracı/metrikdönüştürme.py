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