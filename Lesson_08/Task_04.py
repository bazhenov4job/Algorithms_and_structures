# Поиск кратчайшего пути в ширину

from collections import deque

g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]


def bfs(graph, start, finish):
    parrent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:

        current = deq.pop()

        if current == finish:
            # return parrent
            break

        for i, vertex in enumerate(graph[current]):
            if vertex == 1 and not is_visited[i]:

                is_visited[i] = True
                parrent[i] = current
                deq.appendleft(i)

    else:
        return f'Из вершины {start} нельзя дойти до {finish}'

    cost = 0
    way = deque([finish])
    i = finish
    while parrent[i] != start:
        cost += 1
        way.appendleft(parrent[i])
        i = parrent[i]

    cost += 1
    way.appendleft(start)
    print(parrent)
    return way


s = int(input('Введите начальную вершину: '))
f = int(input('Введите конечную вершину: '))
print(bfs(g, s, f))
