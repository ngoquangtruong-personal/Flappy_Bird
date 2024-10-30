import pygame
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from utilities import constants
from utilities import helpers

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.'))
from models.background import background 
from models.floor import floor
from models.pipe import pipe
from models.bird import bird
from models.gameStartMessage import gamestartmessage
from models.gameOverMessage import gameovermessage
from models.score import score

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()
pipeCreateEvent = pygame.USEREVENT
isRunning = True
isGameOver = False
isGameStart = False

helpers.loadImages()
helpers.loadSounds()

pygame.display.set_caption('Flappy Bird')
pygame.display.set_icon(helpers.getImages('Icon'))

images = pygame.sprite.LayeredUpdates()

def createSprites():
    background(0, images)
    background(1, images)

    floor(0, images)
    floor(1, images)
        
    return bird(images), gamestartmessage(images), score(images)

player, gameStartMessage, playerScore = createSprites()

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pipeCreateEvent:
            pipe(images)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not isGameStart and not isGameOver:
                isGameStart = True
                gameStartMessage.kill()
                pygame.time.set_timer(pipeCreateEvent, 1500)
            if event.key == pygame.K_ESCAPE and isGameOver:
                isGameOver = False
                isGameStart = False
                images.empty()
                player, gameStartMessage, playerScore = createSprites()

        player.handleEvent(event)

    screen.fill(0)

    images.draw(screen)

    if isGameStart and not isGameOver:
        images.update()

    if player.checkCollision(images) and not isGameOver:
        isGameOver = True
        isGameStart = False
        gameovermessage(images)
        pygame.time.set_timer(pipeCreateEvent, 0)
        helpers.playSound('Hit')



    for item in images:
        if type(item) is pipe and item.passed():
            playerScore.value += 1
            helpers.playSound('Point')

    pygame.display.flip()
    clock.tick(constants.FPS)

pygame.quit()