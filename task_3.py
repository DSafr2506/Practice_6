import numpy as np


adjacency_matrix = np.array([
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
])


incidence_matrix = np.array([
    [-1, -1, -1,  0,  0,  0,  0,  0],
    [ 1,  0,  0, -1, -1, -1,  0,  0],
    [ 0,  0,  1,  1,  0,  0,  0,  1],
    [ 0,  0,  0,  0,  0,  1,  1, -1],
    [ 0,  1,  0,  0,  1,  0, -1,  0]
])


adjacency_list = {
    0: [1, 4, 2],
    1: [2, 4, 3],
    2: [],
    3: [2],
    4: [3]
}


edge_list = [
    (0, 1),
    (0, 4),
    (0, 2),
    (1, 2),
    (1, 4),
    (1, 3),
    (4, 3),
    (3, 2)
]


ordered_edge_list = sorted(edge_list)


def outgoing_edges(graph, representation, vertex):
    if representation == "матрица смежности":
        result = []

        for j in range(len(graph[vertex])):
            if graph[vertex][j] == 1:
                result.append((vertex, j))

        return result

    elif representation == "матрица инцидентности":
        result = []

        for column in range(graph.shape[1]):
            if graph[vertex][column] == -1:
                for row in range(graph.shape[0]):
                    if graph[row][column] == 1:
                        result.append((vertex, row))

        return result

    elif representation == "список смежности":
        result = []

        for j in graph[vertex]:
            result.append((vertex, j))

        return result

    elif representation == "список дуг":
        result = []

        for i, j in graph:
            if i == vertex:
                result.append((i, j))

        return result

    elif representation == "упорядоченный список дуг":
        result = []

        for i, j in graph:
            if i == vertex:
                result.append((i, j))
            elif i > vertex:
                break

        return result

    else:
        raise ValueError("Неизвестное представление графа")


vertex = 1

print("ЗАДАНИЕ 3")
print()

print("Исходящие дуги из вершины", vertex)
print()

print("Матрица смежности:")
print(outgoing_edges(adjacency_matrix, "матрица смежности", vertex))
print()

print("Матрица инцидентности:")
print(outgoing_edges(incidence_matrix, "матрица инцидентности", vertex))
print()

print("Список смежности:")
print(outgoing_edges(adjacency_list, "список смежности", vertex))
print()

print("Список дуг:")
print(outgoing_edges(edge_list, "список дуг", vertex))
print()

print("Упорядоченный список дуг:")
print(outgoing_edges(ordered_edge_list, "упорядоченный список дуг", vertex))
