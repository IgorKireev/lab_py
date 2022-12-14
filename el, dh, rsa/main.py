import random

def rand_key() -> int:
    K = random.randint(1000, 10000)
    return K
def Y_number_generation(a:int, N:int, K:int) -> int:
    Y = (a ** K) % N
    return Y
def key_generation(func, a:int, N:int, K1:int, K2:int) -> int:
    Y = func(a, N, K1)
    Key = func(Y, N, K2)
    return Key

def diffie_hellman_algorithm():
    print('diffie_hellman_algorithm')
    a = int(input("Введите число a: "))
    N = int(input("Введите число N: "))
    Ka, Kb= rand_key(), rand_key()
    sender_key = key_generation(Y_number_generation, a, N, Kb, Ka)
    recipient_key = key_generation(Y_number_generation, a, N, Ka, Kb)
    print(sender_key, end='\n\n') if sender_key == recipient_key else print('Error')

def input_numbers_elgamal():
    while True:
        try:
            #пример удовлетворяющего условия
            # p = 5879
            # g = 11
            # x = 207
            # k = 1103
            # m = 1111
            p = int(input('Введите простое число p: '))
            g = int(input('Введите натуральное число g: '))
            x = int(input('Введите натуральное число x: '))
            k = int(input('Введите простое число k: '))
            m = int(input('Введите сообщение: '))
            break
        except ValueError:
            print('values error')
            input_numbers_elgamal()
    if not 1 < g < p or g ** (p - 1) % p != 1 or not 1 < x < p or not 1 < k < p - 1 or g ** (k - 1) % k != 1 or m >= p:
        print('values error!')
        input_numbers_elgamal()
    else:
        return [p, g, x, k, m]


def elgamal_algorithm():
    print('elgamal')
    array_input_numbers = input_numbers_elgamal()
    Y = array_input_numbers[1] ** array_input_numbers[2] % array_input_numbers[0]
    a = array_input_numbers[1] ** array_input_numbers[3] % array_input_numbers[0]
    b = array_input_numbers[4] * Y ** array_input_numbers[3] % array_input_numbers[0]
    M = b * a ** (array_input_numbers[0]-1-array_input_numbers[2]) % array_input_numbers[0]
    print(f'Зашифрованные компаненты сообщения: {a}, {b}\n'
          f'Расшифрованное сообщение: {M}', end='\n\n')

def input_numbers_rsa():
    while True:
        try:
            p = int(input('Введите простое число p: ')) #5879
            q = int(input('Введите простое число q: ')) #11
            break
        except ValueError:
            print('values error')
            input_numbers_rsa()
    if 10 ** (p - 1) % p != 1 or 10 ** (q - 1) % q != 1:
        print('values error!')
        input_numbers_rsa()
    else:
        return [p, q]
def rsa_algorithm():
    print('rsa')
    e = 17
    k = 1
    m = int(input('Введите сообщение: ')) #405
    array_input_numbers = input_numbers_rsa()
    n = array_input_numbers[0]*array_input_numbers[1]
    Fn = (array_input_numbers[0]-1)*(array_input_numbers[1]-1)
    while True:
        if (1 + k * Fn) % e == 0:
            d = (1 + k * Fn) // e
            break
        k += 1
    c = m ** e % n
    m = c ** d % n
    print(f'Открытый ключ: {e}\tСекретный ключ: {d}\nЗашифрованное сообщение: {c}\tРасшифрованное сообщение: {m}')

def main():
    diffie_hellman_algorithm()
    elgamal_algorithm()
    rsa_algorithm()

if __name__ == '__main__':
    main()