"""
exercise from: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
topic: modules, input and output, bulces
"""

import random, time, os

MENU = """
-------------- ADIVINA EL NÚMERO!! -----------------
    - Adivina el número que eligió la máquina
    - Para salir del juego escriba: exit

    Type a number between 1 and 9: """

def pruebas():
    numero = int(input("número: "))
    if type(numero) != int:
        print(True)
    else:
        print(False)

def convert_str_to_int(user_number):
    while type(user_number) != int:
        try:
            user_number = int(user_number)
        except ValueError as te:
            print("\n    No se admiten letras.", te, "Intente de nuevo")
            user_number = input("    Digite un número del 1 al 9: ")
    return user_number


def run():
    while True:
        os.system("clear")
        random_number = random.randint(1,9)
        user_number = input(MENU)
        if user_number == 'exit':
            break
        user_number = convert_str_to_int(user_number)
        
        while random_number != user_number:
            if random_number > user_number:
                print("\n    El número es más alto, intentelo otra vez.")
                time.sleep(2)
            elif random_number < user_number:
                print("\n    El número es más bájo, intentelo otra vez.")
                time.sleep(2)
            else:
                break           # if random_number equals user_number, get out from the while
                
            
            user_number = input('    Digite un número del 1 al 9: ')
            user_number = convert_str_to_int(user_number)

        print('\n    Ganaste!! El número es:', random_number)
        time.sleep(2)

    

if __name__ == '__main__':
    run()