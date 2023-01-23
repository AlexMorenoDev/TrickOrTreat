""" 
 * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco o Trato" y
 * un listado (array) de personas con las siguientes propiedades:
 * - Nombre de la niña o niño
 * - Edad
 * - Altura en centímetros
 *
 * Si las personas han pedido truco, el programa retornará sustos (aleatorios)
 * siguiendo estos criterios:
 * - Un susto por cada 2 letras del nombre por persona
 * - Dos sustos por cada edad que sea un número par
 * - Tres sustos por cada 100 cm de altura entre todas las personas
 * - Sustos: 🎃 👻 💀 🕷 🕸 🦇
 *
 * Si las personas han pedido trato, el programa retornará dulces (aleatorios)
 * siguiendo estos criterios:
 * - Un dulce por cada letra de nombre
 * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
 * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
 * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
"""
import random

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

def calculate_frights(person_list):
    num_frights = 0
    total_height = 0
    for person in person_list:
        num_frights += int(len(person.name) / 2)
        if (person.age % 2) == 0:
            num_frights += 2
        total_height += person.height

    num_frights += int(total_height / 100) * 3

    return num_frights

def calculate_candies(person_list):
    num_candies = 0

    for person in person_list:
        num_candies += len(person.name)
        if person.age >= 10:
            num_candies += 3
        else:
            num_candies += int(person.age / 3)

        if person.height >= 150:
            num_candies += 6
        else:
            num_candies += int(person.height / 50) * 2

    return num_candies

def get_frights_or_candies_str(num, lst):
    return_str = ""
    for _ in range(num):
        return_str += random.choice(lst)

    return return_str

def trick_or_treat(option, person_list):
    frights = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]
    candies = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]

    low_option = option.lower()
    if low_option == "trick":
        num_frigths = calculate_frights(person_list)
        return get_frights_or_candies_str(num_frigths, frights)
    elif low_option == "treat":    
        num_candies = calculate_candies(person_list)
        return get_frights_or_candies_str(num_candies, candies)
    
    return "ERROR: Option is not TRICK or TREAT"

def main():
    print(trick_or_treat("TRICK", [
            Person("Brais", 35, 177),
            Person("Sara", 9, 122),
            Person("Pedro", 5, 80),
            Person("Roswell", 3, 54)
        ]
    ))

    print(trick_or_treat("TREAT", [
            Person("Brais", 35, 177),
            Person("Sara", 9, 122),
            Person("Pedro", 5, 80),
            Person("Roswell", 3, 54)
        ]
    ))

if __name__ == "__main__":
    main()