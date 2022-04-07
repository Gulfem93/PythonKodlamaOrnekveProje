
'''
Programda verilen bir listeden itemları tuplardan oluşan yeni bir liste oluşturulsun 
Listeyi oluşturulan tupların 2 itemı olurken ilki sayıyı, ikincisi sayının küpünü gösterir.
Oluşan liste küçükten büyüğe sıralansın. 

EX: Benim Listem:    [2, 1, 3] 
    Oluşan Liste:    [(1, 1), (2, 8), (3, 27)]

'''

def FindingTheCubeOfTheNumber(myList: list) -> list:
    newList = []    # boş listem
    sortList = myList   
    sortList.sort()     # Listeyi sıraladım

    for item in sortList:
        new = []
        cube = item**3  # Sayının kübü alındı
        
        new.append(item)    # Bos listenin içine sayı eklendi.
        new.append(cube)    # Sayı eklendikten sonra sayının kübü eklendi.

        newTupple = tuple(new)  # Listeyi tuple dönüştürüldü
        newList.append(newTupple)   # Dönüşen tuple listeye eklendi
    
    return newList

lst = [2, 1, 3]
print(FindingTheCubeOfTheNumber(lst))


# ------------------------

sampleList = [2, 1, 3, 8, 12, 5]
sampleList.sort()
# sampleList.sort(reverse = True)   dersem tersine sıralar

resultLİst = [(item, pow(item,3)) for item in sampleList]
print(resultLİst)