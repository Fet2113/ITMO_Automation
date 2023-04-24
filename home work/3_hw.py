# Задача 1
print("Задача 2")
def rand(random_number1 = 15, random_number2 = 125) -> None:
    if random_number1 > random_number2:
        print(random_number1)
    else:
        print(random_number2)
    print("Задача 2-vers2", sep='\n')
rand()

import random

def rand1(random_number1 = (12), random_number2 = random.randint(0, 125)) ->None:
    if random_number1 > random_number2:
        print(random_number1)
    else:
        print(random_number2)
    print('Завершилась задача 2','Задача 3', sep='\n')
rand1()

def rand2(random_number1 = (12), random_number2 = random.randint(0, 1000)) ->None:
    if random_number1 - random_number2 == 135 or random_number2 - random_number1 == 135:
        print("yes")
    else:
        print("no")
    print("Задача 4", sep='\n')
rand2()

def rand3(random_number1 = random.randint(1,12)) ->None:
    if random_number1 == 1 or random_number1 == 2 or random_number1 == 12:
        print("зима")
    if random_number1 == 3 or random_number1 == 4 or random_number1 == 5:
        print("весна")
    if random_number1 == 6 or random_number1 == 7 or random_number1 == 8:
        print("лето")
    else:
        print("осень")
    print("Задача 5", sep='\n')
rand3()

def rand4(random_number1 = random.randint(0,20), random_number2 = random.randint(0, 20), random_number3 = random.randint(0, 20)) ->None:
    if random_number1 > 10 and random_number2 > 10 and random_number3 > 10:
        print("yes")
    else:
        print("no")
    print("Задача 6", sep='\n')
rand4()

list1 = [10, -21, 4, -45, 66, -93, 1];
pos_count, neg_count = 0, 0

for num in list1:
    if num >= 0:
        pos_count += 1
    else:
        neg_count += 1
print(" ", pos_count)
print("Задача 7", sep='\n')

def rand6(year = random.randint(0,999), month = random.randint(1, 12), day = 29) ->None:

    print(" ", year*month*day, "Done, Готово к проверке", sep='\n')
rand6()