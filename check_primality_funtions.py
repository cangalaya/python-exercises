def get_integer(message):               # ask for a number
    return int(input(message+" "))

def primality_test(number):
    if number%2 != 0:
        return True
    else:
        return False

def run():
    number = get_integer("Digite un número")
    if primality_test(number):
        print("Es primo!")
    else:
        print("No es primo!")


if __name__ == "__main__":
    run()