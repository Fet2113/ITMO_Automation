# Задача 1
print("Задача 2")
def rand(random_number1 = (15), random_number2 = (125),
    sep = '') -> None:
    if random_number1 > random_number2:
        print(random_number1)
    else:
        print(random_number2)
    print("Задача 2-vers2", sep = '\n')
rand()

import random

def rand(random_number1 = (12), random_number2 = random.randint(0, 125),
         sep = '') ->None:
    if random_number1 > random_number2:
        print(random_number1)
    else:
        print(random_number2)
    print('Завершилась первая задача','Задача 3', sep = '\n')
rand()

import random
def rand(random_number1 = (12), random_number2 = random.randint(0, 1000),
         sep = '') ->None:
    if random_number1 - random_number2 == 135:
        print("yes")
    else:
        print("no")
    print("Задача 4", sep = '\n')
rand()

import random
def rand(random_number1 = random.randint(1,12),
         sep = '') ->None:
    if random_number1 == 1 or random_number1 == 2 or random_number1 == 12:
        print("зима")
    if random_number1 == 3 or random_number1 == 4 or random_number1 == 5:
        print("весна")
    if random_number1 == 6 or random_number1 == 7 or random_number1 == 8:
        print("лето")
    else:
        print("осень")
    print("Задача 5", sep='\n')
rand()

import random
def rand(random_number1 = random.randint(0,20), random_number2 = random.randint(0, 20), random_number3 = random.randint(0, 20),
         sep = '') ->None:
    if random_number1 > 10 and random_number2 > 10 and random_number3 > 10:
        print("yes")
    else:
        print("no")
    print("Задача 6", sep = '\n')
rand()

import random
def rand(random_number1 = random.randint(-20,20), random_number2 = random.randint(-200, 20), random_number3 = random.randint(-200, 20),random_number4 = random.randint(0, 20), random_number5 = random.randint(0, 20),
         sep = '') ->None:
    permit_print = True

    if random_number1 > 0 and permit_print:
        print(random_number1)
    if random_number2 > 0 and permit_print:
        print(random_number2)
    if random_number3 > 0 and permit_print:
        print(random_number3)
    if random_number4 > 0 and permit_print:
        print(random_number4)
    if random_number5 > 0 and permit_print:
        print(random_number5)
    elif not permit_print:
        print()
    print("Задача 7", sep = '\n')
rand()

import random
def rand(year = random.randint(0,999), month = random.randint(1, 12), day = 29,
         sep = '') ->None:

    print(" ", year*month*day, "Done, Готово к проверке", sep = '\n')
rand()