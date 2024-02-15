import numpy as np


class Graf:
    def __init__(self, base, size, input_type):
        if input_type == 0:
            self.size = size
            self.matrix = base
            self.list = [[] for _ in range(self.size)]
            for i in range(self.size):
                for j in range(self.size):
                    if self.matrix[i, j] > 0:
                        self.list[i].append((j, self.matrix[i, j]))
            self.edges = []
            for i in range(self.size):
                for j in range(self.size):
                    if self.matrix[i, j] > 0:
                        self.edges.append((i, j, self.matrix[i, j]))
        elif input_type == 1:
            self.size = size
            self.list = base
            self.matrix = np.zeros((self.size, self.size))
            for i in range(self.size):
                for c in self.list[i]:
                    self.matrix[i, c[0]] = c[1]
            self.edges = []
            for i in range(self.size):
                for j in range(self.size):
                    if self.matrix[i, j] != 0:
                        self.edges.append((i, j, self.matrix[i, j]))
        elif input_type == 2:
            self.size = size
            self.edges = base
            self.matrix = np.zeros((self.size, self.size))
            for c in self.edges:
                matrix[c[0], c[1]] = c[2]
            self.list = [[] for _ in range(self.size)]
            for i in range(self.size):
                for j in range(self.size):
                    if self.matrix[i, j] != 0:
                        self.list[i].append((j, self.matrix[i, j]))

    def dijkstra(self, s, f):
        INF = 10 ** 10
        dist = [INF for _ in range(self.size)]
        dist[s] = 0
        used = [False for _ in range(self.size)]
        min_dist = 0
        min_v = s
        while min_dist < INF:
            i = min_v
            used[i] = True
            for j in range(self.size):
                if dist[i] + self.matrix[i, j] < dist[j] and self.matrix[i, j] != 0:
                    dist[j] = dist[i] + self.matrix[i, j]
            min_dist = INF
            for j in range(self.size):
                if not used[j] and dist[j] < min_dist:
                    min_dist = dist[j]
                    min_v = j
        if dist[f] >= INF:
            return None
        else:
            return dist[f]


matrix = np.array([[0, 1, 1], [4, 0, 1], [2, 1, 0]])
print(Graf(matrix, 3, 0).dijkstra(1, 0))
