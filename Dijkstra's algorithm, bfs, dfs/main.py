from collections import deque
infinity = float("inf")
node: str = 'a'
graph = { 'a': ['b', 'd', 'e', 'c', 'z'],
          'b': ['d', 'e'],
          'd': ['e'],
          'e': ['d'],
          'c': ['f', 'g'],
          'f': ['g'],
          'g': ['f'],
          'z': ['w'],
          'w': ['l'],
          'l': [ ] }
def bfs(value:str, hash: dict):
    array = []
    array.append(value)
    queue = deque()
    queue += hash[value]
    duplicates = []
    while queue:
        value = queue.popleft()
        if not value in duplicates:
            duplicates.append(value)
            array.append(value)
            queue += hash[value]
    return array
def print_bfs(func):
    array = func
    for i in array:
        if i == array[-1]:
            print(f'{i}.')
        else:
            print(f'{i}->', end='')
print_bfs(bfs(node, graph))

visited = set()
array = []
def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        array.append(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
    return array

def print_dfs(func):
    array = func(visited, graph, node)
    with open('file.txt', 'w') as file:
        for i in array:
            if i == array[-1]:
                file.write(f'{i}.')
                #print(f'{i}.')
            else:
                file.write(f'{i}->')
                #print(f'{i}->', end='')
print_dfs(dfs)

graph_new = {
    'a': {
        'b':4,
        'c':3
    },
    'b':{
        'd':1
    },
    'c':{
        'b':1,
        'd':5
    },
    'd':{}
}
costs = {
    'b':100,
    'c':100,
    'd': 100
}

parents = {
    'b':'a',
    'c':'a',
    'd':None
}

def dijkstra():
    head = 'a'
    def find_lowest_cost_node():
        lowest_cost = 100000
        lowest_cost_node = None
        for node in graph_new[head]:
            cost = graph_new[head][node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node
    processed = []
    node = find_lowest_cost_node()
    while node not in processed and node != None:
        cost = graph_new[head][node]
        neighbors = graph_new[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node()
    status = True
    value = 'd'
    array_for_print = []
    while status:
        if value != head:
            array_for_print.append(value)
            value = parents[value]
        else:
            array_for_print.append(head)
            status = False
    for i in array_for_print[::-1]:
        if i == 'd':
            print(f'{i}={costs[i]}')
        else:
            print(f'{i}->', end='')

dijkstra()