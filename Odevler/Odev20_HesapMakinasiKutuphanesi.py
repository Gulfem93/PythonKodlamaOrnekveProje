def Toplama(number1, number2):
    return number1 + number2

def Cikarma(number1, number2):
    return number1 - number2

def Carpma(number1, number2):
    return number1 * number2

def Bolme(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        print(f"ikinci sayi {number2} olamaz")
