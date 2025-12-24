# Deze file om try-except blokken te leren en testen #
#---------------------------------------------#

"""
try:
    a = int("kocpuasipu3289rw9inoasv")
    print(a)
except ValueError:
    print("Fout")
"""

#---------------------------------------------#

"""
try:
    b = int(input("Geef een getal op: "))
    print("Je hebt het getal {} opgegeven.".format(b))
except ValueError:
    print("Jij hebt geen geldig getal opgegeven!")
"""

#---------------------------------------------#

"""
try:
    c = int(input("Geef een getal op: "))
    resultaat = 100 / c
    print("100 gedeeld door {} is {}".format(c, resultaat))
except ValueError:
    print("Jij hebt geen geldig getal opgegeven!")
except ZeroDivisionError:
    print("Delen door nul is niet toegestaan!")
"""

#---------------------------------------------#

"""
try:
    x = int(input("Geef een getal op:"))
    print("Je hebt het getal {} opgegeven.".format(x))
except (ValueError, Exception):
    print("Foutmelding:", Exception, ZeroDivisionError)
print("Einde van het programma.")
"""

#---------------------------------------------#

"""
try:
    y = int(input("Geef een getal op:"))
    resultaat = 100 / y
    print("100 gedeeld door {} is {}".format(y, resultaat))
except ValueError:
    print("Jij hebt geen geldig getal opgegeven!")
except ZeroDivisionError:
    print("Delen door nul is niet toegestaan!")
finally:
    print("Einde van het programma.")
"""

#---------------------------------------------#

"""
try:
    z = int(input("Geef een getal op:"))
    resultaat = 100 / z
    print("100 gedeeld door {} is {}".format(z, resultaat))
except ValueError as ve:
    print("Foutmelding:", ve)
except ZeroDivisionError as zde:    
    print("Foutmelding:", zde)
finally:
    print("Einde van het programma.") 
"""
  