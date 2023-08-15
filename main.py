import pygame, sys, random
from player import Player
from button import Button
from crosshair import Crosshair
from level import Level

pygame.mixer.pre_init(44100,-16,2, 1024)
pygame.init()
pygame.mixer.init()

volume = 0.5

time_passed = 0

pygame.mixer.music.set_volume(volume)

# setup
screen = pygame.display.set_mode((1920, 1080))
BACKGROUND_MENU = "black"
BACKGROUND_GAME = "black"
BACKGROUND_SETTINGS = "black"
BACKGROUND_WARNING = "black"

pygame.display.set_caption("Pixel Breaker")

clock = pygame.time.Clock()

crosshair = Crosshair('assets/images/crosshair.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)
    
pygame.mouse.set_visible(False)

# audio
click = pygame.mixer.Sound("assets/audio/PremiumBeat_0013_cursor_click_11.wav")

hover = pygame.mixer.Sound("assets/audio/PremiumBeat_0013_move_cursor_11.wav")

menu_music = pygame.mixer.music.load("assets/audio/song55.mid")


# images
rect1 = pygame.image.load("assets/images/Rect1.png").convert()
rect2 = pygame.image.load("assets/images/Rect2.png").convert()
rect3 = pygame.image.load("assets/images/Rect3.png").convert()
gear = pygame.image.load("assets/images/settings_gear.png").convert()
question = pygame.image.load("assets/images/ques.png").convert()
info_img = pygame.image.load("assets/images/info.png").convert()
on = pygame.image.load("assets/images/audio_on.png").convert()
off = pygame.image.load("assets/images/audio_off.png").convert()

def get_font(size):
    return pygame.font.Font("assets/font.ttf", int(size))

width, height = 1920, 1080

level = Level()
player = Player(width/2,height/2)

map_surface = pygame.Surface((1920, 1080))

new_width = 1.6
new_height = 1.53125
new_size = 2

def start_menu():
    pygame.mixer.music.stop()
    level_music = pygame.mixer.music.load("assets/audio/song55.mid")
    pygame.mixer.music.play()
    while True:
        screen.fill((0,0,0))

        mouse_pos = pygame.mouse.get_pos()
        start_text = get_font(100*new_size).render("Pixel Breaker", True, "purple").convert_alpha()
        start_rect = start_text.get_rect(center=(600*new_width, 100*new_height))

        PLAY_BUTTON = Button(image=rect1, pos=(600*new_width, 300*new_height),
                             text_input="play", font=get_font(75*new_size), base_color="White", hovering_color="Green")
        QUIT_BUTTON = Button(image=rect1, pos=(600*new_width, 500*new_height),
                             text_input="quit", font=get_font(75*new_size), base_color="White", hovering_color="Red")
        SETTINGS_BUTTON = Button(image=gear, pos=(1140*new_width, 60*new_height),
                                 text_input="", font=get_font(30*new_size), base_color="White", hovering_color="Black")
        HOWTOPLAY_BUTTON = Button(image=question, pos=(1135*new_width, 310*new_height),
                             text_input="", font=get_font(75*new_size), base_color="White", hovering_color="Red")
        INFO_BUTTON = Button(image=info_img, pos=(1140*new_width, 175*new_height),
                             text_input="", font=get_font(75*new_size), base_color="White", hovering_color="Red")

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
                    pygame.mixer.Sound.play(click)
                    play()
                if SETTINGS_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(click)
                    settings()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(click)
                    warning_quit()
                if HOWTOPLAY_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(click)
                    howtoplay()
                if INFO_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(click)
                    info()

        crosshair_group.draw(screen)
        crosshair_group.update()

        pygame.display.update()
    
def howtoplay():
    about = """
    Pixel Breaker is a stealth game where you play as a hacker who can only see the level when he is standing still. You and your mentor are data thieves who break into high-security buildings and steal valuable information from corporations. However, your latest heist goes wrong when you are betrayed by a fellow data thief who steals your data and leaves you for dead. You manage to escape, but you are now hunted by the corporations and the traitor. You have to use your hacking skills and your mutation to sneak past enemies, hack devices, and find clues to track down the traitor and get your data back. Along the way, you will discover secrets and conspiracies that will change your life forever.

    The game features pixel art graphics, cyberpunk music, and simple controls. The game is divided into levels, each with a different setting, layout, and objective. The game challenges you to use your vision wisely, as you can only see the level when you are still, but you also have to move quickly and quietly to avoid detection. The game also lets you hack various devices, such as cameras, doors, alarms, and robots, to help you progress or distract your enemies. The game has a branching storyline, with multiple endings depending on your choices and actions.
    """
    while True:
        screen.fill((0,0,0))

        mouse_pos = pygame.mouse.get_pos()

        howtoplay_text = get_font(100*new_size).render("ABOUT", True, "white").convert_alpha()
        howtoplay_rect = howtoplay_text.get_rect(center=(600*new_width, 100*new_height))

        howtoplay2_text = get_font(10*new_size).render(about, True, "white").convert_alpha()
        howtoplay2_rect = howtoplay2_text.get_rect(center=(600*new_width, 300*new_height))

        RETURN_BUTTON = Button(image=rect1, pos=(600*new_width, 500*new_height),
                        text_input="return", font=get_font(50*new_size), base_color="white", hovering_color="Darkgray")

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
                    pygame.mixer.Sound.play(click)
                    return
                
        crosshair_group.draw(screen)
        crosshair_group.update()
        
        pygame.display.update()

def settings():
    global volume
    while True:
        screen.fill(BACKGROUND_SETTINGS)

        mouse_pos = pygame.mouse.get_pos()

        SETTINGS_TEXT = get_font(100*new_size).render("SETTINGS", True, "gray").convert_alpha()
        SETTINGS_RECT = SETTINGS_TEXT.get_rect(center=(600*new_width, 100*new_height))

        RETURN_BUTTON = Button(image=rect2, pos=(600*new_width, 400*new_height),
                            text_input="return", font=get_font(75*new_size), base_color="White", hovering_color="DarkGray")

        AUDIO_ON_BUTTON = Button(image=on, pos=(500*new_width, 250*new_height),
                            text_input="", font=get_font(75*new_size), base_color="White", hovering_color="DarkGray")
        AUDIO_OFF_BUTTON = Button(image=off, pos=(700*new_width, 250*new_height),
                            text_input="", font=get_font(75*new_size), base_color="White", hovering_color="DarkGray")
        
        screen.blit(SETTINGS_TEXT, SETTINGS_RECT)
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
                    pygame.mixer.Sound.play(click)
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AUDIO_ON_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(click)
                    if volume <= 1:
                        volume += 0.1
                    pygame.mixer.music.set_volume(volume)
                elif AUDIO_OFF_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(click)
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
        screen.fill(BACKGROUND_WARNING)

        mouse_pos = pygame.mouse.get_pos()

        warning_text = get_font(75*new_size).render("Are you sure you want to quit?", True, (255, 255, 255)).convert_alpha()
        warning_rect = warning_text.get_rect(center=(600*new_width, 100*new_height))

        YES_BUTTON = Button(image=rect1, pos=(425*new_width, 250*new_height),
                             text_input="yes", font=get_font(75*new_size), base_color="White", hovering_color="Green")
        NO_BUTTON = Button(image=rect1, pos=(775*new_width, 250*new_height),
                                 text_input="no", font=get_font(75*new_size), base_color="White", hovering_color="Red")

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
                    pygame.mixer.Sound.play(click)
                    return
                if YES_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(click)
                    pygame.quit()
                    sys.exit()

        crosshair_group.draw(screen)
        crosshair_group.update()

        pygame.display.update()

def info():
    while True:
        screen.fill(BACKGROUND_SETTINGS)

        mouse_pos = pygame.mouse.get_pos()

        INFO_TEXT = get_font(100*new_size).render("INFO", True, "blue").convert_alpha()
        INFO_RECT = INFO_TEXT.get_rect(center=(600*new_width, 100*new_height))

        CREDITS1_TEXT = get_font(50*new_size).render("this was made by blake verner copyright lololol", True, "silver").convert_alpha()
        CREDITS1_RECT = CREDITS1_TEXT.get_rect(center=(600*new_width, 200*new_height))

        CREDITS2_TEXT = get_font(60*new_size).render("made in pygame", True, "gold").convert_alpha()
        CREDITS2_RECT = CREDITS2_TEXT.get_rect(center=(600*new_width, 300*new_height))

        RETURN_BUTTON = Button(image=rect2, pos=(600*new_width, 400*new_height),
                            text_input="return", font=get_font(75*new_size), base_color="White", hovering_color="DarkGray")

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
                    pygame.mixer.Sound.play(click)
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
            screen_value -= 5
        
        screen.fill((0,0,0))

        #map_surface.set_alpha(screen_value)

        level.draw(screen)
        #screen.blit(map_surface, (0, 0))
        
        level.update(player)
        player.update(screen, level)
        
        crosshair_group.draw(screen)
        crosshair_group.update()

        pygame.display.update()

start_menu()