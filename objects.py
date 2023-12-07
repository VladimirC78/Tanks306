class Tank:
    def __init__(self, x, y, scale):
        self.r = list([x, y])  # Координаты танка по осям х и у
        self.scale = scale  # Характерный размер танка
        self.v = [0, 0]  # Скорость танка по осям х и у
        self.charges = 5  # Количество выстрелов у танка, перезаряжается со временем


class Bullet:
    def __init__(self, x, y, v, rad):
        self.r = list([x, y])  # Координаты танка по осям х и у
        self.rad = rad  # Радиус пули
        self.v = v  # Двумерный вектор со скоростями по осям
