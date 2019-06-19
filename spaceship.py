import pygame
class Spaceship():
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.width = 100
        self.height = 100
        self.color = pygame.Color(255,45,39)
        self.rect = pygame.Rect((self.pos_x,self.pos_y),(self.width,self.height))

    def getObject(self):
        return self.rect

    def getColor(self):
        return self.color

    def draw(self,surface):
        #surface.blit(surface,self.getObject())
        pygame.draw.rect(surface,self.getColor(),self.getObject())

    def updateObject(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        #self.rect = pygame.Rect((self.pos_x,self.pos_y),(self.width,self.height))

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys=pygame.key.get_pressed()

                #self.pos_x += 10
                #self.updateObject()
                #print self.pos_x
                if event.key == pygame.K_LEFT:
                    print pygame.K_LEFT
                    self.pos_x -= 20
                    self.updateObject()
                elif event.key == pygame.K_RIGHT:
                    print pygame.K_RIGHT
                    self.pos_x += 20
                    self.updateObject()
