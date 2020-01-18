"""3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
 по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин."""

"""
Отрабатывал алгоритм на вручную введённом графе g,
при желании можете сами раскомментить строки в конце и 
скормить сгенерированный граф.
Вводите вершины через запятую, без пробелов. 
"""



def generate_graph(veterex_number):
    g = list()
    for i in range(vertex_number):
        vertex_row = input(f"Вершина {i} обладает связями: ").split(',')
        for j in range(len(vertex_row)):
            vertex_row[j] = int(vertex_row[j])
        g.append(vertex_row)

    return g

g = [
    [4],
    [2, 5],
    [5],
    [1, 2],
    [3],
    []
]


def begin_dfs(graph, start):
    length = len(graph)
    is_visited = [False for _ in range(length)]
    is_visited[start] = True
    ways = [[start] for _ in range(length)]

    def dfs(graph, start):
        count_visited = 0
        for vertex in graph[start]:
            if not is_visited[vertex]:
                heritage = ways[start]

                for parent in heritage:
                    if parent not in ways[vertex]:
                        ways[vertex].append(parent)
                if start not in ways[vertex]:
                    ways[vertex].append(start)
                if vertex not in ways[vertex]:
                    ways[vertex].append(vertex)
                is_visited[vertex] = True
                dfs(graph, vertex)
            else:
                count_visited += 1
        if count_visited == len(graph[start]):
            return ways[start][-1]


    # parent = [-1 for _ in range(length)]
    dfs(graph, start)
    return ways

# vertex_number = int(input("Введите число вершин графа: "))
# g = generate_graph(vertex_number)
# print(*g, sep='\n')
ways = begin_dfs(g, 0)
# print(*begin_dfs(graph=g, start=0), sep='\n')
print(ways)
