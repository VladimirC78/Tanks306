import Levels_encoded


def calculate_distance(place1, place2):
    # Рассчитывает расстояние между двумя объектами, например, между танком и стеной
    return place1[0] - place2[0], place1[1] - place2[1]


def create_walls(field, block_size):
    # Создает стены
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 1:
                walls.append(Wall(block_size, i * block_size, j * block_size))


class Wall:
    def __init__(self, block_size, x, y):
        self.block_size = block_size
        self.r = list([x, y])
        self.hit_dict = {'u': False, 'd': False, 'r': False, 'l': False}

    def wall_hit(self, obj):
        # Проверка на соударение объекта со стенкой, принимает на вход параметры объекта
        # Возвращает словарь, указывающий с какой стороны произошло столкновение, нужно использовать
        # в move_draw для изменения скорости танка или пули
        dist = calculate_distance(obj.r, self.r)
        if dist[0] < 0 and abs(dist[0]) <= self.block_size + obj.scale:
            self.hit_dict['l'] = True
        if dist[0] > 0 and abs(dist[0]) <= self.block_size + obj.scale:
            self.hit_dict['r'] = True
        if dist[1] < 0 and abs(dist[1]) <= self.block_size + obj.scale:
            self.hit_dict['u'] = True
        if dist[1] > 0 and abs(dist[1]) <= self.block_size + obj.scale:
            self.hit_dict['d'] = True

        return self.hit_dict


field = Levels_encoded.level1
scale_factor = 800 // len(field)  # screen_width
block_size = 20 * scale_factor
walls = []

create_walls(field, block_size)
