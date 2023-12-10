
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
    def tank_check_hit(self,walls):
        L,R,U,D = 0,0,0,0
        for wall in walls:
            if wall.wall_hit(self)["l"]==True:
                L+=1
            if wall.wall_hit(self)["r"]==True:
                 R+=1
            if wall.wall_hit(self)["u"]==True:
                 U+=1
            if wall.wall_hit(self)["d"]==True:
                 D+=1
        self.tank_hit_walls = {'u': bool(U), 'd': bool(D), 'r': bool(R), 'l': bool(L)}
        return self.tank_hit_walls

                # Количество выстрелов у танка, перезаряжается со временем
        self.live=1 #жизнь танка

class Bullet:
    def __init__(self, x, y, v, scale):
        self.r = list([x, y])  # Координаты танка по осям х и у
        self.scale = scale  # Радиус пули
        self.v = v  # Двумерный вектор со скоростями по осям

# TODO Возможно, в процессе нужно будет добавить еще какие-то параметры
