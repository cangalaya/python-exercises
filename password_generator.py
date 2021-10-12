import random
import os

MENU = """  ++  P A S S W O R D  G E N E R A T O R  ++
    
    Choose a security level:
        [1] - Low
        [2] - Medium
        [3] - High
        
        Type a number [1-3] -> """

def num_input(message):
    try:
        number = int(input(message))
        return number
    except ValueError as ve:
        print("Type a number, try again.")

# pass generator, number can be 1 for low and 3 for high security
def pass_gen(number):

    def random_dic():
        dic_words = {   # dic that return a random number, letter or simbol
            'number': str(random.randint(0,9)),
            'letter': random.choice('qwertyuiopasdfghjklñzxcvbnm'),
            'simbol': random.choice("!#$%&/()=?¡[];: ")
        }
        return dic_words

    if number == 1:
        password_list = [random_dic()[random.choice(['number', 'letter'])] for i in range(5)]    # password of 5 digits of numbers and letters
    elif number == 2:
        password_list = [random_dic()[random.choice(['number', 'letter'])] for i in range(10)]   # password of 10 digits of numbers and letters
    elif number == 3:
        password_list = [random_dic()[random.choice(['number', 'letter', 'simbol'])] for i in range(15)]       # password of 10 digits of numbers, letters and simbols
    else:
        raise ValueError("Invalid number, choose a number from 1 to 3.")

    #print(password_list)
    password = "".join(password_list)
    return password

def run():
    os.system("clear")
    security_level = num_input(MENU)
    password = pass_gen(security_level)
    print("        The password generated is:", password)

if __name__ == "__main__":
    run()