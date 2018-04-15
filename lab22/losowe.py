import random
import time


random.seed(time.time())
a = random.randrange(3685)

print(a)

imiona = ["Marcin", "Lukasz", "Anna", "Kasia", "Piotr", "Stefan", "Maria", "Olek", "Marian", "Joanna"]

print(random.choice(imiona))

random.shuffle(imiona)
print(imiona)
