import random
import time

lista = ['kamien', 'papier', 'nozyce']

random.seed(time.time())

a = random.choice(lista)
print(a)
b = input("podaj kamien/papier/nozyce")

if b != 'kamien' and b != 'papier' and b != 'nozyce':
    print("blad, podaj kamien papier lub nozyce")

if a == b:
    print("remis")

if b == 'kamien' :
    if a == 'papier':
        print('przegrales')
    elif a == 'nozyce':
        print('wygrales')

if b == 'papier':
    if a == 'kamien':
        print("wygrales")
    elif a == 'nozyce':
        print('przegrales')

if b == 'nozyce':
    if a == 'papier':
        print('wygrales')
    elif a == 'kamien':
        print('przegrales')









