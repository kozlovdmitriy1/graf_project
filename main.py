import numpy as np


import pygame


class Graph:
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
                self.matrix[c[0], c[1]] = c[2]
            self.list = [[] for _ in range(self.size)]
            for i in range(self.size):
                for j in range(self.size):
                    if self.matrix[i, j] != 0:
                        self.list[i].append((j, self.matrix[i, j]))

    def add_vertex(self):
        self.size += 1
        self.matrix = np.hstack([np.vstack([self.matrix, np.zeros((1, self.size - 1))]), np.zeros((self.size, 1))])
        self.list.append([])

    def add_edge(self, ver1, ver2, length):
        self.edges.append((ver1, ver2, length))
        self.matrix[ver1, ver2] = length
        self.list[ver1].append((ver2, length))
        self.matrix[ver2, ver1] = length
        self.list[ver2].append((ver1, length))

    def remove_edge(self, ver1, ver2):
        self.matrix[ver1, ver2] = 0
        self.matrix[ver2, ver1] = 0
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

    def remove_vertex(self, ver):
        self.size -= 1
        self.matrix = np.delete(np.delete(self.matrix, ver, 0), ver, 1)
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


class GetAdjacencyMatrixButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('venv\\sprites\\get_adjacency_matrix_default.png')
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 20

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if held:
                self.image = pygame.image.load('venv\\sprites\\get_adjacency_matrix_pressed.png')
                if clicked:
                    print(graph.matrix)
            else:
                self.image = pygame.image.load('venv\\sprites\\get_adjacency_matrix_selected.png')
        else:
            self.image = pygame.image.load('venv\\sprites\\get_adjacency_matrix_default.png')


class GetAdjacencyListButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('venv\\sprites\\get_adjacency_list_default.png')
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 70

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if held:
                self.image = pygame.image.load('venv\\sprites\\get_adjacency_list_pressed.png')
                if clicked:
                    print(graph.list)
            else:
                self.image = pygame.image.load('venv\\sprites\\get_adjacency_list_selected.png')
        else:
            self.image = pygame.image.load('venv\\sprites\\get_adjacency_list_default.png')


class GetEdgeListButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('venv\\sprites\\get_edge_list_default.png')
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 120

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if held:
                self.image = pygame.image.load('venv\\sprites\\get_edge_list_pressed.png')
                if clicked:
                    print(graph.edges)
            else:
                self.image = pygame.image.load('venv\\sprites\\get_edge_list_selected.png')
        else:
            self.image = pygame.image.load('venv\\sprites\\get_edge_list_default.png')


connect = False


class ConnectVerticesButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('venv\\sprites\\connect_vertices_default.png')
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 190

    def update(self):
        global connect
        if self.rect.collidepoint(pygame.mouse.get_pos()) or connect:
            if held or connect:
                self.image = pygame.image.load('venv\\sprites\\connect_vertices_pressed.png')
                if self.rect.collidepoint(pygame.mouse.get_pos()) and clicked:
                    if not connect:
                        connect = True
                    else:
                        connect = False
            else:
                self.image = pygame.image.load('venv\\sprites\\connect_vertices_selected.png')
        else:
            self.image = pygame.image.load('venv\\sprites\\connect_vertices_default.png')


class AddVertexButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('venv\\sprites\\add_vertex_default.png')
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 240

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if held:
                self.image = pygame.image.load('venv\\sprites\\add_vertex_pressed.png')
                if clicked:
                    global all_sprites
                    all_sprites.add(Vertex(220, 20))
            else:
                self.image = pygame.image.load('venv\\sprites\\add_vertex_selected.png')
        else:
            self.image = pygame.image.load('venv\\sprites\\add_vertex_default.png')


delete = False


class DeleteVertexButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('venv\\sprites\\delete_vertex_default.png')
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 290

    def update(self):
        global delete
        if self.rect.collidepoint(pygame.mouse.get_pos()) or delete:
            if held or delete:
                self.image = pygame.image.load('venv\\sprites\\delete_vertex_pressed.png')
                if self.rect.collidepoint(pygame.mouse.get_pos()) and clicked:
                    if not delete:
                        delete = True
                    else:
                        delete = False
            else:
                self.image = pygame.image.load('venv\\sprites\\delete_vertex_selected.png')
        else:
            self.image = pygame.image.load('venv\\sprites\\delete_vertex_default.png')


