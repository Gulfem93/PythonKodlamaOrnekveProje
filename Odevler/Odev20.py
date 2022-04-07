'''
Programı dort işlem yapan basit bir hesap makinası görsün
'''

from Odev20_HesapMakinasiKutuphanesi import Cikarma, Carpma, Bolme, Toplama 

number1 = int(input("Birinci sayıyı giriniz: "))
number2 = int(input("İkinci sayıyı giriniz: "))

print("Toplama işlemi icin 1 giriniz")
print("Cıkarma işlemi icin 2 giriniz")
print("Çarpma işlemi icin 3 giriniz")
print("Bolme işlemi icin 4 giriniz")

while True:
    number = int(input("0 - 4 arasında bir deger giriniz: "))

    if True:
        if number == 1:
            print(Toplama(number1, number2))
        elif number == 2:
            print(Cikarma(number1, number2))
        elif number == 3:
            print(Carpma(number1, number2))
        elif number == 4:
            print(Bolme(number1, number2))

    print("işlemi sonlandırmak için h(ayır):  ")
    sequel = input()
    
    if sequel.lower() == "h":
        print("İşlem sonlandı")
        break
                    