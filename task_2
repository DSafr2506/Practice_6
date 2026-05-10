import numpy as np


vertices = [0, 1, 2, 3, 4]

edges = [
    (0, 1),
    (0, 4),
    (0, 2),
    (1, 2),
    (1, 4),
    (1, 3),
    (4, 3),
    (3, 2)
]


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


print("ЗАДАНИЕ 2")
print()

print("Вершины:")
print(vertices)
print()

print("Дуги:")
print(edges)
print()

print("а) Матрица смежности:")
print(adjacency_matrix)
print()

print("б) Матрица инцидентности:")
print(incidence_matrix)
print()

print("в) Список смежности:")
print(adjacency_list)
print()

print("г) Список дуг:")
print(edge_list)
