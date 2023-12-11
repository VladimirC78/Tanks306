import Levels_encoded
import main
import objects
import numpy as np


def calculate_distance(place1, place2):
    # Рассчитывает расстояние между двумя объектами, например, между танком и стеной
    return place1[0] - place2[0], place1[1] - place2[1]


def create_walls(field, block_size):
    # Создает стены
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 1:
                walls.append(Wall(block_size, i * block_size, j * block_size))

    return walls


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
            r_a = [obj.r[0] + 0.5 * obj.scale * np.cos(np.pi/4 - obj.ang),
                   obj.r[1] - 0.5 * obj.scale * np.sin(np.pi/4 - obj.ang)]
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


field = Levels_encoded.field
scale_factor = main.screen_height // len(field)  # screen_height
block_size = scale_factor
walls = []

create_walls(field, block_size)
