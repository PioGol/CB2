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
            return
    else:
        return liczby


