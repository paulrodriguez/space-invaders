import pygame
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 500
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
    
    def getScreen(self):
        return self.screen 
