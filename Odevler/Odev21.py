'''
Program metin dosyası içindeki tüm karakteri teker teker 15 sayısı ile xor yapsın. 
Oluşan yeni karakterin metinini bir dosyaya yazsın.
'''

from fileinput import filename

FileName = "Odev21_Sentence"
with open(FileName, "a+", encoding = "utf-8") as FileObject:
    while True:    
        kullaniciIsmi = input("Kullanici ismi giriniz:")

        if kullaniciIsmi == "":
            break

        FileObject.write(kullaniciIsmi)
   
with open(FileName, "rb") as FileObject:
    fileContent = FileObject.read()
    print(fileContent)

NewFileContent = ""


for byte in fileContent:
    NewFileContent += chr(byte ^ 15)

with open(f"{FileName}.new", "w") as FileObject:
    FileObject.write(NewFileContent)

print(NewFileContent)
