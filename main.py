import numpy as np


import pygame


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
                self.matrix[c[0], c[1]] = c[2]
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
            else:
                self.image = pygame.image.load('venv\\sprites\\get_edge_list_selected.png')
        else:
            self.image = pygame.image.load('venv\\sprites\\get_edge_list_default.png')


class ConnectVerticesButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('venv\\sprites\\connect_vertices_default.png')
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 190

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if held:
                self.image = pygame.image.load('venv\\sprites\\connect_vertices_pressed.png')
            else:
                self.image = pygame.image.load('venv\\sprites\\connect_vertices_selected.png')
        else:
            self.image = pygame.image.load('venv\\sprites\\connect_vertices_default.png')


class Vertex(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('venv\\sprites\\vertex.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.grabbed = False

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and clicked:
            self.grabbed = True
        elif self.grabbed and (not held):
            self.grabbed = False
        if self.grabbed:
            self.rect.x = pygame.mouse.get_pos()[0] - 20
            self.rect.y = pygame.mouse.get_pos()[1] - 20


pygame.init()
all_sprites = pygame.sprite.Group()


held = False


tools = pygame.Surface((200, 920))
get_adjacency_matrix_button = GetAdjacencyMatrixButton()
all_sprites.add(get_adjacency_matrix_button)
get_adjacency_list_button = GetAdjacencyListButton()
all_sprites.add(get_adjacency_list_button)
get_edge_list_button = GetEdgeListButton()
all_sprites.add(get_edge_list_button)
connect_vertices_button = ConnectVerticesButton()
all_sprites.add(connect_vertices_button)
v1 = Vertex(250, 250)
all_sprites.add(v1)
v2 = Vertex(300, 300)
all_sprites.add(v2)
v3 = Vertex(350, 350)
all_sprites.add(v3)
v4 = Vertex(400, 400)
all_sprites.add(v4)


screen = pygame.display.set_mode((920, 650))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            held = True
            clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held = False
        else:
            clicked = False
    screen.fill((255, 255, 255))
    tools.fill((170, 190, 200))
    screen.blit(tools, (0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(60)
