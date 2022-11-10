UPPalp = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
alp = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
en_alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
en_UPPalp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def menu():
    while True:
        try:
            value = int(input("Введите число: 1 - шифрование текста, 2 - расшифрование текста, 3 - закончить программу: "))
            break
        except ValueError:
            print("Значение некорректно")
    if not value == 1 and not value == 2 and not value == 3:
        print("Значение некорректно")
        return menu()
    else:
        return value
def what_step():
    while True:
        try:
            step = int(input("Введите шаг шифра: "))
            break
        except ValueError:
            print("Значение некорректно")
    if step < 0:
        print("Значение некорректно. Программа не предусмотрена для ввода отрицательного шага.")
        return what_step()
    else:
        return step

def cipher(alphabet: list, letter: str, step: int, solution: bool) -> int:
    for j in alphabet:
        if not letter != j:
            return (alphabet.index(j) + step) % len(alphabet) if solution else (alphabet.index(j) - step + len(alphabet)) % len(alphabet)

def add_later(word: list, letter: str, step: int, solution: bool, cipher) -> None:
    def alphabet() -> list|None:
        if letter in alp:
            return alp
        elif letter in UPPalp:
            return UPPalp
        elif letter in en_alp:
            return en_alp
        elif letter in en_UPPalp:
            return en_UPPalp
        return None
    alphabet = alphabet()
    if alphabet is None:
        word.append(letter)
    else:
        word.append(alphabet[cipher(alphabet, letter=letter, step=step, solution=solution)])

def main():
    while True:
        result = menu()
        if not result - 3:
            exit()
        step = what_step()
        word = input("Введите текст: ")
        new_word = []
        for letter in word:
            if not result - 1:
                solution = True
            else:
                solution = False
            add_later(new_word, letter, step, solution, cipher)
        print(''.join(new_word))

if __name__ == '__main__':
    main()








