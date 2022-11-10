def get_table(template: str) -> dict:
    hash = dict()
    for i in range(len(template)):
        if template[i] == template[-1]:
            hash[template[i]] = len(template)
        else:
            hash[template[i]] = len(template) - (i + 1)
    return hash

def main():
    text = input("Введите строку: ")
    template = input("Введите подстроку: ")
    table = get_table(template)
    count = 0
    i = 1
    index = 0
    while True:
        if count == len(template):
            print(len(template) - i + index + 1)
            with open("file.txt", 'w') as file:
                file.write(f'{len(template) - i + index + 1}')
            break
        if text[len(template) - i + index] == template[len(template) - i]:
            count += 1
        else:
            i = 0
            if not text[len(template) - 1 + index] in table:
                index += len(template)
            else:
                index += table[text[len(template) - 1 + index]]
        i += 1

if __name__ == '__main__':
    main()