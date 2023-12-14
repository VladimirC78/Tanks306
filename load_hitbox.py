import random
import Levels_encoded

import objects
import numpy as np

map_number = 2


def calculate_distance(place1, place2):
    # Рассчитывает расстояние между двумя объектами, например, между танком и стеной
    return place1[0] - place2[0], place1[1] - place2[1]


def segment_distance(x, y, x1, y1, x2, y2):  # Рассчитывает расстояние между точкой (х, у) и отрезком (х1, у1, х2, у2)
    v1 = np.array([x - x1, y - y1])
    v2 = np.array([x - x2, y - y2])
    v3 = np.array([x2 - x1, y2 - y1])
    v4 = -v3

    prod1 = np.dot(v1, v3)
    prod2 = np.dot(v2, v4)

    if prod1 * prod2 < 0:
        return min(((x - x1) ** 2 + (y - y1) ** 2) ** 0.5, ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5)
    else:
        if x2 != x1:
            k = (y2 - y1) / (x2 - x1)
            b1 = y1 - k * x1
            return abs(y - k * x - b1) / (k ** 2 + 1) ** 0.5
        else:
            return abs(x - x1)


def bullet_hittest(obj1, obj2):  # Проверка попадания пули в танк, здесь obj1 - пуля, obj2 - танк
    # Координаты каждой из вершин танка
    r_a = [obj2.r[0] + 0.5 * obj2.scale * np.cos(np.pi / 4 - obj2.ang),
           obj2.r[1] - 0.5 * obj2.scale * np.sin(np.pi / 4 - obj2.ang)]
    r_c = [obj2.r[0] - 0.5 * obj2.scale * np.cos(np.pi / 4 - obj2.ang),
           obj2.r[1] + 0.5 * obj2.scale * np.sin(np.pi / 4 - obj2.ang)]
    r_b = [obj2.r[0] + 0.5 * obj2.scale * np.cos(np.pi / 4 + obj2.ang),
           obj2.r[1] + 0.5 * obj2.scale * np.sin(np.pi / 4 + obj2.ang)]
    r_d = [obj2.r[0] - 0.5 * obj2.scale * np.cos(np.pi / 4 + obj2.ang),
           obj2.r[1] - 0.5 * obj2.scale * np.sin(np.pi / 4 + obj2.ang)]

    dist_ab = segment_distance(obj1.r[0], obj1.r[1], r_a[0], r_a[1], r_b[0], r_b[1])
    dist_bc = segment_distance(obj1.r[0], obj1.r[1], r_b[0], r_b[1], r_c[0], r_c[1])
    dist_cd = segment_distance(obj1.r[0], obj1.r[1], r_c[0], r_c[1], r_d[0], r_d[1])
    dist_da = segment_distance(obj1.r[0], obj1.r[1], r_d[0], r_d[1], r_a[0], r_a[1])

    if dist_ab <= obj1.scale or dist_bc <= obj1.scale or dist_cd <= obj1.scale or dist_da <= obj1.scale:
        return True
    else:
        return False



def create_walls(field, block_size):
    # Создает стены
    walls = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                walls.append(Wall(block_size, i * block_size, j * block_size))

    return walls


def create_new_map():
    map_choice = random.choice(range(map_number))
    field = Levels_encoded.fields[map_choice]
    scale_factor = 800 // len(field)
    block_size = scale_factor
    walls = create_walls(field, block_size)
    return walls, field, block_size


class Wall:
    def __init__(self, block_size, x, y):
        self.block_size = block_size
        self.r = list([x, y])
        self.hit_dict = {'u': False, 'd': False, 'r': False, 'l': False}

    def wall_hit(self, obj):
        # Проверка на соударение объекта со стенкой, принимает на вход параметры объекта
        # Возвращает словарь, указывающий с какой стороны произошло столкновение, нужно использовать
        # в move_draw для изменения скорости танка или пули
        self.hit_dict = {'u': False, 'd': False, 'r': False, 'l': False}
        if isinstance(obj, objects.Bullet):
            dist = calculate_distance(obj.r, self.r)
            if dist[0] < 0 and abs(dist[0]) <= obj.scale:
                self.hit_dict['l'] = True
            if dist[0] > 0 and abs(dist[0]) <= self.block_size + obj.scale:
                self.hit_dict['r'] = True
            if dist[1] < 0 and abs(dist[1]) <= obj.scale:
                self.hit_dict['u'] = True
            if dist[1] > 0 and abs(dist[1]) <= self.block_size + obj.scale:
                self.hit_dict['d'] = True
        elif isinstance(obj, objects.Tank):
            # Координаты каждой из вершин танка
            r_a = [obj.r[0] + 0.5 * obj.scale * np.cos(np.pi / 4 - obj.ang),
                   obj.r[1] - 0.5 * obj.scale * np.sin(np.pi / 4 - obj.ang)]
            r_c = [obj.r[0] - 0.5 * obj.scale * np.cos(np.pi / 4 - obj.ang),
                   obj.r[1] + 0.5 * obj.scale * np.sin(np.pi / 4 - obj.ang)]
            r_b = [obj.r[0] + 0.5 * obj.scale * np.cos(np.pi / 4 + obj.ang),
                   obj.r[1] + 0.5 * obj.scale * np.sin(np.pi / 4 + obj.ang)]
            r_d = [obj.r[0] - 0.5 * obj.scale * np.cos(np.pi / 4 + obj.ang),
                   obj.r[1] - 0.5 * obj.scale * np.sin(np.pi / 4 + obj.ang)]
            # Находим максимальные и минимальные координаты
            x_max = max(r_a[0], r_b[0], r_c[0], r_d[0])
            x_min = min(r_a[0], r_b[0], r_c[0], r_d[0])
            y_max = max(r_a[1], r_b[1], r_c[1], r_d[1])
            y_min = min(r_a[1], r_b[1], r_c[1], r_d[1])
            # Проверка, с какой стороны танк сталкивается со стеной
            if x_max >= self.r[0] and y_max <= self.r[1] + self.block_size and y_min >= self.r[1]:
                self.hit_dict['l'] = True
            if x_min <= self.r[0] + self.block_size and y_max <= self.r[1] + self.block_size and y_min >= self.r[1]:
                self.hit_dict['r'] = True
            if y_max >= self.r[1] and x_max <= self.r[0] + self.block_size and x_min >= self.r[0]:
                self.hit_dict['u'] = True
            if y_min >= self.r[1] + self.block_size and x_max <= self.r[0] + self.block_size and x_min >= self.r[0]:
                self.hit_dict['d'] = True

        return self.hit_dict