vertices = []
some_vertex_grabbed = False
new_edge_start = -1


class Vertex(pygame.sprite.Sprite):
    def __init__(self, x, y):
        global vertices, graph
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('venv\\sprites\\vertex.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.grabbed = False
        self.number = len(vertices)
        self.text = font.render(str(self.number + 1), True, (0, 0, 0))
        vertices.append(self)
        graph.add_vertex()

    def update(self):
        global some_vertex_grabbed, new_edge_start, graph, vertices, connect, delete
        if self.rect.collidepoint(pygame.mouse.get_pos()) and clicked and not some_vertex_grabbed:
            self.grabbed = True
            some_vertex_grabbed = True
        elif self.grabbed and (not held):
            self.grabbed = False
            some_vertex_grabbed = False
        if self.grabbed:
            if 220 <= pygame.mouse.get_pos()[0] <= 900:
                self.rect.x = pygame.mouse.get_pos()[0] - 20
            if 20 <= pygame.mouse.get_pos()[1] <= 630:
                self.rect.y = pygame.mouse.get_pos()[1] - 20
        if self.rect.collidepoint(pygame.mouse.get_pos()) and clicked and connect:
            self.image = pygame.image.load('venv\\sprites\\vertex_selected.png')
            self.image.set_colorkey((255, 255, 255))
            if new_edge_start == -1:
                new_edge_start = self.number
            else:
                if graph.matrix[new_edge_start, self.number] == 0:
                    graph.add_edge(new_edge_start, self.number, 1)
                else:
                    graph.remove_edge(new_edge_start, self.number)
                self.image = pygame.image.load('venv\\sprites\\vertex.png')
                self.image.set_colorkey((255, 255, 255))
                vertices[new_edge_start].image = pygame.image.load('venv\\sprites\\vertex.png')
                vertices[new_edge_start].image.set_colorkey((255, 255, 255))
                new_edge_start = -1
                connect = False
        if self.rect.collidepoint(pygame.mouse.get_pos()) and clicked and delete:
            self.grabbed = False
            some_vertex_grabbed = False
            delete = False
            graph.remove_vertex(self.number)
            del vertices[self.number]
            for i in range(self.number, len(vertices)):
                vertices[i].number -= 1
                vertices[i].text = font.render(str(vertices[i].number + 1), True, (0, 0, 0))
            self.kill()
        if self.number < 10:
            screen.blit(self.text, (self.rect.x + 15, self.rect.y + 14))
        elif self.number < 100:
            screen.blit(self.text, (self.rect.x + 10, self.rect.y + 14))


pygame.init()
font = pygame.font.SysFont(None, 24)
all_sprites = pygame.sprite.Group()


held = False
graph = Graph([], 0, 2)


tools = pygame.Surface((200, 920))
get_adjacency_matrix_button = GetAdjacencyMatrixButton()
all_sprites.add(get_adjacency_matrix_button)
get_adjacency_list_button = GetAdjacencyListButton()
all_sprites.add(get_adjacency_list_button)
get_edge_list_button = GetEdgeListButton()
all_sprites.add(get_edge_list_button)
connect_vertices_button = ConnectVerticesButton()
all_sprites.add(connect_vertices_button)
add_vertex_button = AddVertexButton()
all_sprites.add(add_vertex_button)
delete_vertex_button = DeleteVertexButton()
all_sprites.add(delete_vertex_button)


screen = pygame.display.set_mode((920, 650))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
while running:
    clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            held = True
            clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held = False
    screen.fill((255, 255, 255))
    tools.fill((170, 190, 200))
    screen.blit(tools, (0, 0))
    for e in graph.edges:
        pygame.draw.line(screen, (60, 120, 255), [vertices[e[0]].rect.x + 20, vertices[e[0]].rect.y + 20],
                         [vertices[e[1]].rect.x + 20, vertices[e[1]].rect.y + 20], 5)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(60)
