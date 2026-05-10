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


def to_edge_list(graph, representation):
    if representation == "список дуг":
        return list(graph)

    elif representation == "список смежности":
        result = []

        for i in graph:
            for j in graph[i]:
                result.append((i, j))

        return result

    elif representation == "матрица смежности":
        result = []

        for i in range(graph.shape[0]):
            for j in range(graph.shape[1]):
                if graph[i][j] == 1:
                    result.append((i, j))

        return result

    elif representation == "матрица инцидентности":
        result = []

        for column in range(graph.shape[1]):
            start = None
            end = None

            for row in range(graph.shape[0]):
                if graph[row][column] == -1:
                    start = row
                elif graph[row][column] == 1:
                    end = row

            result.append((start, end))

        return result

    else:
        raise ValueError("Неизвестное представление графа")


def from_edge_list(edges, representation, vertex_count):
    if representation == "список дуг":
        return list(edges)

    elif representation == "список смежности":
        result = {}

        for vertex in range(vertex_count):
            result[vertex] = []

        for i, j in edges:
            result[i].append(j)

        return result

    elif representation == "матрица смежности":
        result = np.zeros((vertex_count, vertex_count), dtype=int)

        for i, j in edges:
            result[i][j] = 1

        return result

    elif representation == "матрица инцидентности":
        result = np.zeros((vertex_count, len(edges)), dtype=int)

        for column, edge in enumerate(edges):
            i = edge[0]
            j = edge[1]

            result[i][column] = -1
            result[j][column] = 1

        return result

    else:
        raise ValueError("Неизвестное требуемое представление графа")


def convert_graph(graph, from_representation, to_representation):
    if from_representation == "матрица смежности":
        vertex_count = graph.shape[0]

    elif from_representation == "матрица инцидентности":
        vertex_count = graph.shape[0]

    elif from_representation == "список смежности":
        vertex_count = len(graph)

    elif from_representation == "список дуг":
        vertex_count = max(max(i, j) for i, j in graph) + 1

    else:
        raise ValueError("Неизвестное начальное представление графа")

    edges = to_edge_list(graph, from_representation)

    return from_edge_list(edges, to_representation, vertex_count)


print("ЗАДАНИЕ 4")
print()

print("Матрица смежности -> список дуг:")
print(convert_graph(adjacency_matrix, "матрица смежности", "список дуг"))
print()

print("Список дуг -> матрица смежности:")
print(convert_graph(edge_list, "список дуг", "матрица смежности"))
print()

print("Список смежности -> матрица инцидентности:")
print(convert_graph(adjacency_list, "список смежности", "матрица инцидентности"))
print()

print("Матрица инцидентности -> список смежности:")
print(convert_graph(incidence_matrix, "матрица инцидентности", "список смежности"))
