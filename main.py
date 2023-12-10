import pygame
import sys

"""Нужно будет загрузить картинки и звуки в папку проекта, image path  и ему подобные - переменные, в которые 
мы записываем путь на звуки и картинки(если загрузим в проект, то вместо полного пути можно будет использовать просто имя,
что удобнее) "is_hovered" отвечает за наведение, если конпка мыши находится где-то внутри кнопки, вместо обычной 
картинки кнопки отображается другая(например, более светлая) "handle_event" отвечает за воспроизведение звука при клике 
на кнопку
 """
screen_width = 800
screen_height = 600

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
menu_background = pygame.image.load("имя файла")
settings_background = pygame.image.load("имя файла")
class Image_Button():
    def __init__(self,x,y,width,height,image_path,hover_image_path,sound_path=None):
        self.x=x #координата х верхнего левого угла
        self.y = y #координата у левого верхнего угла
        self.width = width #размер по горизонтали
        self.height = height # размер по вертикали
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(width,height))
        self.hover_image = pygame.image.load(hover_image_path)
        self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.sound = None
        self.is_hovered = False
    def draw(self,screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image,self.rect.topleft)
    def check_hover(self,mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    def handle_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()



def main_menu():


    start_button = Image_Button(screen_width / 2 - 252 / 2, 100, 252, 74, "start_button.jpg","hovered_start_button.jpg")
    quit_button = Image_Button(screen_width / 2 - 50, 250, 252, 74, "quit_button.png", "hovered_quit_button.png")
    settings_button = Image_Button(screen_width / 2 - 252 / 2, 400, 252, 74, "settings_button.jpg","hovered_settings_button.jpg")
    buttons = [start_button,settings_button, quit_button]
    running=True
    while running:
       screen.fill((0,0,0))
       screen.blit(settings_background, (0, 0))
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
               pygame.quit()
               sys.exit()
           for button in buttons:
               button.handle_event(event)
           if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and settings_button.is_hovered:
               settings_menu()
           if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and quit_button.is_hovered:
               running=False
               pygame.quit()
               sys.exit()
       for button in buttons:
           button.check_hover(pygame.mouse.get_pos())
           button.draw(screen)
       pygame.display.flip()
def settings_menu():
    back_button = Image_Button(screen_width / 2 - 150 / 2, 500, 150, 74, "button_back.png","hovered_button_back.png")
    buttons=[back_button]
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(settings_background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.handle_event(event)
            if  event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button.is_hovered:
                main_menu()
        for button in buttons:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)
        pygame.display.flip()

main_menu()