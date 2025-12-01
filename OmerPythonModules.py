
def greet(name):
    return f"Hello, {name}!"

pi = 3.14159


class Calculator:
    def add(self, a, b):
        return a + b

#---------------------------------------------#

class softwarer():
    def __init__(self,isim,soyisim,salaris,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.salaris = salaris
        self.diller = diller

    def informatiesoftwarer(self):
        print("""
        İsim: {}
        Soyisim: {}
        Maaş: {}
        Diller: {}""".format(self.isim,self.soyisim,self.salaris,self.diller)
        )

    def dil_ekle(self, yeni_dil):
        self.diller.append(yeni_dil)
        print("Dil eklendi:", yeni_dil)

    # Maaş artırma tamamen kullanıcıya bağlı
    #Try ve Except kullanarak hata yönetimi ekledim. Eger kullanici sayi girerse program cokmek yerine hata mesajı verecek.
    def salaris_verhogen(self):
        x = input("Hoeveel wil je verhogen? ")
        try:
            artış = int(x)
            self.salaris += artış
            primannt("Nieuwe salaris is:", self.salaris)
        except:
            print("Lütfen bir sayı girin!")

software1 = softwarer("Omer","Kurt",5000,["Python","Java","C++"])
software1.informatiesoftwarer()

software1.salaris_verhogen()     # Kullanıcı artıracak
software1.dil_ekle("JavaScript")
software1.informatiesoftwarer()

#---------------------------------------------#

class Calisan():
    def __init__(self,isim,soyisim,maas,departman):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.departman = departman

    def informatiecalisan(self):
        print("""
        İsim: {}
        Soyisim: {}
        Maaş: {}
        Departman: {}""".format(self.isim,self.soyisim,self.maas,self.departman)
        )
    def departman_degistir(self,yeni_departman):
        self.departman = yeni_departman
        print("Departman değiştirildi:", yeni_departman)

class Yonetici(Calisan):
    pass 
Yonetici1 = Yonetici("Ahmet","Yılmaz",8000,"Satış")
Yonetici1.informatiecalisan()
Yonetici1.departman_degistir("Pazarlama")
Yonetici1.informatiecalisan()

#---------------------------------------------#

class car():
    def __init__(self,model,price,year,color):
        self.model = model
        self.price = price
        self.year = year 
        self.color = color

    def car_info(self):
        print("""
        Model:{}\
        Price:{}
        Year:{}
        Color:{}""".format(self.model,self.price,self.year,self.color))
        
car1 = car("Toyota",30000,2020,"Red")
car2 = car("Honda",28000,2019,"Blue")
car3 = car("Ford",25000,2018,"Black")

car1.car_info()
car2.car_info()
car3.car_info()