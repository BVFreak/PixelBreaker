import pygame, sys
from assets.scripts.player import Player
from assets.scripts.button import Button
from assets.scripts.crosshair import Crosshair
from assets.scripts.level import Level
from assets.scripts.font import get_font
from assets.scripts import debugging

pygame.mixer.pre_init(44100,-16,2, 1024)
pygame.init()
pygame.mixer.init()

volume = 0.5

time_passed = 0

pygame.mixer.music.set_volume(volume) 

# setup
screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode((screen_width, screen_height))
BACKGROUND = "black"
BACKGROUND_IMAGE = pygame.image.load("assets/images/far-buildings.png").convert_alpha()

image_width, image_height = BACKGROUND_IMAGE.get_size()

scale_x = screen_width / image_width
scale_y = screen_height / image_height
scale = max(scale_x, scale_y)

# Calculate the new dimensions of the image
new_image_width = int(image_width * scale)
new_image_height = int(image_height * scale)

# Resize the background image to cover the screen
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (new_image_width, new_image_height))

# Calculate the position to center the image on the screen
x_offset = (new_image_width - screen_width) // -2
y_offset = (new_image_height - screen_height) // -2

pygame.display.set_caption("Pixel Breaker")

clock = pygame.time.Clock()

crosshair = Crosshair('assets/images/crosshair.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)
    
pygame.mouse.set_visible(False)

# audio
button_click = pygame.mixer.Sound("assets/audio/cursor_click_01.wav")
change_click = pygame.mixer.Sound("assets/audio/cursor_click_11.wav")

hover = pygame.mixer.Sound("assets/audio/move_cursor_11.wav")

menu_music = pygame.mixer.music.load("assets/audio/song55.mid")


# images
rect1 = pygame.image.load("assets/images/Rect1.png").convert()
rect2 = pygame.image.load("assets/images/Rect2.png").convert()
rect3 = pygame.image.load("assets/images/Rect3.png").convert()
gear = pygame.image.load("assets/images/settings_gear.png").convert_alpha()
question = pygame.image.load("assets/images/ques.png").convert_alpha()
info_img = pygame.image.load("assets/images/info.png").convert_alpha()
on = pygame.image.load("assets/images/audio_on.png").convert()
off = pygame.image.load("assets/images/audio_off.png").convert()


level = Level()
player = Player(screen_width/2,screen_height/2)

map_surface = pygame.Surface((1920, 1080)).convert_alpha()

def start_menu():
    pygame.mixer.music.stop()
    level_music = pygame.mixer.music.load("assets/audio/song55.mid")
    pygame.mixer.music.play()
    while True:
        screen.fill(BACKGROUND)

        mouse_pos = pygame.mouse.get_pos()
        start_text = get_font(200).render("Pixel Breaker", True, "orange").convert_alpha()
        start_rect = start_text.get_rect(center=(960, 150))

        PLAY_BUTTON = Button(image=rect1, pos=(960, 450),
                             text_input="Play", font=get_font(150), base_color="White", hovering_color="Green")
        QUIT_BUTTON = Button(image=rect1, pos=(960, 750),
                             text_input="Quit", font=get_font(150), base_color="White", hovering_color="Red")
        SETTINGS_BUTTON = Button(image=gear, pos=(1825, 90),
                                 text_input="", font=get_font(60), base_color="White", hovering_color="Black")
        HOWTOPLAY_BUTTON = Button(image=question, pos=(1815, 465),
                             text_input="", font=get_font(150), base_color="White", hovering_color="Red")
        INFO_BUTTON = Button(image=info_img, pos=(1825, 260),
                             text_input="", font=get_font(150), base_color="White", hovering_color="Red")

        screen.blit(BACKGROUND_IMAGE, (0, 0))
        
        screen.blit(start_text, start_rect)

        for button in [PLAY_BUTTON, SETTINGS_BUTTON, QUIT_BUTTON, HOWTOPLAY_BUTTON, INFO_BUTTON]:
            #pygame.mixer.Sound.play(hover)
            button.changeColor(mouse_pos)
            button.update(screen)


        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                warning_quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    play()
                if SETTINGS_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    settings()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    warning_quit()
                if HOWTOPLAY_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    howtoplay()
                if INFO_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    info()

        crosshair_group.draw(screen)
        crosshair_group.update()

        pygame.display.update()
        
def menu():
    while True:
        screen.fill(BACKGROUND)

        mouse_pos = pygame.mouse.get_pos()
        start_text = get_font(200).render("Pixel Breaker", True, "orange").convert_alpha()
        start_rect = start_text.get_rect(center=(960, 150))

        PLAY_BUTTON = Button(image=rect1, pos=(960, 450),
                             text_input="Play", font=get_font(150), base_color="White", hovering_color="Green")
        QUIT_BUTTON = Button(image=rect1, pos=(960, 750),
                             text_input="Quit", font=get_font(150), base_color="White", hovering_color="Red")
        SETTINGS_BUTTON = Button(image=gear, pos=(1825, 90),
                                 text_input="", font=get_font(60), base_color="White", hovering_color="Black")
        HOWTOPLAY_BUTTON = Button(image=question, pos=(1815, 465),
                             text_input="", font=get_font(150), base_color="White", hovering_color="Red")
        INFO_BUTTON = Button(image=info_img, pos=(1825, 260),
                             text_input="", font=get_font(150), base_color="White", hovering_color="Red")

        screen.blit(BACKGROUND_IMAGE, (0, 0))
        
        screen.blit(start_text, start_rect)

        for button in [PLAY_BUTTON, SETTINGS_BUTTON, QUIT_BUTTON, HOWTOPLAY_BUTTON, INFO_BUTTON]:
            #pygame.mixer.Sound.play(hover)
            button.changeColor(mouse_pos)
            button.update(screen)


        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                warning_quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    play()
                if SETTINGS_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    settings()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    warning_quit()
                if HOWTOPLAY_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    howtoplay()
                if INFO_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    info()

        crosshair_group.draw(screen)
        crosshair_group.update()

        pygame.display.update()

def howtoplay():
    about = """
    Controls
    WASD | Movement
    Esc  | Menu/Quit
    """
    while True:
        screen.fill((0,0,0))

        mouse_pos = pygame.mouse.get_pos()

        howtoplay_text = get_font(250).render("ABOUT", True, "white").convert_alpha()
        howtoplay_rect = howtoplay_text.get_rect(center=(960, 150))

        howtoplay2_text = get_font(50).render(about, True, "white").convert_alpha()
        howtoplay2_rect = howtoplay2_text.get_rect(center=(960, 450))

        RETURN_BUTTON = Button(image=rect2, pos=(960, 750),
                        text_input="Return", font=get_font(150), base_color="white", hovering_color="Darkgray")

        screen.blit(howtoplay_text,howtoplay_rect)
        screen.blit(howtoplay2_text,howtoplay2_rect)

        for button in [RETURN_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    return
                
        crosshair_group.draw(screen)
        crosshair_group.update()
        
        pygame.display.update()

def settings():
    global volume
    while True:
        screen.fill(BACKGROUND)

        mouse_pos = pygame.mouse.get_pos()

        SETTINGS_TEXT = get_font(200).render("SETTINGS", True, "gray").convert_alpha()
        SETTINGS_RECT = SETTINGS_TEXT.get_rect(center=(960, 150))
        
        VOLUME_TEXT = get_font(40).render(f"Volume [ {round(volume, 2)}% ]", True, "white").convert_alpha()
        VOLUME_RECT = VOLUME_TEXT.get_rect(center=(960, 900))

        RETURN_BUTTON = Button(image=rect2, pos=(960, 750),
                            text_input="Return", font=get_font(150), base_color="White", hovering_color="DarkGray")

        AUDIO_ON_BUTTON = Button(image=on, pos=(800, 375),
                            text_input="", font=get_font(150), base_color="White", hovering_color="DarkGray")
        AUDIO_OFF_BUTTON = Button(image=off, pos=(1120, 375),
                            text_input="", font=get_font(150), base_color="White", hovering_color="DarkGray")
        
        screen.blit(SETTINGS_TEXT, SETTINGS_RECT)
        screen.blit(VOLUME_TEXT, VOLUME_RECT)
        
        for button in [AUDIO_ON_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for button in [AUDIO_OFF_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)
            

        for button in [RETURN_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                warning_quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AUDIO_ON_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(change_click)
                    if volume <= 1:
                        volume += 0.1
                    pygame.mixer.music.set_volume(volume)
                elif AUDIO_OFF_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(change_click)
                    if volume >= 0:
                        volume -= 0.1
                    pygame.mixer.music.set_volume(volume)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            warning_quit()

        crosshair_group.draw(screen)
        crosshair_group.update()

        pygame.display.update()

def warning_quit():
    while True:
        screen.fill(BACKGROUND)

        mouse_pos = pygame.mouse.get_pos()

        warning_text = get_font(150).render("Are you sure you want to quit?", True, (255, 255, 255)).convert_alpha()
        warning_rect = warning_text.get_rect(center=(960, 150))

        YES_BUTTON = Button(image=rect1, pos=(680, 375),
                             text_input="Yes", font=get_font(150), base_color="White", hovering_color="Green")
        NO_BUTTON = Button(image=rect1, pos=(1240, 375),
                                 text_input="No", font=get_font(150), base_color="White", hovering_color="Red")

        screen.blit(warning_text, warning_rect)

        for button in [YES_BUTTON, NO_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NO_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    return
                if YES_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    pygame.quit()
                    sys.exit()

        crosshair_group.draw(screen)
        crosshair_group.update()

        pygame.display.update()

def info():
    while True:
        screen.fill(BACKGROUND)

        mouse_pos = pygame.mouse.get_pos()

        INFO_TEXT = get_font(200).render("INFO & CREDITS", True, "blue").convert_alpha()
        INFO_RECT = INFO_TEXT.get_rect(center=(960, 150))

        CREDITS1_TEXT = get_font(100).render("Blake Verner - Developer", True, "silver").convert_alpha()
        CREDITS1_RECT = CREDITS1_TEXT.get_rect(center=(960, 300))

        CREDITS2_TEXT = get_font(90).render("cTrix - Music", True, "silver").convert_alpha()
        CREDITS2_RECT = CREDITS2_TEXT.get_rect(center=(960, 410))

        RETURN_BUTTON = Button(image=rect2, pos=(960, 600),
                            text_input="return", font=get_font(150), base_color="White", hovering_color="DarkGray")

        screen.blit(INFO_TEXT, INFO_RECT)
        screen.blit(CREDITS1_TEXT, CREDITS1_RECT)
        screen.blit(CREDITS2_TEXT, CREDITS2_RECT)

        for button in [RETURN_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                warning_quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(button_click)
                    return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            warning_quit()
            
        crosshair_group.draw(screen)
        crosshair_group.update()

        pygame.display.update()

def play():
    screen_value = 255
    pygame.mixer.music.stop()
    level_music = pygame.mixer.music.load("assets/audio/bass.mid")
    pygame.mixer.music.play()

    while True:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                start_menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if player.is_moving == True and screen_value < 255:
            # vision
            screen_value += 5
        if player.is_moving == False and screen_value > 0:
            # no vision
            screen_value -= 10
        
        screen.fill((0, 0, 0))

        map_surface.set_alpha(screen_value)
        
        level.draw(screen)

        screen.blit(map_surface, (0, 0))

        level.update(player)
        player.update(screen, level)

        ### ! Use only for debugging !
        #debugging.debug(screen, screen_value)
        ###


        crosshair_group.draw(screen)
        crosshair_group.update()

        pygame.display.update()


start_menu()
