class TvRemote():

    def __init__(self, Tv_situatie = "Uit", kanaal_list = ["NOS", "RTL"], volume = 0, difult_kanal = "NOS"):
        self.Tv_situatie = Tv_situatie
        self.kanaal_list = kanaal_list
        self.volume = volume
        self.difult_kanal = difult_kanal
    
    def Tv_aan(self):
        
        if self.Tv_situatie == "Uit":
            self.Tv_situatie = "Aan"
            print("Tv is nu Aan")
        else:
            print("Tv is al Aan")

    def Tv_uit(self):
        
        if self.Tv_situatie == "Aan":
            self.Tv_situatie = "Uit"
            print("Tv is nu Uit")
        else:
            print("Tv is al Uit")

    def volume_omhoog(self):

        while True:
            antwoord = input("Om het volume omhoog te doen: '+'. Om het volume omlaag te doen: '-'. Om te stoppen: 'stop'")

            if antwoord == "+":
                if(self.volume != 100):
                    self.volume += 1
                    print(f"Het volume is nu: {self.volume}")
            elif antwoord == "-":
                if ( self.volume != 0):
                    self.volume -= 1
                    print(f"Het volume is nu: {self.volume}")
            else:
                print("Ongeldig antwoord, probeer het opnieuw.")
                break
        return self.volume

    def kanaal_toevoegen(self):
        nieuw_kanaal = input("Welk kanaal wil je toevoegen?")
        self.kanaal_list.append(nieuw_kanaal)
        print(f"Het kanaal {nieuw_kanaal} is toegevoegd.")

    def kanaal_verwijderen(self):
        kanaal_verwijderen = input("Welk kanaal wil je verwijderen?")
        if kanaal_verwijderen in self.kanaal_list:
            self.kanaal_list.remove(kanaal_verwijderen)
            print(f"Het kanaal {kanaal_verwijderen} is verwijderd.")
        else:
            print(f"Het kanaal {kanaal_verwijderen} bestaat niet in de lijst.")

    def __str__(self):
        return (f"Tv situatie: {self.Tv_situatie}\n"
                f"Beschikbare kanalen: {', '.join(self.kanaal_list)}\n"
                f"Huidig volume: {self.volume}\n"
                f"Standaard kanaal: {self.difult_kanal}"
                )
    
print("""
Welkom bij de Tv Remote
1. Tv aanzetten
2. Tv uitzetten
3. Volume aanpassen
4. Kanaal toevoegen
5. Kanaal verwijderen
6. Toon Tv status
7. Afsluiten  
""")

while True:
    keuze = input("Maak een keuze (1-7):")
    if (keuze == "7"):
        print("Tv Remote wordt afgesloten.")
        break
    elif (keuze == "1"):
        remote = TvRemote()
        remote.Tv_aan()
    elif (keuze == "2"):
        remote.Tv_uit()
    elif (keuze == "3"):
        remote.volume_omhoog()
    elif (keuze == "4"):
        remote.kanaal_toevoegen()
    elif (keuze == "5"):   
        remote.kanaal_verwijderen()
    elif (keuze == "6"):
        print(remote)
    else:
        print("Ongeldige keuze, probeer het opnieuw.")
