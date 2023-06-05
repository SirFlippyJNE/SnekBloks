#imports
import pygame as pg
from random import randrange
import random
from Button import Button
import sys

#begins program
pg.init()
pg.mixer.init()
SCREEN = pg.display.set_mode((1280, 720))
pg.display.set_caption("SnekBloks 0.11.0")
#imports background image
BG = pg.image.load("assets/BackGround.png")
#imports sounds
APPLE = pg.mixer.Sound('assets/apple_bite.ogg')
COLLIDE = pg.mixer.Sound('assets/collide.flac')
MUSIC1 = pg.mixer.Sound('assets/SnekBloks-MainMenu.ogg')
#MUSIC2 = pg.mixer.Sound()
#MOVEMENT = pg.mixer.Sound()
#SPAWN = pg.mixer.Sound()
def get_font(size): # Returns Font in the desired size
    return pg.font.Font("assets/font/Font.otf", size)
#game functions
def Fullscreen():
    while True:
        MUSIC1.play()
        FULLSCREEN_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.fill('Black')
        FULLSCREEN_TEXT = get_font(75).render('FULLSCREEN', True, 'White')
        FULLSCREEN_RECT = FULLSCREEN_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(FULLSCREEN_TEXT, FULLSCREEN_RECT)
        #Buttons
        ON = Button(image=None, pos=(500, 150),
                    text_input='ON', font=get_font(50), base_color='White', hovering_color='Green')
        OFF = Button(image=None, pos=(750, 150),
                    text_input='OFF', font=get_font(50), base_color='White', hovering_color='Green')
        BACK = Button(image=None, pos=(640, 650),
                    text_input='BACK', font=get_font(50), base_color='White', hovering_color='Green')
        for button in (ON, OFF, BACK):
            button.changeColor(FULLSCREEN_MOUSE_POS)
            button.update(SCREEN)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if ON.checkForInput(FULLSCREEN_MOUSE_POS):
                    pg.display.set_mode((1280, 720), pg.FULLSCREEN)
                elif OFF.checkForInput(FULLSCREEN_MOUSE_POS):
                    pg.display.set_mode((1280, 720))
                elif BACK.checkForInput(FULLSCREEN_MOUSE_POS):
                    options()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    options()
        pg.display.update()
