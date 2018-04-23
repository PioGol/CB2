#Konwersja listy string do listy int
def konwersjaLiczb(liczbyPodane):

    liczbyZnaki = liczbyPodane.split(" ")
    liczby = []
    for i in liczbyZnaki:
        liczby.append(int(i))

    return liczby

#weryfikacja czy liczby powtarzaja sie na liście
def weryfikacjaDuplikatow(liczby):

    for i in liczby:
        if liczby.count(i) > 1:
            print('Liczby nie moga sie powtarzac, sprobuj ponownie')
            return quit()
    else:
        return liczby
#weryfikacja dlugosci listy
def weryfikacjaDlugsciListy(liczby):

    if len(liczby) != 6:
        print("Ilość podanych liczb:", len(liczby), "wymagana ilosc to 6, sprobuj ponownie")
        return quit()
    else:
        return liczby

def weryfikacjaZakresu(liczby):

    for i in liczby:
        if i not in range(1, 49):
            print("Podane liczby muszą znajdować się w zakresie od 1 do 49, spróbuj ponownie")
            return quit()
        else:
            return liczby

def losowanieLiczb():

   import random
   import time

   random.seed(time.time())

   losowe = random.sample(range(1, 49), 6)

   return losowe

def wynikiLosowania(liczby, losowe):

    wynik = len(set(liczby) & set(losowe))

    if wynik is 0:
        print("Niestety tym razem nie trafiłeś, spróbuj ponownie")
        return 0
    elif wynik is 6:
        print("gratulacje zostałeś milonerem!")
        return wynik
    else:
        return wynik

def restart():
    import Lotto
    retry = int(input("Wcisnij 1 by zagrac ponownie, Enter by zakonczyc"))

    if retry is 1:
        Lotto.losowanieLotto()
    else:
        quit()



