import pickle
import os

from numpy import record

def DisplayMenu() -> None:
    print("1. Kayıtları Listele")
    print("2. Kayıt Ara")
    print("3. Kayıt Ekle")
    print("4. Kayıt Sil")
    print("5. Çıkış")
    print()

def MenuLoop():
    while True:
        DisplayMenu()
        option = input("Secenek (1-5): ")
        print("\n")

        if option.isdigit() and 1 <= int(option) <= 5:
            break
    
    return option

def MainLoop() -> None:
    while True:
        option = MenuLoop()

        if option == "1":
            ListRecord()
        elif option == "2":
            SearchRecord()
        elif option == "3":
            AddRecord()
        elif option == "4":
            DeleteRecord()
        elif option == "5":
            break


def ListRecord() -> None:
    recordList = ReadFile()
    print(f"Kayıt Sayısı: {len(recordList)}")
    print(f"{'İsim':^10}{'Soyisim':^10}{'Telefon':^11}")
    
    for record in recordList:
        print(f'{record.get("name", " "):10.10} {record.get("surName", " "):10.10} {record.get("telNumber", " "):11.11}')
    print()


def SearchRecord() -> None:
    print("Kayıt Arama")
    name = input("İsim: ")
    surName = input("Soyadı: ")

    recordList = SearchRecordFromFile(name, surName)
    print("Telefon Numarası", end="")
    for record in recordList:
        print(f'{record.get("telNumber"):11.11}')
    print("\n")


def AddRecord() -> None:
    print("Yeni Kayıt Ekle")
    name = input("İsim: ")
    surName = input("Soyadı: ")
    telNumber = input("Telefon Numarası: ")

    print(f"Yeni kayıt: {name} {surName} - {telNumber}")
    
    if AreYouSure():
        AddRecordToFile(name, surName, telNumber)
        print("Kayıt Eklendi \n")
    

def DeleteRecord() -> None:
    print("Kayıt Silmek")
    name = input("İsim: ")
    surName = input("Soyadı: ")

    recordsList = SearchRecordFromFile(name, surName)


def AreYouSure() -> bool:
    while True:
        answer = input("Emin misiniz? (E)vet / (H)ayır")
        print()
        if answer.upper() == "E":
            return True
        elif answer.upper() == "H":
            return False


def ReadFile() -> None:
    if os.path.isfile("data.bin"):
        with open("data.bin", "rb") as fileObject:
            recordList = pickle.load(fileObject)
    else:
        recordList = list()
    return recordList


def WriteFile(recordListParam: list) -> None:
    with open("data.bin", "wb") as fileObject:
        pickle.dump(recordListParam, fileObject)


def SearchRecordFromFile(nameParam: str, surNameParam: str) -> list:
    recordList = ReadFile()
    responseList = list()
    for record in recordList:
        if record.get("name").upper() == nameParam.upper() and record.get("surName").upper() == surNameParam.upper():
            responseList.append(record)
    
    return responseList


def AddRecordToFile(nameParam: str, surnameParam: str, telnumberParam: int) -> None:
    recordList = ReadFile()
    recordDict = dict(name = nameParam, surName = surnameParam, telNumber = telnumberParam)
    recordList.append(recordDict)
    WriteFile(recordList)

MainLoop()