def peacefull():
    MUSIC1.stop()
    pg.display.set_caption('SnekBloks')
    pg.font.init()
    WINDOW = 1280
    HEIGHT = 720
    TILE_SIZE = 50
    RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
    get_random_post = lambda: [randrange(*RANGE), randrange(*RANGE)]
    snek = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
    snek.center = get_random_post()
    length = 1
    segments = [snek.copy()]
    snek_dir = (0, 0)
    time, time_step = 0, 110
    food1 = snek.copy()
    food1.center = get_random_post()
    food2 = snek.copy()
    food2.center = get_random_post()
    food3 = snek.copy()
    food3.center = get_random_post()
    food4 = snek.copy()
    food4.center = get_random_post()
    clock = pg.time.Clock()
    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
    
    #score variables
    current_score = 0
    high_score = 0
    recent_score = 0
    #snek
    while True:
        if current_score > high_score:
            high_score = current_score
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and dirs[pg.K_w]:
                    snek_dir = (0, -TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_s and dirs[pg.K_s]:
                    snek_dir = (0, TILE_SIZE)
                    dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_a and dirs[pg.K_a]:
                    snek_dir = (-TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_d and dirs[pg.K_d]:
                    snek_dir = (TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_UP and dirs[pg.K_UP]:
                    snek_dir = (0, -TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 0, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_DOWN and dirs[pg.K_s]:
                    snek_dir = (0, TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 0, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_LEFT and dirs[pg.K_a]:
                    snek_dir = (-TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 0}
                elif event.key == pg.K_RIGHT and dirs[pg.K_d]:
                    snek_dir = (TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 0, pg.K_RIGHT: 1}
                elif event.key == pg.K_ESCAPE:
                    MainMenu()
        SCREEN.fill('blue')
        #check borders and selfeatingas while as working collisions
        self_eating = pg.Rect.collidelist(snek, segments[:-1]) != -1
        if snek.left < 0 or snek.right > WINDOW or snek.top < 0 or snek.bottom > HEIGHT or self_eating:
            snek.center, food1.center, food2.center, food3.center, food4.center =  get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()            
            length, snek_dir = 1, (0, 0)
            segments = [snek.copy()]
            recent_score = current_score
            current_score = 0
            COLLIDE.play()
        elif food1.left < 0 or food1.right > WINDOW or food1.top < 0 or food1.bottom > HEIGHT:
            food1.center = get_random_post()
        elif food2.left < 0 or food2.right > WINDOW or food2.top < 0 or food2.bottom > HEIGHT:
            food2.center = get_random_post()
        elif food3.left < 0 or food3.right > WINDOW or food3.top < 0 or food3.bottom > HEIGHT:
            food3.center = get_random_post()
        elif food4.left < 0 or food4.right > WINDOW or food4.top < 0 or food4.bottom > HEIGHT:
            food4.center = get_random_post()
        elif snek.center == food1.center:
            food1.center = get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food2.center:
            food2.center = get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food3.center:
            food3.center = get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food4.center:
            food4.center = get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        #draw food
        pg.draw.rect(SCREEN, 'red', food1)
        pg.draw.rect(SCREEN, 'red', food2)
        pg.draw.rect(SCREEN, 'red', food3)
        pg.draw.rect(SCREEN, 'red', food4)
        #draw snek
        [pg.draw.rect(SCREEN, 'green', segment) for segment in segments]
        #move snek
        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snek.move_ip(snek_dir)
            segments.append(snek.copy())
            segments = segments[-length:]
        score_surface = get_font(25).render(f"Current Score {current_score}  Last Score {recent_score}  High Score {high_score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(640, 680))
        SCREEN.blit(score_surface, score_rect)
        pg.display.flip()
        clock.tick(60)
def easy():
    MUSIC1.stop()
    pg.display.set_caption('SnekBloks')
    pg.font.init()
    WINDOW = 1280
    HEIGHT = 720
    TILE_SIZE = 50
    RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
    get_random_post = lambda: [randrange(*RANGE), randrange(*RANGE)]
    snek = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
    snek.center = get_random_post()
    length = 1
    segments = [snek.copy()]
    snek_dir = (0, 0)
    time, time_step = 0, 110
    food1 = snek.copy()
    food1.center = get_random_post()
    food2 = snek.copy()
    food2.center = get_random_post()
    food3 = snek.copy()
    food3.center = get_random_post()
    food4 = snek.copy()
    food4.center = get_random_post()
    clock = pg.time.Clock()
    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
    blok1 = snek.copy()
    blok1.center = get_random_post()
    blok2 = snek.copy()
    blok2.center = get_random_post()
    blok3 = snek.copy()
    blok3.center = get_random_post()
    blok4 = snek.copy()
    blok4.center = get_random_post()
    #score variables
    current_score = 0
    high_score = 0
    recent_score = 0
    #snek
    while True:
        if current_score > high_score:
            high_score = current_score
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and dirs[pg.K_w]:
                    snek_dir = (0, -TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_s and dirs[pg.K_s]:
                    snek_dir = (0, TILE_SIZE)
                    dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_a and dirs[pg.K_a]:
                    snek_dir = (-TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_d and dirs[pg.K_d]:
                    snek_dir = (TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_UP and dirs[pg.K_UP]:
                    snek_dir = (0, -TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 0, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_DOWN and dirs[pg.K_s]:
                    snek_dir = (0, TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 0, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_LEFT and dirs[pg.K_a]:
                    snek_dir = (-TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 0}
                elif event.key == pg.K_RIGHT and dirs[pg.K_d]:
                    snek_dir = (TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 0, pg.K_RIGHT: 1}
                elif event.key == pg.K_ESCAPE:
                    MainMenu()
        SCREEN.fill('blue')
        #check borders and selfeatingas while as working collisions
        self_eating = pg.Rect.collidelist(snek, segments[:-1]) != -1
        if snek.left < 0 or snek.right > WINDOW or snek.top < 0 or snek.bottom > HEIGHT or self_eating:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()            
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0, 0)
            segments = [snek.copy()]
            recent_score = current_score
            current_score = 0
            COLLIDE.play()
        elif food1.left < 0 or food1.right > WINDOW or food1.top < 0 or food1.bottom > HEIGHT:
            food1.center = get_random_post()
        elif food2.left < 0 or food2.right > WINDOW or food2.top < 0 or food2.bottom > HEIGHT:
            food2.center = get_random_post()
        elif food3.left < 0 or food3.right > WINDOW or food3.top < 0 or food3.bottom > HEIGHT:
            food3.center = get_random_post()
        elif food4.left < 0 or food4.right > WINDOW or food4.top < 0 or food4.bottom > HEIGHT:
            food4.center = get_random_post()
        elif blok1.left < 0 or blok1.right > WINDOW or blok1.top < 0 or blok1.bottom > HEIGHT:
            blok1.center = get_random_post()
        elif blok2.left < 0 or blok2.right > WINDOW or blok2.top < 0 or blok2.bottom > HEIGHT:
            blok2.center = get_random_post()
        elif blok3.left < 0 or blok3.right > WINDOW or blok3.top < 0 or blok3.bottom > HEIGHT:
            blok3.center = get_random_post()
        elif blok4.left < 0 or blok4.right > WINDOW or blok4.top < 0 or blok4.bottom > HEIGHT:
            blok4.center = get_random_post()
        elif snek.center == food1.center:
            food1.center = get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food2.center:
            food2.center = get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food3.center:
            food3.center = get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food4.center:
            food4.center = get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == blok1.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            COLLIDE.play()
        elif snek.center == blok2.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            COLLIDE.play()
        elif snek.center == blok3.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            COLLIDE.play()
        elif snek.center == blok4.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            COLLIDE.play()
        elif food1.center == blok1.center:
            food1.center = get_random_post()
        elif food1.center == blok2.center:
            food1.center = get_random_post()
        elif food1.center == blok3.center:
            food1.center = get_random_post()
        elif food1.center == blok4.center:
            food1.center = get_random_post()
        elif food2.center == blok1.center:
            food2.center = get_random_post()
        elif food2.center == blok2.center:
            food2.center = get_random_post()
        elif food2.center == blok3.center:
            food2.center = get_random_post()
        elif food2.center == blok4.center:
            food2.center = get_random_post()
        elif food3.center == blok1.center:
            food3.center = get_random_post()
        elif food3.center == blok2.center:
            food3.center = get_random_post()
        elif food3.center == blok3.center:
            food3.center = get_random_post()
        elif food3.center == blok4.center:
            food3.center = get_random_post()
        elif food4.center == blok1.center:
            food4.center = get_random_post()
        elif food4.center == blok2.center:
            food4.center = get_random_post()
        elif food4.center == blok3.center:
            food4.center = get_random_post()
        elif food4.center == blok4.center:
            food4.center = get_random_post()
        #draw food
        pg.draw.rect(SCREEN, 'red', food1)
        pg.draw.rect(SCREEN, 'red', food2)
        pg.draw.rect(SCREEN, 'red', food3)
        pg.draw.rect(SCREEN, 'red', food4)
        #draw snek
        [pg.draw.rect(SCREEN, 'green', segment) for segment in segments]
        #draw bloks
        pg.draw.rect(SCREEN, 'yellow', blok1)
        pg.draw.rect(SCREEN, 'yellow', blok2)
        pg.draw.rect(SCREEN, 'yellow', blok3)
        pg.draw.rect(SCREEN, 'yellow', blok4)
        #move snek
        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snek.move_ip(snek_dir)
            segments.append(snek.copy())
            segments = segments[-length:]
        score_surface = get_font(25).render(f"Current Score {current_score}  Last Score {recent_score}  High Score {high_score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(640, 680))
        SCREEN.blit(score_surface, score_rect)
        pg.display.flip()
        clock.tick(60)
def normal():
    MUSIC1.stop()
    pg.display.set_caption('SnekBloks')
    pg.font.init()
    global WINDOW
    WINDOW = 1280
    global HEIGHT
    HEIGHT = 720
    TILE_SIZE = 50
    RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
    get_random_post = lambda: [randrange(*RANGE), randrange(*RANGE)]
    snek = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
    snek.center = get_random_post()
    length = 1
    segments = [snek.copy()]
    snek_dir = (0, 0)
    time, time_step = 0, 110
    food1 = snek.copy()
    food1.center = get_random_post()
    food2 = snek.copy()
    food2.center = get_random_post()
    food3 = snek.copy()
    food3.center = get_random_post()
    food4 = snek.copy()
    food4.center = get_random_post()
    clock = pg.time.Clock()
    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
    blok1 = snek.copy()
    blok1.center = get_random_post()
    blok2 = snek.copy()
    blok2.center = get_random_post()
    blok3 = snek.copy()
    blok3.center = get_random_post()
    blok4 = snek.copy()
    blok4.center = get_random_post()
    blok5 = snek.copy()
    blok5.center = get_random_post()
    
    #score variables
    current_score = 0
    high_score = 0
    recent_score = 0
    #snek
    while True:
        if current_score > high_score:
            high_score = current_score
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and dirs[pg.K_w]:
                    snek_dir = (0, -TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_s and dirs[pg.K_s]:
                    snek_dir = (0, TILE_SIZE)
                    dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_a and dirs[pg.K_a]:
                    snek_dir = (-TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_d and dirs[pg.K_d]:
                    snek_dir = (TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_UP and dirs[pg.K_UP]:
                    snek_dir = (0, -TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 0, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_DOWN and dirs[pg.K_s]:
                    snek_dir = (0, TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 0, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_LEFT and dirs[pg.K_a]:
                    snek_dir = (-TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 0}
                elif event.key == pg.K_RIGHT and dirs[pg.K_d]:
                    snek_dir = (TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 0, pg.K_RIGHT: 1}
                elif event.key == pg.K_ESCAPE:
                    MainMenu()
                elif event.key == pg.K_p:
                    PAUSETEXT = get_font(75).render('PAUSED', True, 'White')
                    PAUSERECT = PAUSETEXT.get_rect(center=(640, 50))
                    snek_dir = (0, 0)
                    SCREEN.blit(PAUSETEXT, PAUSERECT)
        SCREEN.fill('blue')
        #check borders and selfeatingas while as working collisions
        self_eating = pg.Rect.collidelist(snek, segments[:-1]) != -1
        if snek.left < 0 or snek.right > WINDOW or snek.top < 0 or snek.bottom > HEIGHT or self_eating:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center, blok5.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()            
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center or blok5.center:
                blok1.center, blok2.center, blok3.center, blok4.center, blok5.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0, 0)
            segments = [snek.copy()]
            recent_score = current_score
            current_score = 0
            COLLIDE.play()
        elif food1.left < 0 or food1.right > WINDOW or food1.top < 0 or food1.bottom > HEIGHT:
            food1.center = get_random_post()
        elif food2.left < 0 or food2.right > WINDOW or food2.top < 0 or food2.bottom > HEIGHT:
            food2.center = get_random_post()
        elif food3.left < 0 or food3.right > WINDOW or food3.top < 0 or food3.bottom > HEIGHT:
            food3.center = get_random_post()
        elif food4.left < 0 or food4.right > WINDOW or food4.top < 0 or food4.bottom > HEIGHT:
            food4.center = get_random_post()
        elif blok1.left < 0 or blok1.right > WINDOW or blok1.top < 0 or blok1.bottom > HEIGHT:
            blok1.center = get_random_post()
        elif blok2.left < 0 or blok2.right > WINDOW or blok2.top < 0 or blok2.bottom > HEIGHT:
            blok2.center = get_random_post()
        elif blok3.left < 0 or blok3.right > WINDOW or blok3.top < 0 or blok3.bottom > HEIGHT:
            blok3.center = get_random_post()
        elif blok4.left < 0 or blok4.right > WINDOW or blok4.top < 0 or blok4.bottom > HEIGHT:
            blok4.center = get_random_post()
        elif blok5.left < 0 or blok5.right > WINDOW or blok5.top < 0 or blok5.bottom > HEIGHT:
            blok5.center = get_random_post()
        elif snek.center == food1.center:
            food1.center = get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food2.center:
            food2.center = get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food3.center:
            food3.center = get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food4.center:
            food4.center = get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == blok1.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center, blok5.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center or blok5.center:
                blok1.center, blok2.center, blok3.center, blok4.center, blok5.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            COLLIDE.play()
        elif snek.center == blok2.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center, blok5.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center or blok5.center:
                blok1.center, blok2.center, blok3.center, blok4.center, blok5.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            COLLIDE.play()
        elif snek.center == blok3.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center, blok5.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center or blok5.center:
                blok1.center, blok2.center, blok3.center, blok4.center, blok5.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            COLLIDE.play()
        elif snek.center == blok4.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center, blok5.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center or blok5.center:
                blok1.center, blok2.center, blok3.center, blok4.center, blok5.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            COLLIDE.play()
        elif snek.center == blok5.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center, blok5.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center or blok5.center:
                blok1.center, blok2.center, blok3.center, blok4.center, blok5.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            COLLIDE.play()
        elif food1.center == blok1.center:
            food1.center = get_random_post()
        elif food1.center == blok2.center:
            food1.center = get_random_post()
        elif food1.center == blok3.center:
            food1.center = get_random_post()
        elif food1.center == blok4.center:
            food1.center = get_random_post()
        elif food1.center == blok5.center:
            food1.center = get_random_post()
            food1.center = get_random_post()
        elif food2.center == blok1.center:
            food2.center = get_random_post()
        elif food2.center == blok2.center:
            food2.center = get_random_post()
        elif food2.center == blok3.center:
            food2.center = get_random_post()
        elif food2.center == blok4.center:
            food2.center = get_random_post()
        elif food2.center == blok5.center:
            food2.center = get_random_post()
            food2.center = get_random_post()
        elif food3.center == blok1.center:
            food3.center = get_random_post()
        elif food3.center == blok2.center:
            food3.center = get_random_post()
        elif food3.center == blok3.center:
            food3.center = get_random_post()
        elif food3.center == blok4.center:
            food3.center = get_random_post()
        elif food3.center == blok5.center:
            food3.center = get_random_post()
            food3.center = get_random_post()
        elif food4.center == blok1.center:
            food4.center = get_random_post()
        elif food4.center == blok2.center:
            food4.center = get_random_post()
        elif food4.center == blok3.center:
            food4.center = get_random_post()
        elif food4.center == blok4.center:
            food4.center = get_random_post()
        elif food4.center == blok5.center:
            food4.center = get_random_post()
        #draw food
        pg.draw.rect(SCREEN, 'red', food1)
        pg.draw.rect(SCREEN, 'red', food2)
        pg.draw.rect(SCREEN, 'red', food3)
        pg.draw.rect(SCREEN, 'red', food4)
        #draw snek
        [pg.draw.rect(SCREEN, 'green', segment) for segment in segments]
        #draw bloks
        pg.draw.rect(SCREEN, 'yellow', blok1)
        pg.draw.rect(SCREEN, 'yellow', blok2)
        pg.draw.rect(SCREEN, 'yellow', blok3)
        pg.draw.rect(SCREEN, 'yellow', blok4)
        pg.draw.rect(SCREEN, 'yellow', blok5)
        #move snek
        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snek.move_ip(snek_dir)
            segments.append(snek.copy())
            segments = segments[-length:]
        score_surface = get_font(25).render(f"Current Score {current_score}  Last Score {recent_score}  High Score {high_score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(640, 680))
        SCREEN.blit(score_surface, score_rect)
        pg.display.flip()
        clock.tick(60)
def try_again_hard():
    while True:
        MUSIC1.play()
        SCREEN.fill((203, 12, 238))
        TRY_AGAIN_MOUSE_POS = pg.mouse.get_pos()
        TRY_AGAIN_TEXT = get_font(75).render('YOU DIED! TRY AGAIN?', True, (255, 255, 255))
        TRY_AGAIN_RECT = TRY_AGAIN_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(TRY_AGAIN_TEXT, TRY_AGAIN_RECT)
        #Buttons
        TRY_AGAIN_BUTTON = Button(image=None, pos=(500, 150),
                                text_input='TRY AGAIN', font=get_font(50), base_color=(255, 255, 255), hovering_color='Green')
        QUIT = Button(image=None, pos=(800, 150),
                    text_input='QUIT', font=get_font(50), base_color=(255, 255, 255), hovering_color='Green')
        for button in [TRY_AGAIN_BUTTON, QUIT]:
            button.changeColor(TRY_AGAIN_MOUSE_POS)
            button.update(SCREEN)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if TRY_AGAIN_BUTTON.checkForInput(TRY_AGAIN_MOUSE_POS):
                    hard()
                elif QUIT.checkForInput(TRY_AGAIN_MOUSE_POS):
                    MainMenu()
        pg.display.update()
def try_again_impos():
    while True:
        MUSIC1.play()
        SCREEN.fill((203, 12, 238))
        TRY_AGAIN_MOUSE_POS = pg.mouse.get_pos()
        TRY_AGAIN_TEXT = get_font(75).render('YOU DIED! TRY AGAIN?', True, (255, 255, 255))
        TRY_AGAIN_RECT = TRY_AGAIN_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(TRY_AGAIN_TEXT, TRY_AGAIN_RECT)
        #Buttons
        TRY_AGAIN_BUTTON = Button(image=None, pos=(500, 150),
                                text_input='TRY AGAIN', font=get_font(50), base_color=(255, 255, 255), hovering_color='Green')
        QUIT = Button(image=None, pos=(800, 150),
                    text_input='QUIT', font=get_font(50), base_color=(255, 255, 255), hovering_color='Green')
        for button in [TRY_AGAIN_BUTTON, QUIT]:
            button.changeColor(TRY_AGAIN_MOUSE_POS)
            button.update(SCREEN)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if TRY_AGAIN_BUTTON.checkForInput(TRY_AGAIN_MOUSE_POS):
                    impossable()
                elif QUIT.checkForInput(TRY_AGAIN_MOUSE_POS):
                    MainMenu()
        pg.display.update()
def impossable():
    MUSIC1.stop()
    pg.display.set_caption('SnekBloks')
    pg.font.init()
    WINDOW = 1280
    HEIGHT = 720
    TILE_SIZE = 50
    RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
    get_random_post = lambda: [randrange(*RANGE), randrange(*RANGE)]
    snek = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
    snek.center = get_random_post()
    length = 1
    segments = [snek.copy()]
    snek_dir = (0, 0)
    time, time_step = 0, 110
    food1 = snek.copy()
    food1.center = get_random_post()
    food2 = snek.copy()
    food2.center = get_random_post()
    food3 = snek.copy()
    food3.center = get_random_post()
    food4 = snek.copy()
    food4.center = get_random_post()
    clock = pg.time.Clock()
    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
    blok1 = snek.copy()
    blok1.center = get_random_post()
    blok2 = snek.copy()
    blok2.center = get_random_post()
    blok3 = snek.copy()
    blok3.center = get_random_post()
    blok4 = snek.copy()
    blok4.center = get_random_post()
    lifes = random.randint(1, 5)    
    def relocate_bloks():
        blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
    pg.time.set_timer(pg.USEREVENT + 1, 2000)
    #score variables
    current_score = 0
    high_score = 0
    recent_score = 0
    #snek
    while True:
        if current_score > high_score:
            high_score = current_score
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and dirs[pg.K_w]:
                    snek_dir = (0, -TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_s and dirs[pg.K_s]:
                    snek_dir = (0, TILE_SIZE)
                    dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_a and dirs[pg.K_a]:
                    snek_dir = (-TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_d and dirs[pg.K_d]:
                    snek_dir = (TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_UP and dirs[pg.K_UP]:
                    snek_dir = (0, -TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 0, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_DOWN and dirs[pg.K_s]:
                    snek_dir = (0, TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 0, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_LEFT and dirs[pg.K_a]:
                    snek_dir = (-TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 0}
                elif event.key == pg.K_RIGHT and dirs[pg.K_d]:
                    snek_dir = (TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 0, pg.K_RIGHT: 1}
                elif event.key == pg.K_ESCAPE:
                    MainMenu()
                elif event.key == pg.K_SPACE:
                    snek_dir = (0, 0)
                elif event.key == pg.K_h and current_score >= 10:
                    lifes += 1
                    current_score -= 10
                    length -= 10
            elif event.type == pg.USEREVENT + 1:
                relocate_bloks()
        SCREEN.fill('blue')
        if current_score >= 10:
            addhealthtext = get_font(25).render('Press H to add 1 life', True, (255, 255, 255))
            SCREEN.blit(addhealthtext, (25, 25))
        #check borders and selfeatingas while as working collisions
        self_eating = pg.Rect.collidelist(snek, segments[:-1]) != -1
        if snek.left < 0 or snek.right > WINDOW or snek.top < 0 or snek.bottom > HEIGHT or self_eating:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()            
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0, 0)
            segments = [snek.copy()]
            recent_score = current_score
            current_score = 0
            lifes -= 1
            COLLIDE.play()
        elif food1.left < 0 or food1.right > WINDOW or food1.top < 0 or food1.bottom > HEIGHT:
            food1.center = get_random_post()
        elif food2.left < 0 or food2.right > WINDOW or food2.top < 0 or food2.bottom > HEIGHT:
            food2.center = get_random_post()
        elif food3.left < 0 or food3.right > WINDOW or food3.top < 0 or food3.bottom > HEIGHT:
            food3.center = get_random_post()
        elif food4.left < 0 or food4.right > WINDOW or food4.top < 0 or food4.bottom > HEIGHT:
            food4.center = get_random_post()
        elif blok1.left < 0 or blok1.right > WINDOW or blok1.top < 0 or blok1.bottom > HEIGHT:
            blok1.center = get_random_post()
        elif blok2.left < 0 or blok2.right > WINDOW or blok2.top < 0 or blok2.bottom > HEIGHT:
            blok2.center = get_random_post()
        elif blok3.left < 0 or blok3.right > WINDOW or blok3.top < 0 or blok3.bottom > HEIGHT:
            blok3.center = get_random_post()
        elif blok4.left < 0 or blok4.right > WINDOW or blok4.top < 0 or blok4.bottom > HEIGHT:
            blok4.center = get_random_post()
        elif snek.center == food1.center:
            food1.center = get_random_post()
            blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food2.center:
            food2.center = get_random_post()
            blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food3.center:
            food3.center = get_random_post()
            blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food4.center:
            food4.center = get_random_post()
            blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == blok1.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            lifes -= 1
            COLLIDE.play()
        elif snek.center == blok2.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            lifes -= 1
            COLLIDE.play()
        elif snek.center == blok3.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            lifes -= 1
            COLLIDE.play()
        elif snek.center == blok4.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center, = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            lifes -= 1
            COLLIDE.play()
        elif food1.center == blok1.center:
            food1.center = get_random_post()
        elif food1.center == blok2.center:
            food1.center = get_random_post()
        elif food1.center == blok3.center:
            food1.center = get_random_post()
        elif food1.center == blok4.center:
            food1.center = get_random_post()
        elif food2.center == blok1.center:
            food2.center = get_random_post()
        elif food2.center == blok2.center:
            food2.center = get_random_post()
        elif food2.center == blok3.center:
            food2.center = get_random_post()
        elif food2.center == blok4.center:
            food2.center = get_random_post()
        elif food3.center == blok1.center:
            food3.center = get_random_post()
        elif food3.center == blok2.center:
            food3.center = get_random_post()
        elif food3.center == blok3.center:
            food3.center = get_random_post()
        elif food3.center == blok4.center:
            food3.center = get_random_post()
        elif food4.center == blok1.center:
            food4.center = get_random_post()
        elif food4.center == blok2.center:
            food4.center = get_random_post()
        elif food4.center == blok3.center:
            food4.center = get_random_post()
        elif food4.center == blok4.center:
            food4.center = get_random_post()
        
        elif lifes < 1:
            try_again_impos()
        #draw food
        pg.draw.rect(SCREEN, 'red', food1)
        pg.draw.rect(SCREEN, 'red', food2)
        pg.draw.rect(SCREEN, 'red', food3)
        pg.draw.rect(SCREEN, 'red', food4)
        #draw snek
        [pg.draw.rect(SCREEN, 'green', segment) for segment in segments]
        #draw bloks
        pg.draw.rect(SCREEN, 'yellow', blok1)
        pg.draw.rect(SCREEN, 'yellow', blok2)
        pg.draw.rect(SCREEN, 'yellow', blok3)
        pg.draw.rect(SCREEN, 'yellow', blok4)
        #move snek
        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snek.move_ip(snek_dir)
            segments.append(snek.copy())
            segments = segments[-length:]
        score_surface = get_font(25).render(f"Current Score {current_score}  Last Score {recent_score}  High Score {high_score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(640, 680))
        life_counter = get_font(25).render(f'Lifes {lifes}', True, 'White')
        SCREEN.blit(score_surface, score_rect)
        SCREEN.blit(life_counter, (20, 680))
        pg.display.flip()
        clock.tick(60)
def hard():    
    MUSIC1.stop()
    HARD_MOUSE_POS = pg.mouse.get_pos()
    pg.display.set_caption('SnekBloks')
    pg.font.init()
    WINDOW = 1280
    HEIGHT = 720
    TILE_SIZE = 50
    RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
    get_random_post = lambda: [randrange(*RANGE), randrange(*RANGE)]
    snek = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
    snek.center = get_random_post()
    length = 1
    segments = [snek.copy()]
    snek_dir = (0, 0)
    time, time_step = 0, 110
    food1 = snek.copy()
    food1.center = get_random_post()
    food2 = snek.copy()
    food2.center = get_random_post()
    food3 = snek.copy()
    food3.center = get_random_post()
    food4 = snek.copy()
    food4.center = get_random_post()
    clock = pg.time.Clock()
    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
    blok1 = snek.copy()
    blok1.center = get_random_post()
    blok2 = snek.copy()
    blok2.center = get_random_post()
    blok3 = snek.copy()
    blok3.center = get_random_post()
    blok4 = snek.copy()
    blok4.center = get_random_post()
    lifes = random.randint(1, 5)  
    #score variables
    current_score = 0
    high_score = 0
    recent_score = 0
    #snek
    while True:
        if current_score > high_score:
            high_score = current_score
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and dirs[pg.K_w]:
                    snek_dir = (0, -TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_s and dirs[pg.K_s]:
                    snek_dir = (0, TILE_SIZE)
                    dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_a and dirs[pg.K_a]:
                    snek_dir = (-TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_d and dirs[pg.K_d]:
                    snek_dir = (TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_UP and dirs[pg.K_UP]:
                    snek_dir = (0, -TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 0, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_DOWN and dirs[pg.K_s]:
                    snek_dir = (0, TILE_SIZE)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 0, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
                elif event.key == pg.K_LEFT and dirs[pg.K_a]:
                    snek_dir = (-TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 0}
                elif event.key == pg.K_RIGHT and dirs[pg.K_d]:
                    snek_dir = (TILE_SIZE, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1, pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 0, pg.K_RIGHT: 1}
                elif event.key == pg.K_ESCAPE:
                    MainMenu()
                elif event.key == pg.K_SPACE:
                    snek_dir = (0, 0)
                elif event.key == pg.K_h and current_score >= 10:
                    lifes += 1
                    current_score -= 10
                    length -= 10
        SCREEN.fill('blue')
        if current_score >= 10:
            addhealthtext = get_font(25).render('Press H to add 1 life', True, (255, 255, 255))
            SCREEN.blit(addhealthtext, (25, 25))
        #check borders and selfeatingas while as working collisions
        self_eating = pg.Rect.collidelist(snek, segments[:-1]) != -1
        if snek.left < 0 or snek.right > WINDOW or snek.top < 0 or snek.bottom > HEIGHT or self_eating:
            blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            snek.center = get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            food1.center, food2.center, food3.center, food4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()            
            length, snek_dir = 1, (0, 0)
            segments = [snek.copy()]
            recent_score = current_score
            current_score = 0
            lifes -= 1
            COLLIDE.play()
        elif food1.left < 0 or food1.right > WINDOW or food1.top < 0 or food1.bottom > HEIGHT:
            food1.center = get_random_post()
        elif food2.left < 0 or food2.right > WINDOW or food2.top < 0 or food2.bottom > HEIGHT:
            food2.center = get_random_post()
        elif food3.left < 0 or food3.right > WINDOW or food3.top < 0 or food3.bottom > HEIGHT:
            food3.center = get_random_post()
        elif food4.left < 0 or food4.right > WINDOW or food4.top < 0 or food4.bottom > HEIGHT:
            food4.center = get_random_post()
        elif blok1.left < 0 or blok1.right > WINDOW or blok1.top < 0 or blok1.bottom > HEIGHT:
            blok1.center = get_random_post()
        elif blok2.left < 0 or blok2.right > WINDOW or blok2.top < 0 or blok2.bottom > HEIGHT:
            blok2.center = get_random_post()
        elif blok3.left < 0 or blok3.right > WINDOW or blok3.top < 0 or blok3.bottom > HEIGHT:
            blok3.center = get_random_post()
        elif blok4.left < 0 or blok4.right > WINDOW or blok4.top < 0 or blok4.bottom > HEIGHT:
            blok4.center = get_random_post()
        elif snek.center == food1.center:
            food1.center = get_random_post()
            blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food2.center:
            food2.center = get_random_post()
            blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food3.center:
            food3.center = get_random_post()
            blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:    
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == food4.center:
            food4.center = get_random_post()
            blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length += 1
            current_score += 1
            APPLE.play()
        elif snek.center == blok1.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            lifes -= 1
            COLLIDE.play()
        elif snek.center == blok2.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            lifes -= 1
            COLLIDE.play()
        elif snek.center == blok3.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            lifes -= 1
            COLLIDE.play()
        elif snek.center == blok4.center:
            snek.center, food1.center, food2.center, food3.center, food4.center, blok1.center, blok2.center, blok3.center, blok4.center, = get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post(), get_random_post()
            if snek.center == blok1.center or blok2.center or blok3.center or blok4.center:
                blok1.center, blok2.center, blok3.center, blok4.center = get_random_post(), get_random_post(), get_random_post(), get_random_post()
            length, snek_dir = 1, (0,0)
            recent_score = current_score
            current_score = 0
            lifes -= 1
            COLLIDE.play()
        elif food1.center == blok1.center:
            food1.center = get_random_post()
        elif food1.center == blok2.center:
            food1.center = get_random_post()
        elif food1.center == blok3.center:
            food1.center = get_random_post()
        elif food1.center == blok4.center:
            food1.center = get_random_post()
        elif food2.center == blok1.center:
            food2.center = get_random_post()
        elif food2.center == blok2.center:
            food2.center = get_random_post()
        elif food2.center == blok3.center:
            food2.center = get_random_post()
        elif food2.center == blok4.center:
            food2.center = get_random_post()
        elif food3.center == blok1.center:
            food3.center = get_random_post()
        elif food3.center == blok2.center:
            food3.center = get_random_post()
        elif food3.center == blok3.center:
            food3.center = get_random_post()
        elif food3.center == blok4.center:
            food3.center = get_random_post()
        elif food4.center == blok1.center:
            food4.center = get_random_post()
        elif food4.center == blok2.center:
            food4.center = get_random_post()
        elif food4.center == blok3.center:
            food4.center = get_random_post()
        elif food4.center == blok4.center:
            food4.center = get_random_post()
        elif lifes < 1:
            try_again_hard()
        #draw food
        pg.draw.rect(SCREEN, 'red', food1)
        pg.draw.rect(SCREEN, 'red', food2)
        pg.draw.rect(SCREEN, 'red', food3)
        pg.draw.rect(SCREEN, 'red', food4)
        #draw snek
        [pg.draw.rect(SCREEN, 'green', segment) for segment in segments]
        #draw bloks
        pg.draw.rect(SCREEN, 'yellow', blok1)
        pg.draw.rect(SCREEN, 'yellow', blok2)
        pg.draw.rect(SCREEN, 'yellow', blok3)
        pg.draw.rect(SCREEN, 'yellow', blok4)
        #move snek
        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snek.move_ip(snek_dir)
            segments.append(snek.copy())
            segments = segments[-length:]
        score_surface = get_font(25).render(f"Current Score {current_score}  Last Score {recent_score}  High Score {high_score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(640, 680))
        life_counter = get_font(25).render(f'Lifes {lifes}', True, 'White')
        SCREEN.blit(score_surface, score_rect)
        SCREEN.blit(life_counter, (20, 680))
        pg.display.flip()
        clock.tick(60)
def Controls():
    while True:
        MUSIC1.play()
        CONTROLS_MOUSE_POS = pg.mouse.get_pos()
        SCREEN.fill('Black')
        CONTROLSTEXT = get_font(75).render('CONTROLS', True, (255, 255, 255))
        CONTROLSRECT = CONTROLSTEXT.get_rect(center=(640, 50))
        SCREEN.blit(CONTROLSTEXT, CONTROLSRECT)
        UPTEXT = get_font(30).render('UP - W or Up Arrow', True, 'White')
        UPRECT = UPTEXT.get_rect(center=(640, 150))
        SCREEN.blit(UPTEXT, UPRECT)
        DOWNTEXT = get_font(30).render('DOWN - S or Down Arrow', True, 'White')
        DOWNRECT = DOWNTEXT.get_rect(center=(640, 200))
        SCREEN.blit(DOWNTEXT, DOWNRECT)
        LEFTTEXT = get_font(30).render('LEFT - A or Left Arrow', True, 'White')
        LEFTRECT = LEFTTEXT.get_rect(center=(640, 250))
        SCREEN.blit(LEFTTEXT, LEFTRECT)
        RIGHTTEXT = get_font(30).render('RIGHT - D or Right Arrow', True, 'White')
        RIGHTRECT = UPTEXT.get_rect(center=(565, 300))
        SCREEN.blit(RIGHTTEXT, RIGHTRECT)
        #button
        BACK = Button(image=None, pos=(640, 650),
                      text_input='BACK', font=get_font(50), base_color='White', hovering_color='Green')
        for button in [BACK]:
            button.changeColor(CONTROLS_MOUSE_POS)
            button.update(SCREEN)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if BACK.checkForInput(CONTROLS_MOUSE_POS):
                    options()
        pg.display.update()
def volume():
    while True:
        MUSIC1.play()
        VOLUME_MOUSE_POS = pg.mouse.get_pos()
        SCREEN.fill('Black')

        VOLUME_TEXT = get_font(75).render('VOLUME', True, 'White')
        VOLUME_RECT = VOLUME_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(VOLUME_TEXT, VOLUME_RECT)

        FULL = Button(image=None, pos=(640, 150),
                      text_input='100%', font=get_font(50), base_color='White', hovering_color='Green')
        THREEQUARTERS = Button(image=None, pos=(640, 250),
                               text_input='75%', font=get_font(50), base_color='White', hovering_color='Green')
        HALF =  Button(image=None, pos=(640, 350),
                       text_input='50%', font=get_font(50), base_color='White', hovering_color='Green')
        ONEQUARTER = Button(image=None, pos=(640, 450),
                            text_input='25%', font=get_font(50), base_color='White', hovering_color='Green')
        ZERO = Button(image=None, pos=(640, 550),
                      text_input='0%', font=get_font(50), base_color='White', hovering_color='Green')
        BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")
        for button in [FULL, THREEQUARTERS, HALF, ONEQUARTER, ZERO, BACK]:
            button.changeColor(VOLUME_MOUSE_POS)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    options()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if FULL.checkForInput(VOLUME_MOUSE_POS):
                    APPLE.set_volume(1)
                    COLLIDE.set_volume(1)
                    MUSIC1.set_volume(1)
                elif THREEQUARTERS.checkForInput(VOLUME_MOUSE_POS):
                    APPLE.set_volume(0.75)
                    COLLIDE.set_volume(0.75)
                    MUSIC1.set_volume(0.75)
                elif HALF.checkForInput(VOLUME_MOUSE_POS):
                    APPLE.set_volume(0.5)
                    COLLIDE.set_volume(0.5)
                    MUSIC1.set_volume(0.5)
                elif ONEQUARTER.checkForInput(VOLUME_MOUSE_POS):
                    APPLE.set_volume(0.25)
                    COLLIDE.set_volume(0.25)
                    MUSIC1.set_volume(0.25)
                elif ZERO.checkForInput(VOLUME_MOUSE_POS):
                    APPLE.set_volume(0)
                    COLLIDE.set_volume(0)
                    MUSIC1.set_volume(0)
                elif BACK.checkForInput(VOLUME_MOUSE_POS):
                    options()
        pg.display.update()
def options():
     while True:
        MUSIC1.play()
        OPTIONS_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.fill("Black")

        OPTIONS_TEXT = get_font(75).render("OPTIONS", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        #buttons
        OPTIONS_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")
        FULLSCREEN = Button(image=None, pos=(640, 150),
                            text_input='FULLSCREEN', font=get_font(50), base_color='White', hovering_color='Green')
        CONTROLS = Button(image=None, pos=(640, 250),
                          text_input='CONTROLS', font=get_font(50), base_color=(255, 255, 255), hovering_color="Green")
        HELP_BUTTON = Button(image=None, pos=(640, 350),
                             text_input='HELP', font=get_font(50), base_color='White', hovering_color='Green')
        VOLUME_BUTTON = Button(image=None, pos=(640, 450),
                               text_input='VOLUME', font=get_font(50), base_color='White', hovering_color='Green')

        for button in [OPTIONS_BACK, FULLSCREEN, CONTROLS, HELP_BUTTON, VOLUME_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    MainMenu()
                elif FULLSCREEN.checkForInput(OPTIONS_MOUSE_POS):
                    Fullscreen()
                elif CONTROLS.checkForInput(OPTIONS_MOUSE_POS):
                    Controls()
                elif HELP_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    help()
                elif VOLUME_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    volume()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    MainMenu()

        pg.display.update()
def credits():
    while True:    
        MUSIC1.play()
        CREDITS_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.fill('Black')

        CREDITS_TEXT = get_font(75).render('CREDITS', True, 'White')
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)
        LEAD_DEV_TEXT = get_font(50).render('Lead Developer', True, 'White')
        LEAD_DEV_NAME_TEXT = get_font(50).render('Void0717', True, 'White')
        LEAD_DEV_NAME_RECT = LEAD_DEV_NAME_TEXT.get_rect(center=(640, 200))
        LEAD_DEV_RECT = LEAD_DEV_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(LEAD_DEV_TEXT, LEAD_DEV_RECT)
        SCREEN.blit(LEAD_DEV_NAME_TEXT, LEAD_DEV_NAME_RECT)
        BUTTON_TEXT = get_font(50).render('Button Script', True, 'White')
        BUTTON_NAME = get_font(50).render('Baraltech on YouTube', True, 'White')
        BUTTON_RECT = BUTTON_TEXT.get_rect(center=(640, 250))
        BUTTON_NAME_RECT = BUTTON_NAME.get_rect(center=(640, 300))
        SCREEN.blit(BUTTON_TEXT, BUTTON_RECT)
        SCREEN.blit(BUTTON_NAME, BUTTON_NAME_RECT)
        #buttons
        BACK = Button(image=None, pos=(640, 650),
                    text_input='BACK', font=get_font(75), base_color='White', hovering_color='Green')
        for button in [BACK]:
            button.changeColor(CREDITS_MOUSE_POS)
            button.update(SCREEN)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if BACK.checkForInput(CREDITS_MOUSE_POS):
                    MainMenu()
        pg.display.update()
def impos_check():
   while True:
        MUSIC1.play()
        SCREEN.fill('Black')
        HARD_CHECK_MOUSE_POS = pg.mouse.get_pos()
        HARD_CHECK_TEXT = get_font(75).render('ARE YOU SURE?', True, 'White')
        SECOND_LINE = get_font(75).render('ITS IMPOSSIBLE!', True, 'White')
        SECOND_RECT = SECOND_LINE.get_rect(center=(640, 150))
        HARD_CHECK_RECT = HARD_CHECK_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(HARD_CHECK_TEXT, HARD_CHECK_RECT)
        SCREEN.blit(SECOND_LINE, SECOND_RECT)

        YES = Button(image=None, pos=(540, 250),
                    text_input='YES', font=get_font(50), base_color='White', hovering_color='Green')
        NO = Button(image=None, pos=(740, 250),
                    text_input='NO', font=get_font(50), base_color='White', hovering_color='Green')

        for button in [YES, NO]:
            button.changeColor(HARD_CHECK_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if YES.checkForInput(HARD_CHECK_MOUSE_POS):
                    impossable()
                elif NO.checkForInput(HARD_CHECK_MOUSE_POS):
                    MainMenu()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    diff_select()
        pg.display.update()
def hard_check():
    while True:
        MUSIC1.play()
        SCREEN.fill('Black')
        HARD_CHECK_MOUSE_POS = pg.mouse.get_pos()
        HARD_CHECK_TEXT = get_font(75).render('ARE YOU SURE?', True, 'White')
        SECOND_LINE = get_font(75).render('ITS HARD!', True, 'White')
        SECOND_RECT = SECOND_LINE.get_rect(center=(640, 150))
        HARD_CHECK_RECT = HARD_CHECK_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(HARD_CHECK_TEXT, HARD_CHECK_RECT)
        SCREEN.blit(SECOND_LINE, SECOND_RECT)

        YES = Button(image=None, pos=(540, 250),
                    text_input='YES', font=get_font(55), base_color='White', hovering_color='Green')
        NO = Button(image=None, pos=(740, 250),
                    text_input='NO', font=get_font(55), base_color='White', hovering_color='Green')

        for button in [YES, NO]:
            button.changeColor(HARD_CHECK_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if YES.checkForInput(HARD_CHECK_MOUSE_POS):
                    hard()
                elif NO.checkForInput(HARD_CHECK_MOUSE_POS):
                    MainMenu()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    diff_select()
        pg.display.update()
def diff_select():
    while True:
        MUSIC1.play()
        SCREEN.fill('Black')
        DIFF_SELECT_MOUSE_POS = pg.mouse.get_pos()
        DIFF_SELECT_TEXT = get_font(75).render('DIFFICULTY SELECT', True, 'White')
        DIFF_SELECT_RECT = DIFF_SELECT_TEXT.get_rect(center=(640, 50))
        PEACEFULL_BUTTON = Button(image=None, pos=(640, 150),
                                  text_input='PEACEFULL', font=get_font(50), base_color='White', hovering_color='Green')        
        EASY_BUTTON = Button(image=None, pos=(640, 250),
                                  text_input='Easy', font=get_font(50), base_color='White', hovering_color='Green')
        NORMAL_BUTTON = Button(image=None, pos=(640, 350),
                            text_input='NORMAL', font=get_font(50), base_color='White', hovering_color='Green')
        HARD_BUTTON = Button(image=None, pos=(640, 450),
                            text_input='HARD', font=get_font(50), base_color='White', hovering_color='Green')
        IMPOSSIBLE_BUTTON = Button(image=None, pos=(640, 550),
                                   text_input='IMPOSSIBLE', font=get_font(50), base_color='White', hovering_color='Green')
        BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")
        SCREEN.blit(DIFF_SELECT_TEXT, DIFF_SELECT_RECT)
        for button in [PEACEFULL_BUTTON ,EASY_BUTTON, NORMAL_BUTTON, HARD_BUTTON, IMPOSSIBLE_BUTTON, BACK]:
            button.changeColor(DIFF_SELECT_MOUSE_POS)
            button.update(SCREEN)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit
            elif event.type == pg.MOUSEBUTTONDOWN:
                if PEACEFULL_BUTTON.checkForInput(DIFF_SELECT_MOUSE_POS):
                    peacefull()
                elif EASY_BUTTON.checkForInput(DIFF_SELECT_MOUSE_POS):
                    easy()
                elif NORMAL_BUTTON.checkForInput(DIFF_SELECT_MOUSE_POS):
                    normal()
                elif HARD_BUTTON.checkForInput(DIFF_SELECT_MOUSE_POS):
                    hard_check()
                elif IMPOSSIBLE_BUTTON.checkForInput(DIFF_SELECT_MOUSE_POS):
                    impos_check()
                elif BACK.checkForInput(DIFF_SELECT_MOUSE_POS):
                    MainMenu()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    MainMenu()
        pg.display.update()
def help():
    while True:
        MUSIC1.play()
        HELP_MOUSE_POS = pg.mouse.get_pos()
        SCREEN.fill('Black')
        TITLE = get_font(75).render('Help', True, 'White')
        TITLERECT = TITLE.get_rect(center=(640, 50))
        SCREEN.blit(TITLE, TITLERECT)
        TEXT1 = get_font(19).render('Welcome to SnekBloks.', True, 'White')
        TEXT2 = get_font(19).render('Your goal is to eat as many apples as possible without colliding with a block.', True, 'White')
        TEXT3 = get_font(19).render('On the harder modes you have a limited number of lives and the blocks move', True, 'White')
        TEXT4 = get_font(19).render('Have Fun!', True, 'White')
        RECT1 = TEXT1.get_rect(center=(640, 200))
        RECT2 = TEXT2.get_rect(center=(640, 250))
        RECT3 = TEXT3.get_rect(center=(640, 300))
        RECT4 = TEXT4.get_rect(center=(640, 350))
        SCREEN.blit(TEXT1, RECT1)
        SCREEN.blit(TEXT2, RECT2)
        SCREEN.blit(TEXT3, RECT3)
        SCREEN.blit(TEXT4, RECT4)
        BACK = Button(image=None, pos=(640, 650),
                      text_input='Back', font=get_font(55), base_color='White', hovering_color='Green')
        for button in [BACK]:
            button.changeColor(HELP_MOUSE_POS)
            button.update(SCREEN)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    options()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if BACK.checkForInput(HELP_MOUSE_POS):
                    options()
        pg.display.update()
def MainMenu():
    while True:
        MUSIC1.play()
        SCREEN.blit(BG, (0, 0))
        version = get_font(35).render('V 0.11.0', True, 'White')
        versionrect = version.get_rect(center =(1162, 700))
        SCREEN.blit(version, versionrect)
        #draws a snek on main menu
        snekpiece = pg.image.load('assets/Snek Piece.png')
        SCREEN.blit(snekpiece, (50, 200))
        SCREEN.blit(snekpiece, (50, 255))
        SCREEN.blit(snekpiece, (50, 310))
        SCREEN.blit(snekpiece, (50, 365))
        SCREEN.blit(snekpiece, (50, 420))
        SCREEN.blit(snekpiece, (105, 420))
        MENU_MOUSE_POS = pg.mouse.get_pos()
        #draws apples on main menu
        apple = pg.image.load('assets/Apple.png')
        SCREEN.blit(apple, (1000, 300))
        SCREEN.blit(apple, (500, 630))
        SCREEN.blit(apple, (100, 500))
        SCREEN.blit(apple, (300, 80))
        #draws bloks on the main menu
        blok = pg.image.load('assets/Blok.png')
        SCREEN.blit(blok, (900, 400))
        SCREEN.blit(blok, (200, 550))
        SCREEN.blit(blok, (100, 880))
        SCREEN.blit(blok, (10, 10))
        SCREEN.blit(blok, (100, 90))

        MENU_TEXT1 = get_font(75).render("SNEKBL KS", True, "Green")
        MENU_TEXT2 = get_font(75).render("      O  ", True, "Red")
        MENU_RECT1 = MENU_TEXT1.get_rect(center=(640, 100))
        MENU_RECT2 = MENU_TEXT2.get_rect(center=(640, 100))
        NAME_TEXT1 = get_font(55).render('By Void 717', True, 'Green')
        NAME_TEXT2 = get_font(55).render('       O   ', True, 'Red')
        NAME_RECT1 = NAME_TEXT1.get_rect(center=(640, 160))
        NAME_RECT2 = NAME_TEXT2.get_rect(center=(640, 160))
        SCREEN.blit(MENU_TEXT1, MENU_RECT1)
        SCREEN.blit(MENU_TEXT2, MENU_RECT2)
        SCREEN.blit(NAME_TEXT1, NAME_RECT1)
        SCREEN.blit(NAME_TEXT2, NAME_RECT2)
        
        PLAY_BUTTON = Button(image=None, pos=(640, 250), 
                            text_input="PLAY", font=get_font(50), base_color="White", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 350),
                            text_input='OPTIONS', font=get_font(50), base_color='White', hovering_color='Green')
        CREDITS = Button(image=None, pos=(640, 450),
                        text_input='CREDITS', font=get_font(50), base_color='White', hovering_color='Green')
        QUIT_BUTTON = Button(image=None, pos=(640, 550), 
                            text_input="QUIT", font=get_font(50), base_color="White", hovering_color="Green")


        for button in [PLAY_BUTTON, OPTIONS_BUTTON, CREDITS, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    diff_select()
                elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                elif CREDITS.checkForInput(MENU_MOUSE_POS):
                    credits()
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit()

        pg.display.update()
def Loading():
    randtime = random.randint(0, 3)
    times = 3
    randinc = random.randint(1, 400)
    
    # Define loading bar properties
    loading_bar_width = 800
    loading_bar_height = 50
    loading_bar_x = 220
    loading_bar_y = 420
    loading_progress = 0

    loading_bar_width_increment = loading_bar_width // randinc

    while True:
        SCREEN.blit(BG, (0, 0))
        LOADING_TEXT1 = get_font(75).render("SNEKBL KS", True, "Green")
        LOADING_TEXT2 = get_font(75).render("      O  ", True, "Red")
        LOADING_RECT1 = LOADING_TEXT1.get_rect(center=(640, 300))
        LOADING_RECT2 = LOADING_TEXT2.get_rect(center=(640, 300))
        NAME_TEXT1 = get_font(55).render('By Void 717', True, 'Green')
        NAME_TEXT2 = get_font(55).render('       O   ', True, 'Red')
        NAME_RECT1 = NAME_TEXT1.get_rect(center=(640, 360))
        NAME_RECT2 = NAME_TEXT2.get_rect(center=(640, 360))
        SCREEN.blit(LOADING_TEXT1, LOADING_RECT1)
        SCREEN.blit(LOADING_TEXT2, LOADING_RECT2)
        SCREEN.blit(NAME_TEXT1, NAME_RECT1)
        SCREEN.blit(NAME_TEXT2, NAME_RECT2)

        # Update the loading bar
        loading_progress += loading_bar_width_increment

        # Draw the loading bar
        loading_bar_rect = pg.Rect(loading_bar_x, loading_bar_y, loading_progress, loading_bar_height)
        pg.draw.rect(SCREEN, "green", loading_bar_rect)

        if loading_progress >= loading_bar_width:
            MainMenu()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
        
        pg.display.update()
Loading()