'''
Sayılardan oluşan bir listeden yeni bir liste oluştursun. 
Yeni listenin itemlerı ilkinin tersi olsun. 
Sadece ikiye bölünmeyenleri içersin.


EX: Benim listem:       [1, 2, 3, 4, 5]
    İstediğim liste:    [5, 3, 1]
'''


def ReverseOddList(myList: list) -> list:
    newList = []

    for item in myList:
        try:
            if item % 2 == 0:
                continue
        except Exception as exceptionObject:
            return 1
        newList.append(item)
    newList.reverse()
    return newList   

lst = [1, 2, 3, 4, 5]
print(ReverseOddList(lst))