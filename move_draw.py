# TODO здесь нужно написать функции, меняющие координаты объектов, а так же рисующие их
import pygame
import numpy as np
def bullet_move(obj,field):
    obj.r[0] += obj.v[0]  # вроде бы v- это вектор, поэтому беру проекцию
    obj.r[1] += obj.v[1]
    #FIXME      надо дописать изменение скорости пули при столкновении со стенкой, но пока не пойму, как строится карта

def tank_move(obj,field):
    keys = pygame.key.get_pressed()
    if obj.type == 1:
          if keys[pygame.K_w]:
              obj.r[0]+=obj.v*np.sin(obj.ang)
              obj.r[1] += obj.v*np.cos(obj.ang)
          elif keys[pygame.K_s]:
              obj.r[0] -= obj.v*np.sin(obj.ang)
              obj.r[1] -= obj.v*np.cos(obj.ang)
          if keys[pygame.K_a]:
              obj.ang += obj.omega
          elif keys[pygame.K_d]:
              obj.ang -= obj.omega
    else:
          if keys[pygame.K_UP]:
              obj.r[0] += obj.v * np.sin(obj.ang)
              obj.r[1] += obj.v * np.cos(obj.ang)
          elif keys[pygame.K_DOWN]:
              obj.r[0] -= obj.v * np.sin(obj.ang)
              obj.r[1] -= obj.v * np.cos(obj.ang)
          if keys[pygame.K_LEFT]:
              obj.ang += obj.omega
          elif keys[pygame.K_RIGHT]:
              obj.ang -= obj.omega


