import pygame, random, math

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = random.randint(1, 3)
        self.is_moving = False
        self.direction = random.choice(["left", "right", "up", "down"])
        self.image = pygame.image.load("assets/images/player/idle/1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.index = 0
        self.images_right = []
        self.images_left = []
        self.images_up = []
        self.images_down = []
        self.current_time = pygame.time.get_ticks()
        self.change_interval = random.randint(1000, 3000)

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
        # check if the enemy needs to change direction
        if random.random() < random.uniform(0.01,0.1):
            # choose a random direction from the four options
            self.direction = random.choice(["left", "right", "up", "down"])
            # choose a random speed from 1 to 5
            self.speed = random.randint(1, 3)
            # choose a random interval from 1 to 3 seconds
            self.change_interval = random.randint(1000, 3000)
            # update the change time
            self.current_time = pygame.time.get_ticks()

        # move in the current direction with the current speed
        if self.direction == "left":
            self.move_single_axis(-self.speed, 0, "left")
            self.image = self.images_left[self.index]
        elif self.direction == "right":
            self.move_single_axis(self.speed, 0, "right")
            self.image = self.images_right[self.index]
        elif self.direction == "up":
            self.move_single_axis(0, -self.speed, "up")
            self.image = self.images_up[self.index]
        elif self.direction == "down":
            self.move_single_axis(0, self.speed, "down")
            self.image = self.images_down[self.index]

        screen.blit(self.image, (int(self.x - level.x - 25), int(self.y - level.y - 50)))

        # update the animation index every 100 milliseconds
        if pygame.time.get_ticks() > (self.current_time + 100):
            if (self.index + 1) >= len(self.images_right):
                self.index = 0
            else:
                self.index += 1

            self.current_time = pygame.time.get_ticks()

        # check if the enemy has reached the edge of the screen or collided with an obstacle
        screen_width, screen_height = pygame.display.get_surface().get_size() # get the size of the screen

        # check if the enemy has reached the left or right edge of the screen
        if self.x < 0 or self.x > screen_width:
            # reverse the horizontal direction of the enemy
            if self.direction == "left":
                self.direction = "right"
            elif self.direction == "right":
                self.direction = "left"

        # check if the enemy has reached the top or bottom edge of the screen
        if self.y < 0 or self.y > screen_height:
            # reverse the vertical direction of the enemy
            if self.direction == "up":
                self.direction = "down"
            elif self.direction == "down":
                self.direction = "up"

    def move_single_axis(self, dx, dy, direction):
        # move the enemy in a single axis
        self.direction = direction
        self.x += dx
        self.y += dy

    def move_diagonal(self, dx, dy, direction):
        # move the enemy in a diagonal direction
        self.direction = direction
        self.x += dx / math.sqrt(2)
        self.y += dy / math.sqrt(2)
