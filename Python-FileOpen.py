"""
Dosya acmak icin:
    open(dosya-adi, dosya-erisim-kipi)

'w' ile dosya acarsak dosya yoksa olusturulur, varsa icerigi silinir ve tekrar olusturur.
'a' ile dosya acarsak dosya yoksa olusturulur, varsa iceriginin sonuna ekleme yapar.
'r' ile dosya acarsak dosya yoksa hata verir, varsa icerigini okur.
'r+' ile dosya acarsak dosya yoksa hata verir, varsa icerigini okur ve yazma islemi yapar.
'b' ile dosya acarsak dosya ikili (binary) kipte acilir.
'+' ile dosya acarsak dosya okuma ve yazma kipinde acilir.

for example:

    open("ornek.txt", "w")
    file = open("ornek.txt", "a")
    file.write("Merhaba dunya!\n")
    file.write("Python ile dosya islemleri.\n")
    file.close()

    file = open("C:\\Users\\KullaniciAdi\\Belgeler\\ornek.txt", "r")
    icerik = file.read()
    print(icerik)
    file.close()

Pythonda actigimiz dosyalarla isimiz bittiginde dosyayi kapatmak onemlidir.
Bunu otamatik olarak yapmak icin 'with' ifadesini kullanabiliriz:
    with open("ornek.txt", "r") as file:
        icerik = file.read()
        print(icerik)

Pythonda dosya icini okumak icin kullanabilecegimiz bazi metodlar vardir:
    file.seek(0)  # Dosya imlecini baslangica goturur
    file.read()   # Dosyanin tum icerigini okur
    file.readline()  # Dosyadan bir satir okur
    file.readlines() # Dosyadaki tum satirlari liste olarak okur
    file.tell()      # Dosya imlecinin mevcut konumunu dondurur

Ornek:
    with open("ornek.txt", "r") as file:
        print("Dosya imlecinin konumu:", file.tell())
        icerik = file.read(10)
        print("Okunan icerik:", icerik)
        print("Dosya imlecinin konumu:", file.tell())

Dosyaya birseyler eklemek icin 'write()' ve 'writelines()' metodlarini kullanabiliriz:
    with open("ornek.txt", "a") as file:
        file.write("Yeni bir satir ekleniyor.\n")
        file.writelines(["Satir 1\n", "Satir 2\n", "Satir 3\n"])    

Yeni bir index eklemek icin:
    with open("ornek.txt", "r+") as file:
        liste = file.readlines()
        file.seek(0, 2)  # Dosya imlecini dosyanin sonuna goturur
        file.write("Dosyanin sonuna yeni bir satir ekleniyor.\n") 
        file.seek(0)     # Dosya imlecini baslangica goturur
        for i in liste:     # Dosyadaki mevcut satirlari tekrar yazar
            file.write(i)

# Ornek:           
   open("TvRemote.py", "r")
file = open("TvRemote.py", "r")
icerik = file.read()
print(icerik) 
 
"""

