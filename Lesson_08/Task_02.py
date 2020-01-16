"""списки смежности"""
from collections import namedtuple

# graph - обычный неориентированный граф. Список смежности занимает меньше места в памяти

graph = []

graph.append([1, 2])
graph.append(([0, 2, 3]))
graph.append([0, 1])
graph.append([1])

print(graph)

# Представление в виде словаря позволяет более легко получить доступ к графу
graph_2 = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1},
    3: {1}
}

print(graph_2)

# Что делать, если граф взвешенный
# В список смежности добавляются пары значений
# 1-е значение - номер вершины, 2-е - вес ребра

Vertex = namedtuple('Vertex', 'vertex, edge')
graph_3 = list()
graph_3.append([Vertex(1, 2), Vertex(2, 3)])
graph_3.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph_3.append([Vertex(0, 3), Vertex(1, 2)])
graph_3.append([Vertex(1, 1)])

print(*graph_3, sep='\n')

# Пример хранения графов в виде классов. Очень удобно, если хотим добавить гибкости структуре


class Graph:
    def __init__(self, vertex, edge, spam):
        self.vertex = vertex
        self.edge = edge
        self.spam = spam

