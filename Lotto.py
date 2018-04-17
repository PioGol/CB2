import random
import time
import lottofunkcje

#Powitanie uzytkownika
print("Witaj w LOTTO")

liczbyPodane = input("Podaj 6 liczb w zakresie od 1 do 49, liczby oddziel spacjami")


print("liczby ktore podales to:")
liczby = lottofunkcje.konwersjaLiczb(liczbyPodane)

print(liczby)

liczbyzweryfikowane = lottofunkcje.weryfikacjaDuplikatow(liczby)

print(liczbyzweryfikowane)

