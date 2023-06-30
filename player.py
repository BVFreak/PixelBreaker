import pygame
import math

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.vel = 1

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x - self.width // 2, self.y - self.height // 2, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            self.x -= self.vel / math.sqrt(2)
            self.y -= self.vel / math.sqrt(2)
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            self.x -= self.vel / math.sqrt(2)
            self.y += self.vel / math.sqrt(2)
        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            self.x += self.vel / math.sqrt(2)
            self.y -= self.vel / math.sqrt(2)
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            self.x += self.vel / math.sqrt(2)
            self.y += self.vel / math.sqrt(2)
        elif keys[pygame.K_LEFT]:
            self.x -= self.vel
        elif keys[pygame.K_RIGHT]:
            self.x += self.vel
        elif keys[pygame.K_UP]:
            self.y -= self.vel
        elif keys[pygame.K_DOWN]:
            self.y += self.vel

