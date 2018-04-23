import lottofunkcje



def losowanieLotto():
    #Powitanie uzytkownika
    print("Witaj w LOTTO")

    losowe = lottofunkcje.losowanieLiczb()
    #print(losowe)

    liczbyPodane = input("Podaj 6 liczb w zakresie od 1 do 49, liczby oddziel spacjami")

    liczby = lottofunkcje.konwersjaLiczb(liczbyPodane)

    lottofunkcje.weryfikacjaDuplikatow(liczby)
    lottofunkcje.weryfikacjaDlugsciListy(liczby)
    lottofunkcje.weryfikacjaZakresu(liczby)


    wynik = lottofunkcje.wynikiLosowania(liczby, losowe)

    if wynik == 6 or wynik == 0:
        return
    else:
        print("Ilość trafionych liczb:", wynik, "Próbuj dalej")

gram = True

while (gram == True):

    losowanieLotto()

gram = False