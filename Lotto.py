import lottofunkcje


def losowanieLotto():
    #Powitanie uzytkownika
    print("Witaj w LOTTO")

    losowe = lottofunkcje.losowanieLiczb()
    print(losowe)

    liczbyPodane = input("Podaj 6 liczb w zakresie od 1 do 49, liczby oddziel spacjami")

    liczby = lottofunkcje.konwersjaLiczb(liczbyPodane)

    lottofunkcje.weryfikacjaDuplikatow(liczby)
    lottofunkcje.weryfikacjaDlugsciListy(liczby)
    lottofunkcje.weryfikacjaZakresu(liczby)


    wynik = lottofunkcje.wynikiLosowania(liczby, losowe)

    print("Ilość trafionych liczb:", wynik, "Próbuj dalej")

losowanieLotto()
lottofunkcje.restart()

