import os

import pygame, sys

pygame.init()  # initializes the Pygame
import random
import math
import time

screen = pygame.display.set_mode((798, 600))
pygame.mixer.init()
pygame.display.set_caption('Racing Game: Python Version')
logo = pygame.image.load('Assets/Logo.png')
pygame.display.set_icon(logo)

# MAKING INTRO SCREEEN
IntroFont = pygame.font.Font("freesansbold.ttf", 38)


def introImg(x, y):
    intro = pygame.image.load("Assets/Intro.png")

    screen.blit(intro, (x, y))


def instructionIMG(x, y):
    instruct = pygame.image.load("Assets/Instructions.jpg")
    run = True
    while run:
        screen.blit(instruct, (x, y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def aboutIMG(x, y):
    aboutimg = pygame.image.load("Assets/About.jpg")
    run = True
    while run:
        screen.blit(aboutimg, (x, y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def play(x, y):
    playtext = IntroFont.render("PLAY", True, (255, 0, 0))
    screen.blit(playtext, (x, y))


def ABOUT(x, y):
    aboutText = IntroFont.render("ABOUT", True, (255, 0, 0))
    screen.blit(aboutText, (x, y))


def Instruction(x, y):
    instructionText = IntroFont.render("INSTRUCTION", True, (255, 0, 0))
    screen.blit(instructionText, (x, y))


def introscreen():
    global click
    run = True
    pygame.mixer.music.load('Assets/Audio/Intro.mp3')
    pygame.mixer.music.play(-1)
    while run:
        screen.fill((0, 0, 0))
        introImg(0, 0)
        play(100, 450)
        Instruction(280, 450)
        ABOUT(615, 450)

        # getting coordinates of mouse cursor
        x, y = pygame.mouse.get_pos()

        # storing rectangle coordinates (x, y, length, height) by making variables
        button1 = pygame.Rect(60, 440, 175, 50)
        button2 = pygame.Rect(265, 440, 300, 50)
        button3 = pygame.Rect(600, 440, 165, 50)

        # Drawing rectangles with stored coorditates of rectangles
        pygame.draw.rect(screen, (255, 255, 255), button1, 6)
        pygame.draw.rect(screen, (255, 255, 255), button2, 6)
        pygame.draw.rect(screen, (255, 255, 255), button3, 6)

        # if our cursor is on button1 which is PLAY button
        if button1.collidepoint(x, y):
            pygame.draw.rect(screen, (155, 0, 0), button1, 6)
            if click:
                pygame.mixer.music.stop()
                countdown()  # CALLING COUNTDOWN FUNCTION TO START OUR GAME


        # if our cursor is on button2 which is INSTRUCTION button
        if button2.collidepoint(x, y):
            pygame.draw.rect(screen, (155, 0, 0), button2, 6)
            if click:
                instructionIMG(0, 0)  # DISPLAYING OUR INSTRUCTION IMAGE BY CALLING IT

        # if our cursor is on button3 which is ABOUT button
        if button3.collidepoint(x, y):
            pygame.draw.rect(screen, (155, 0, 0), button3, 6)
            if click:
                aboutIMG(0, 0)  # DISPLAYING OUR ABOUT IMAGE BY CALLING IT

        # checking for mouse click event
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


# Countdown
def countdown():
    font2 = pygame.font.Font('freesansbold.ttf', 85)
    countdownBacground = pygame.image.load('Assets/BG.png')
    three = font2.render('3', True, (187, 30, 16))
    two = font2.render('2', True, (255, 255, 0))
    one = font2.render('1', True, (51, 165, 50))
    go = font2.render('GO!!!', True, (0, 255, 0))

    # displaying blank background
    screen.blit(countdownBacground, (0, 0))
    pygame.display.update()

    # 3
    screen.blit(three, (350, 250))
    pygame.mixer.music.load("Assets/Audio/3.mp3")
    pygame.mixer.music.set_volume(3)
    pygame.mixer.music.play()
    pygame.display.update()
    time.sleep(1)

    # wait
    screen.blit(countdownBacground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    # 2
    screen.blit(two, (350, 250))
    pygame.mixer.music.load("Assets/Audio/2.mp3")
    pygame.mixer.music.set_volume(3)
    pygame.mixer.music.play()
    pygame.display.update()
    time.sleep(1)

    # wait
    screen.blit(countdownBacground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    # 1
    screen.blit(one, (350, 250))
    pygame.mixer.music.load("Assets/Audio/1.mp3")
    pygame.mixer.music.set_volume(3)
    pygame.mixer.music.play()
    pygame.display.update()
    time.sleep(1)

    # wait
    screen.blit(countdownBacground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    # GO!!
    screen.blit(go, (300, 250))
    pygame.mixer.music.load("Assets/Audio/Go.mp3")
    pygame.mixer.music.set_volume(3)
    pygame.mixer.music.play()
    pygame.display.update()
    time.sleep(1)
    gameloop()  # calling the gamloop
    pygame.display.update()

# List of music files
music_files = ['Assets/Audio/Music1.mp3',
               'Assets/Audio/Music2.mp3',
               'Assets/Audio/Music3.mp3',]

DECREASE_SPEED_EVENT = pygame.USEREVENT + 1

# gameloop function
def gameloop():
    # Selecting a random music file from the list
    music_file = random.choice(music_files)

    # music
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    # sound effect for collision
    crash_sound = pygame.mixer.Sound('Assets/Audio/crashSound.mp3')
    # speed of the car
    speedometer = 0
    pygame.time.set_timer(DECREASE_SPEED_EVENT, 1000)  # 1000 milliseconds = 1 second


    # scoring part
    score_value = 0
    font1 = pygame.font.Font("freesansbold.ttf", 25)

    # Load font and set font size
    font = pygame.font.Font("freesansbold.ttf", 13)

    # Render the text "Now Playing"
    song_name = os.path.basename(music_file).replace(".mp3", "")
    song_text = font.render(song_name, True, (255, 255, 255))


    def display_song_name(x, y):
        song = font.render(song_name, True, (0, 0, 128))
        screen.blit(song, (x, y))
        pygame.display.flip()

    def show_score(x, y):
        score = font1.render("SCORE: " + str(score_value), True, (255, 0, 0))
        screen.blit(score, (x, y))

    # highscore part
    with open("Assets/highscore.txt", "r") as f:
        highscore = f.read()

    def show_highscore(x, y):
        Hiscore_text = font1.render('HISCORE :' + str(highscore), True, (255, 0, 0))
        screen.blit(Hiscore_text, (x, y))
        pygame.display.update()

    def car_speed(x, y):
        speed_text = font1.render(f'Speed(KmPH): {speedometer} ', True, (255, 0, 0))
        screen.blit(speed_text, (x, y))
        pygame.display.flip()


    # gameover

    def gameover():
        gameoverImg = pygame.image.load("Assets/Game Over.jpg")
        run = True
        while run:

            screen.blit(gameoverImg,(0,0))
            time.sleep(0.5)
            show_score(330,400)
            time.sleep(0.5)
            show_highscore(330,450)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        countdown()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    # setting background image
    bg = pygame.image.load('Assets/BG.png')

    # setting our player
    maincar = pygame.image.load('Assets/Sprite/Car3.png')
    maincar_rotated = maincar.copy()
    maincar_angle = 0
    car_rect = maincar.get_rect(bottomleft=(350, 495))
    #define rotation function
    def rotate_car(maincar_angle):
        #rotate car surface and angle
        maincar_rotated = pygame.transform.rotate(maincar, maincar_angle)
        maincar_angle += 10
        if maincar_angle > 360:
            maincar_angle = 0
        return maincar_rotated, maincar_angle
    maincar_rect = maincar_rotated.get_rect(center=car_rect.center)
    maincarX = maincar_rect.centerx
    maincarY = maincar_rect.centery
    maincarX_change = 0
    maincarY_change = 0


    # other cars
    car1 = pygame.image.load('Assets/Sprite/Car1.png')
    car1_rect = car1.get_rect()
    car1X = random.randint(178, 490)
    car1Y = 100
    car1Ychange = 1

    car2 = pygame.image.load('Assets/Sprite/Car2.png')
    car2_rect = car2.get_rect()
    car2X = random.randint(178, 490)
    car2Y = 100
    car2Ychange = 1

    car3 = pygame.image.load('Assets/Sprite/Car4.png')
    car3_rect = car3.get_rect()
    car3X = random.randint(178, 490)
    car3Y = 100
    car3Ychange = 1

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == DECREASE_SPEED_EVENT:
                if speedometer > 0:
                    speedometer -= 1
                if speedometer < 0:
                    speedometer = 0
                if speedometer % 5 == 0:
                    car1Ychange -= 0.5
                    if car1Ychange < 1:
                        car1Ychange = 1
                    car2Ychange -= 0.5
                    if car2Ychange < 1:
                        car2Ychange = 1
                    car3Ychange -= 0.5
                    if car3Ychange < 1:
                        car3Ychange = 1


            # checking if any key has been pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    maincarX_change += 4
                    maincar_rotated, maincar_angle = rotate_car(-maincar_angle)

                if event.key == pygame.K_LEFT:
                    maincarX_change -= 4
                    maincar_rotated, maincar_angle = rotate_car(maincar_angle)


                if event.key == pygame.K_UP:
                    speedometer += 10
                    if speedometer > 100:
                        speedometer = 100
                    car1Ychange += 1
                    if car1Ychange > 10:
                        car1Ychange = 10
                    car2Ychange += 1
                    if car2Ychange > 10:
                        car2Ychange = 10
                    car3Ychange += 1
                    if car3Ychange > 10:
                        car3Ychange = 10

                if event.key == pygame.K_DOWN:
                    speedometer -= 10
                    if speedometer < 0:
                        speedometer = 0
                    car1Ychange -= 1
                    if car1Ychange < 1:
                        car1Ychange = 1
                    car2Ychange -= 1
                    if car2Ychange < 1:
                        car2Ychange = 1
                    car3Ychange -= 1
                    if car3Ychange < 1:
                        car3Ychange = 1

            # checking if key has been lifted up
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    maincarX_change = 0
                    maincar_rotated, maincar_angle = rotate_car(0)

                if event.key == pygame.K_LEFT:
                    maincarX_change = 0
                    maincar_rotated, maincar_angle = rotate_car(0)

                if event.key == pygame.K_UP:
                    speedometer += 0
                    if speedometer > 100:
                        speedometer = 100

                if event.key == pygame.K_DOWN:
                    speedometer -= 0
                    if speedometer < 0:
                        speedometer = 0

        # setting boundary for our main car
        if maincarX < 178:
            maincarX = 178
        if maincarX > 490:
            maincarX = 490

        if maincarY < 0:
            maincarY = 0
        if maincarY > 495:
            maincarY = 495


        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play()
            display_song_name(560,450)

        # CHANGING COLOR WITH RGB VALUE, RGB = RED, GREEN, BLUE
        screen.fill((0, 0, 0))

        # displaying the background image
        screen.blit(bg, (0, 0))

        # displaying our main car
        screen.blit(maincar, (maincarX, maincarY))

        # displaing other cars
        screen.blit(car1, (car1X, car1Y))
        screen.blit(car2, (car2X, car2Y))
        screen.blit(car3, (car3X, car3Y))
        # calling our show_score function
        show_score(570, 280)
        # calling show_hiscore function
        show_highscore(0, 0)
        display_song_name(560, 450)
        car_speed(570, 350)

        # updating the values
        maincarX += maincarX_change
        maincarY += maincarY_change

        # movement of the enemies
        car1Y += car1Ychange
        car2Y += car2Ychange
        car3Y += car3Ychange

        # moving enemies infinitely
        if car1Y > 670:
            car1Y = -100
            while True:
                car1X = random.randint(178, 490)
                car1_rect.center = (car1X, car1Y)
                if not car1_rect.colliderect(car2_rect) and not car1_rect.colliderect(car3_rect):
                    break
            score_value += 1
        if car2Y > 670:
            car2Y = -150
            while True:
                car2X = random.randint(178, 490)
                car2_rect.center = (car2X, car2Y)
                if not car2_rect.colliderect(car1_rect) and not car2_rect.colliderect(car3_rect):
                    break
            score_value += 1
        if car3Y > 670:
            car3Y = -200
            while True:
                car3X = random.randint(178, 490)
                car3_rect.center = (car3X, car3Y)
                if not car3_rect.colliderect(car1_rect) and not car3_rect.colliderect(car2_rect):
                    break
            score_value += 1

    # checking if highscore has been created
        if score_value > int(highscore):
            highscore = score_value

        # DETECTING COLLISIONS BETWEEN THE CARS
        # getting distance between our main car and car1
        def iscollision(car1X, car1Y, maincarX, maincarY):
            distance = math.sqrt(math.pow(car1X - maincarX, 1) + math.pow(car1Y - maincarY, 1))

            # checking if distance is smaller than 50 after then collision will occur
            if distance < 40:
                return True
            else:
                return False

        # getting distance between our main car and car2
        def iscollision1(car2X, car2Y, maincarX, maincarY):
            distance = math.sqrt(math.pow(car2X - maincarX, 2) + math.pow(car2Y - maincarY, 2))

            # checking if distance is smaller than 50 after then collision will occur
            if distance < 40:
                return True
            else:
                return False

        # getting distance between our main car and car3
        def iscollision2(car3X, car3Y, maincarX, maincarY):
            distance = math.sqrt(math.pow(car3X - maincarX, 2) + math.pow(car3Y - maincarY, 2))

            # checking if distance is smaller then 50 after then collision will occur
            if distance < 40:
                return True
            else:
                return False

        # giving collision a variable
        # collision between maincar and car1
        coll1 = iscollision2(car1X, car1Y, maincarX, maincarY)
        # collision between maincar and car2
        coll2 = iscollision2(car2X, car2Y, maincarX, maincarY)
        # collision between maincar and car3
        coll3 = iscollision2(car3X, car3Y, maincarX, maincarY)

        # if coll1 occur
        if coll1:
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            pygame.mixer.music.stop()
            crash_sound.play()
            # calling our game over function
            time.sleep(1)
            gameover()

        # if coll2 occur
        if coll2:
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            pygame.mixer.music.stop()
            crash_sound.play()
            # calling our game over function
            time.sleep(1)
            gameover()

        # if coll3 occur
        if coll3:
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            pygame.mixer.music.stop()
            crash_sound.play()
            # calling our game over function
            time.sleep(1)
            gameover()

        if car1Ychange == 0 and car2Ychange == 0 and car3Ychange == 0:
            pass

        # writing to our highscore.txt file
        with open("Assets/highscore.txt", "w") as f:
            f.write(str(highscore))

        pygame.display.update()


introscreen()