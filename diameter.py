import sys


# Алгоритм Флойда–Уоршелла нахождения длин кратчайших путей между всеми парами вершин графа
def floyd(g):
    m = len(g)

    for k in range(m):
        for i in range(m):
            for j in range(m):
                if g[i][k] + g[k][j] < g[i][j]:
                    g[i][j] = g[i][k] + g[k][j]

    return g


# Определение диаметра графа как максимальный из всех кратчайших путей между всеми парами вершин графа
def diameter(distances):
    return max(sum(distances, []))


n = int(input("Введите количество вершин: "))
graph = [[0 for j in range(n)] for i in range(n)]

print("Для обозначения отсутствия пути вводите -1")
for i in range(n):
    for j in range(n):
        if i != j:
            graph[i][j] = int(input(f'Введите расстояние между вершинами {i + 1} и {j + 1}: '))
            if graph[i][j] == -1:
                graph[i][j] = sys.maxsize

print(f'Диаметр графа: {diameter(floyd(graph))}')

'''
# Тестовый граф, диаметр = 8
arr = [
    [0, 8, 5],
    [3, 0, sys.maxsize],
    [sys.maxsize, 2, 0]
]

print(f'Диаметр графа: {diameter(floyd(arr))}')
'''