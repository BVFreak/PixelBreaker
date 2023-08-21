import pygame
import math

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.vel = 3
        self.is_moving = False
        self.direction = "down"
        self.image = pygame.image.load("assets/images/player/idle/1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.index = 0
        self.images_right = []
        self.images_left = []
        self.images_up = []
        self.images_down = []
        self.current_time = pygame.time.get_ticks()

        for i in range(1, 5):
            img_right = pygame.image.load(f"assets/images/player/run/{i}.png").convert_alpha()
            img_left = pygame.transform.flip(img_right, True, False)
            img_up = pygame.image.load(f"assets/images/player/run/{i}.png").convert_alpha()
            img_down = pygame.image.load(f"assets/images/player/run/{i}.png").convert_alpha()
            self.images_right.append(img_right)
            self.images_left.append(img_left)
            self.images_up.append(img_up)
            self.images_down.append(img_down)
        
        self.image = self.images_right[self.index]

    def update(self, screen, level):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and keys[pygame.K_w]:
            self.move_diagonal(-1, -1, "left")
            self.image = self.images_left[self.index]
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            self.move_diagonal(-1, 1, "left")
            self.image = self.images_left[self.index]
        elif keys[pygame.K_d] and keys[pygame.K_w]:
            self.move_diagonal(1, -1, "right")
            self.image = self.images_right[self.index]
        elif keys[pygame.K_d] and keys[pygame.K_s]:
            self.move_diagonal(1, 1, "right")
            self.image = self.images_right[self.index]
        elif keys[pygame.K_a]:
            self.move_single_axis(-1, 0, "left")
            self.image = self.images_left[self.index]
        elif keys[pygame.K_d]:
            self.move_single_axis(1, 0, "right")
            self.image = self.images_right[self.index]
        elif keys[pygame.K_w]:
            self.move_single_axis(0, -1, "up")
        elif keys[pygame.K_s]:
            self.move_single_axis(0, 1, "down")
        else:
            self.is_moving = False

        screen.blit(self.image, (int(self.x - level.x - 25), int(self.y - level.y - 50)))

        #print(f'self.images_{self.direction}[self.index]')
        
        if not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]):
            if self.direction == 'left':
                self.image = pygame.image.load("assets/images/player/idle/1.png").convert_alpha()
                self.image = pygame.transform.flip(self.image, True,False)
            if self.direction == 'right':
                self.image = pygame.image.load("assets/images/player/idle/1.png").convert_alpha()
            if self.direction == 'up':
                self.image = pygame.image.load("assets/images/player/idle/1.png").convert_alpha()
            if self.direction == 'down':
                self.image = pygame.image.load("assets/images/player/idle/1.png").convert_alpha()
            self.index = 0
        else:
            if pygame.time.get_ticks() > (self.current_time + 100):
                if (self.index + 1) >= len(self.images_right):
                    self.index = 0
                else:
                    self.index += 1

                self.current_time = pygame.time.get_ticks()

            if keys[pygame.K_a]:
                self.direction = 'left'
                self.image = pygame.transform.flip(self.images_left[self.index], True,False)
            if keys[pygame.K_d]:
                self.direction = 'right'
                self.image = pygame.transform.flip(self.images_right[self.index], True,False)
            if keys[pygame.K_w]:
                self.direction = 'up'
                self.image = self.images_up[self.index]
            if keys[pygame.K_s]:
                self.direction = 'down'
                self.image = self.images_down[self.index]




    def move_single_axis(self, dx, dy, direction):
        self.is_moving = True
        self.direction = direction
        self.x += dx * self.vel
        self.y += dy * self.vel


    def move_diagonal(self, dx, dy, direction):
        self.is_moving = True
        self.direction = direction
        self.x += dx * self.vel / math.sqrt(2)
        self.y += dy * self.vel / math.sqrt(2)