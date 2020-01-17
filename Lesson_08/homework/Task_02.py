"""2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые
необходимо обойти."""

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

"""g = [
    [0, 1, 0, 0, 0],
    [0, 0, 2, 3, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]"""

def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    way = [[start] for _ in range(length)]
    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True
        # тут i определяет номер вершины, vertex - вес ребра связи с ней
        for i, vertex in enumerate(graph[start]):
            # вершина рассматривается если ребро к ней существует и её не посещали
            if vertex != 0 and not is_visited[i]:
                # если стоимость пути в ячейке больше ребра и базовой, то
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    # Придумать как добавить наследование от предыдущих вершин
                    heritage = way[start]
                    for element in heritage:
                        if element not in way[i]:
                            way[i].append(element)
                    if start not in way[i]:
                        way[i].append(start)
                    if i not in way[i]:
                        way[i].append(i)

        # Этот участок вычисляет самый дешёвый путь
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
        print(way)
    return cost


s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))
