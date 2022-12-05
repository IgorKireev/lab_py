from collections import deque
node: str = 'a'
unweighted_graph = { 'a': ['b', 'd', 'e', 'c', 'z'],
          'b': ['d', 'e'],
          'd': ['e'],
          'e': ['d'],
          'c': ['f', 'g'],
          'f': ['g'],
          'g': ['f'],
          'z': ['w'],
          'w': ['l'],
          'l': [ ] }

weighted_graph = {
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
def bfs(value:str, graph: dict):
    array = []
    array.append(value)
    queue = deque()
    queue += graph[value]
    duplicates = []
    while queue:
        value = queue.popleft()
        if not value in duplicates:
            duplicates.append(value)
            array.append(value)
            queue += graph[value]
    return array
def print_bfs(func):
    array = func
    for i in array:
        if i == array[-1]:
            print(f'{i}.')
        else:
            print(f'{i}->', end='')
print_bfs(bfs(node, unweighted_graph))

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
    array = func(visited, unweighted_graph, node)
    with open('file.txt', 'w') as file:
        for i in array:
            if i == array[-1]:
                file.write(f'{i}.')
            else:
                file.write(f'{i}->')
print_dfs(dfs)

def dijkstra():
    head = 'a'
    def find_lowest_cost_node():
        lowest_cost = 100000
        lowest_cost_node = None
        for node in weighted_graph[head]:
            cost = weighted_graph[head][node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node
    processed = []
    node = find_lowest_cost_node()
    while node not in processed and node != None:
        cost = weighted_graph[head][node]
        neighbors = weighted_graph[node]
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