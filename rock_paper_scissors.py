# Python practice: Piedra, papel y tijera.
# from: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

import random
import os
import time

MENU = """ESCOJE UNA OPCIÓN:
    [1] = piedra
    [2] = papel
    [3] = tijera
    
Digita una número -> """
options = ['piedra', 'papel', 'tijera']

def choice_option():
    option = options[random.randint(0,2)]
    return option

def jugar(option_machine, option_human):

    if option_human == 'piedra':
        if option_machine == 'tijera':
            resultado = 'gano'
        elif option_machine == 'papel':
            resultado = 'perdio'
        else:
            resultado = 'empate'

    elif option_human == 'papel':
        if option_machine == 'tijera':
            resultado = 'perdio'
        elif option_machine == 'piedra':
            resultado = 'gano'
        else:
            resultado = 'empate'

    elif option_human == 'tijera':
        if option_machine == 'papel':
            resultado = 'gano'
        elif option_machine == 'piedra':
            resultado = 'perdio'
        else:
            resultado = 'empate'
    
    else:
        resultado = 'invalido'

    return resultado
    

def run():

    while True:
        os.system('clear')
        option_machine = choice_option()
        try:
            option_human = options[int(input(MENU))-1]
        except ValueError:
            print('No se permiten letras... intente de nuevo')
            break
        except IndexError:
            print('Número no valido, intente de nuevo')
            break

        print(f'*MAQUINA = {option_machine} \n*TU = {option_human}')
        resultado = jugar(option_machine, option_human)

        if resultado == 'gano':
            print('GANASTE!')
            break
        elif resultado == 'perdio':
            print('PERDISTE')
            break
        elif resultado == 'empate':
            print('¡¡¡EMPATE!!!')
            time.sleep(2.2)
            continue
        else:
            print('La opción digitada no es valida ...')
            break
    


if __name__ == '__main__':
    run()
