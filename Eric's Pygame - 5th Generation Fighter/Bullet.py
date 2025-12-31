import math
import random

import pygame


class Bullet:
    red = (255, 0, 0)
    yellow = (225, 225, 0)
    green = (0, 200, 0)
    blue = (135, 206, 235)
    brown = (128, 96, 77)
    black = (0, 0, 0)
    white = (255, 255, 255)
    gray = (128, 128, 128)
    width = 1400
    height = 750
    screen = pygame.display.set_mode((width, height))

    def __init__(self, startX, startY, targetX, targetY, bulletRange, accuracy, velocity):
        global screen, red
        if setCoordinate:
            finalLocation_x = mousePosition[0]
            finalLocation_y = mousePosition[1]
            while abs(math.sqrt((finalLocation_x - startX) ** 2 + (finalLocation_y - startY) ** 2)) < bulletRange - 25:
                finalLocation_x += (mousePosition[0] - startX) / 10
                finalLocation_y += (mousePosition[1] - startY) / 10
            while abs(math.sqrt((finalLocation_x - startX) ** 2 + (finalLocation_y - startY) ** 2)) > bulletRange + 25:
                finalLocation_x -= (mousePosition[0] - startX) / 10
                finalLocation_y -= (mousePosition[1] - startY) / 10
            finalLocation_x += random.randint(-accuracy, accuracy)
            finalLocation_y += random.randint(-accuracy, accuracy)
            repetition = int(
                math.sqrt((finalLocation_x - startX) ** 2 + (finalLocation_y - startY) ** 2) / velocity)
            originalRepetition = int(
                math.sqrt((finalLocation_x - startX) ** 2 + (finalLocation_y - startY) ** 2) / velocity)
            times = 1
            setCoordinate = False
            bulletInTheAir = True
            firstTime = True
            bulletCount -= 1

        if repetition > 0:
            if repetition < originalRepetition * 0.7 and firstTime and machineGunReloadingTimer == 5:
                setCoordinate2 = True
                firstTime = False
            length_x = abs(targetX - startX) / originalRepetition
            length_y = abs(targetX - startY) / originalRepetition
            if finalLocation_x >= startX and finalLocation_y >= startY:
                startingPointX = startX + length_x + length_x * (times - 1)
                startingPointY = startY + length_y + length_y * (times - 1)
                endingPointX = startX + length_x + length_x * times
                endingPointY = startY + length_y + length_y * times
            elif finalLocation_x >= startX and finalLocation_y <= startY:
                startingPointX = startX + length_x + length_x * (times - 1)
                startingPointY = startY - length_y - length_y * (times - 1)
                endingPointX = startX + length_x + length_x * times
                endingPointY = startY - length_y - length_y * times
            elif finalLocation_x <= startX and finalLocation_y <= startY:
                startingPointX = startX - length_x - length_x * (times - 1)
                startingPointY = startY - length_y - length_y * (times - 1)
                endingPointX = startX - length_x - length_x * times
                endingPointY = startY - length_y - length_y * times
            else:
                startingPointX = startX - length_x - length_x * (times - 1)
                startingPointY = startY + length_y + length_y * (times - 1)
                endingPointX = startX - length_x - length_x * times
                endingPointY = startY + length_y + length_y * times

            if times == 1:
                bullet = pygame.draw.line(screen, red, (startingPointX, startingPointY), (endingPointX, endingPointY), 2)
                shootingEffect = pygame.transform.scale(pygame.image.load("ShootingEffect.png"), (16, 10))
                screen.blit(shootingEffect, (playerX, playerY - 5))
            else:
                bullet = individualBullet(startX, startY, endX, endY, continueShooting)

            if bullet.colliderect(enemyList[0]) and continueShooting:
                enemyHealth -= machineGunDamage
                continueShooting = False
            if bullet.colliderect(enemyList[1]) and continueShooting:
                enemy2Health -= machineGunDamage
                continueShooting = False
            if bullet.colliderect(enemyList[2]) and continueShooting:
                enemy3Health -= machineGunDamage
                continueShooting = False
            times += 1
            repetition -= 1

        if repetition <= 0:
            bulletInTheAir = False
            continueShooting = True