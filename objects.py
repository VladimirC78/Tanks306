class Tank:
    def __init__(self, x, y, v, omega, scale, type):
        self.type = type
        self.r = list([x, y])  # Координаты танка по осям х и у
        self.scale = scale  # Характерный размер танка
        self.v = v  # Модуль скорости
        self.ang = 0  # изначально танк направлен вертикально вверх, угол отсчитывается против часовой стрелки
        self.omega = omega  # потом подберем
        self.charges = 5
        self.tank_hit_walls = {'u': False, 'd': False, 'r': False, 'l': False}
        self.live = 1  # жизнь танка

    def tank_check_hit(self, walls):
        l, r, u, d = False, False, False, False
        for wall in walls:
            if wall.wall_hit(self)["l"]:
                l = True
            if wall.wall_hit(self)["r"]:
                r = True
            if wall.wall_hit(self)["u"]:
                u = True
            if wall.wall_hit(self)["d"]:
                d = True
        self.tank_hit_walls = {'u': u, 'd': d, 'r': r, 'l': l}
        return self.tank_hit_walls

        # Количество выстрелов у танка, перезаряжается со временем


class Bullet:
    def __init__(self, x, y, v, scale):
        self.r = list([x, y])  # Координаты танка по осям х и у
        self.scale = scale  # Радиус пули
        self.v = v  # Двумерный вектор со скоростями по осям

# TODO Возможно, в процессе нужно будет добавить еще какие-то параметры
