from collections import deque
hash = dict()
node: str = '1'
item: str = '9'
hash['1'] = ['2', '3', '4']
hash['2'] = ['5']
hash['3'] = ['6']
hash['4'] = ['3', '6', '7']
hash['5'] = ['6']
hash['6'] = ['9']
hash['7'] = ['6', '8', '9']
hash['8'] = ['9']
hash['9'] = []
def search(value:str, item:str):
    a = value
    count = 0
    queue = deque()
    queue += hash[value]
    duplicates, elements = [], []
    if item == node:
        return node
    while queue:
        value = queue.popleft()
        if not value in duplicates:
            if value == item:
                return f'{search(node, a)}->{value}'
                #return f'{a}->{item}'
            else:
                duplicates.append(value)
                queue += hash[value]
                if item in hash[value]:
                    elements.append(value)
        if len(elements) > 0:
            a = elements[0]
    return None
print(search(node, item))
with open('file.txt', 'w') as file:
    file.write(search(node, item))





