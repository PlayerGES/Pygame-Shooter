import pygame
import time
import random
import math

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
pygame.init()
clock = pygame.time.Clock()
# Pygame set up variables and color variables

selectingFighter = True
background = False
displayingFighterInformation = False
playingGame = False
takeOff = False
playerFighterType = "none"
fpsCounter = 0
takeOffTimer = 0
runWay_x = 0
# Player information

money = 0
maxHealth = 2000
health = 2000
maxSpeed = 3
minSpeed = 0
currentSpeed = 3
player_x = 0
player_y = 675
player_x_change = 0
player_y_change = 0
# Player information

increasingSpeed = False
decreasingSpeed = False
shooting = False

setCoordinate = True
setCoordinate2 = False
setCoordinate3 = False
setCoordinate4 = False
setCoordinate5 = False

finalLocation_x = 0
finalLocation2_x = 0
finalLocation3_x = 0
finalLocation4_x = 0
finalLocation5_x = 0

finalLocation_y = 0
finalLocation2_y = 0
finalLocation3_y = 0
finalLocation4_y = 0
finalLocation5_y = 0

repetition = 0
repetition2 = 0
repetition3 = 0
repetition4 = 0
repetition5 = 0

originalRepetition = 0
originalRepetition2 = 0
originalRepetition3 = 0
originalRepetition4 = 0
originalRepetition5 = 10

bulletInTheAir = False
bullet2InTheAir = False
bullet3InTheAir = False
bullet4InTheAir = False
bullet5InTheAir = False

times = 1
times2 = 1
times3 = 1
times4 = 1
times5 = 1

firstTime = False
firstTime2 = False
firstTime3 = False
firstTime4 = False
firstTime5 = False

continueShooting = True
continueShooting2 = True
continueShooting3 = True
continueShooting4 = True
continueShooting5 = True

machineGunReloadTime = 8
machineGunReloadingTimer = 8
bulletCount = 50
machineGunDamage = 400
machineGunVelocity = 40
machineGunAccuracy = 50

currentWeapon = "machineGun"
# Player shooting variables

enemyList = []

enemyType = random.randint(1,2)
if enemyType == 1:
    enemyMaxHealth = 1500
    enemyHealth = 1500
    enemy_x = random.randint(2000, 2500)
    enemy_y = 700 - 26
    enemySquare = pygame.Rect(enemy_x, enemy_y, 24, 26)
    enemy = pygame.transform.scale(pygame.image.load("Phalanx CIWS.png"), (24, 26))
else:
    enemyMaxHealth = 1000
    enemyHealth = 1000
    enemy_x = random.randint(2000, 2500)
    enemy_y = random.randint(50, 500)
    enemySquare = pygame.Rect(enemy_x, enemy_y, 50, 15)
    enemy = pygame.transform.scale(pygame.image.load("J-10.png"), (50, 15))
enemyList.append(enemySquare)

enemy2MaxHealth = 5000
enemy2Health = 5000
enemy2_x = random.randint(2000, 2500)
enemy2_y = 700 - 14
enemy2Square = pygame.Rect(enemy2_x, enemy2_y, 44, 14)
enemy2 = pygame.transform.scale(pygame.image.load("Tank.png"), (44, 14))
enemyList.append(enemy2Square)

enemy3MaxHealth = 1000
enemy3Health = 1000
enemy3_x = random.randint(2000, 2500)
enemy3_y = 700 - 26
enemy3Square = pygame.Rect(enemy_x, enemy_y, 24, 26)
enemy3 = pygame.transform.scale(pygame.image.load("Sea Ram.png"), (24, 26))
enemyList.append(enemy3Square)

# definition of all enemies
enemyShooting = False

enemySetCoordinate = True
enemySetCoordinate2 = False
enemySetCoordinate3 = False
enemySetCoordinate4 = False
enemySetCoordinate5 = False

enemyFinalLocation_x = 0
enemyFinalLocation2_x = 0
enemyFinalLocation3_x = 0
enemyFinalLocation4_x = 0
enemyFinalLocation5_x = 0

enemyFinalLocation_y = 0
enemyFinalLocation2_y = 0
enemyFinalLocation3_y = 0
enemyFinalLocation4_y = 0
enemyFinalLocation5_y = 0

enemyRepetition = 0
enemyRepetition2 = 0
enemyRepetition3 = 0
enemyRepetition4 = 0
enemyRepetition5 = 0

enemyOriginalRepetition = 0
enemyOriginalRepetition2 = 0
enemyOriginalRepetition3 = 0
enemyOriginalRepetition4 = 0
enemyOriginalRepetition5 = 10

enemyBulletInTheAir = False
enemyBullet2InTheAir = False
enemyBullet3InTheAir = False
enemyBullet4InTheAir = False
enemyBullet5InTheAir = False

enemyTimes = 1
enemyTimes2 = 1
enemyTimes3 = 1
enemyTimes4 = 1
enemyTimes5 = 1

enemyFirstTime = False
enemyFirstTime2 = False
enemyFirstTime3 = False
enemyFirstTime4 = False
enemyFirstTime5 = False

enemyContinueShooting = True
enemyContinueShooting2 = True
enemyContinueShooting3 = True
enemyContinueShooting4 = True
enemyContinueShooting5 = True

enemyBulletCount = 50
enemyReloadingTimer = 3
enemyReloadTime = 3
enemyAccuracy = 150
enemyBulletVelocity = 30

enemy2FinalLocation_x = 0
enemy2FinalLocation_y = 0
enemy2BulletInTheAir = False
enemy2SetCoordinate = True
enemy2ContinueShooting = True
enemy2Repetition = 0
enemy2Times = 0
enemy2OriginalRepetition = 0

enemy2ReloadingTimer = 7
enemy2ReloadTime = 7
enemy2Accuracy = 400
enemy2BulletVelocity = 40

enemy3ReloadingTimer = 5
enemy3ReloadTime = 5
enemy3Time = 3
enemy3Timer = 0
enemy3SetCoordinate = True
enemy3ContinueShooting = True
enemy3BulletInTheAir = False
lockedOn = False
missile_x = 0
missile_y = 0
missile = pygame.transform.scale(pygame.image.load("RIM Missile.png"), (32.5, 5))
missileRect = pygame.Rect(missile_x, missile_y, 6.5, 1)

# enemy shooting variables

tree = pygame.transform.scale(pygame.image.load("Tree1.png"), (195, 50))
tree2 = pygame.transform.scale(pygame.image.load("Tree2.png"), (195, 50))
tree3 = pygame.transform.scale(pygame.image.load("Tree3.png"), (195, 50))
tree4 = pygame.transform.scale(pygame.image.load("Tree1.png"), (195, 50))
tree5 = pygame.transform.scale(pygame.image.load("Tree2.png"), (195, 50))
tree6 = pygame.transform.scale(pygame.image.load("Tree3.png"), (195, 50))

tree_x = -500
tree2_x = -500
tree3_x = -500
tree4_x = -500
tree5_x = -500
tree6_x = -500
tree_y = 650

cloud = pygame.transform.scale(pygame.image.load("Cloud1.png"), (300, 175))
cloud2 = pygame.transform.scale(pygame.image.load("Cloud2.png"), (300, 175))
cloud3 = pygame.transform.scale(pygame.image.load("Cloud3.png"), (300, 175))
cloud4 = pygame.transform.scale(pygame.image.load("Cloud4.png"), (300, 175))
cloud5 = pygame.transform.scale(pygame.image.load("Cloud5.png"), (300, 175))

cloud_x = random.randint(50, 1400)
cloud2_x = random.randint(50, 1400)
cloud3_x = random.randint(50, 1400)
cloud4_x = random.randint(50, 1400)
cloud5_x = random.randint(50, 1400)

cloud_y = random.randint(50, 150)
cloud2_y = random.randint(50, 150)
cloud3_y = random.randint(50, 150)
cloud4_y = random.randint(50, 150)
cloud5_y = random.randint(50, 150)

# decroations

victory_x = 14000
victoryRect = pygame.Rect(victory_x, 0, victory_x + 10, 700)
victory = False
defeat = False
# victory condition variables

additionalHealth = 0
additionalDamage = 0
additionalHighSpeed = 0
additionalLowSpeed = 0

maxHealth += additionalHealth
health += additionalHealth
maxSpeed += additionalHighSpeed
minSpeed += additionalLowSpeed
# upgrade variables

pygame.display.set_caption('Advanced Fighter Game')
myFont = pygame.font.SysFont('Arial', 20)
myTitleFont = pygame.font.SysFont('Arial', 60)
myFighterExplanationFont = pygame.font.SysFont('Arial', 15)

dollarSign = pygame.transform.scale(pygame.image.load("Dollar.png"), (50, 50))
# Defining all variables


def displayBackgroundInformation():
    global background
    preAddedBackgroundInformation = "Some time in the future, Earth is on the brink of total environmental " \
                                    "destruction, extreme weathers have forced billions out of their homes. This " \
                                    "destruction is caused by the alliance of energy production corporations as " \
                                    "they slowly destroys natural habitats for their own profit. The most " \
                                    "powerful nations created an coalition to fight for the environment, " \
                                    "hoping the restore the beauty that Earth once possess... You are a pilot from " \
                                    "the United Nations assigned to strike the enemy attack force, take down as many " \
                                    "enemies as possible and reach the green beacon where our forces will ensure you " \
                                    "safety. Now, good luck on your mission lieutenant and see you at the finish point!"
    backgroundInformation1 = ""
    backgroundInformation2 = ""
    backgroundInformation3 = ""
    backgroundInformation4 = ""
    backgroundInformation5 = ""

    textPosition = 0
    while True:
        displayDollars(dollarSign)
        if textPosition <= 150:
            backgroundInformation1 += preAddedBackgroundInformation[textPosition]
        elif textPosition <= 300:
            backgroundInformation2 += preAddedBackgroundInformation[textPosition]
        elif textPosition <= 450:
            backgroundInformation3 += preAddedBackgroundInformation[textPosition]
        elif textPosition <= 600:
            backgroundInformation4 += preAddedBackgroundInformation[textPosition]
        else:
            backgroundInformation5 += preAddedBackgroundInformation[textPosition]
        screen.blit(myFighterExplanationFont.render(backgroundInformation1, False, white), (200, 100))
        screen.blit(myFighterExplanationFont.render(backgroundInformation2, False, white), (200, 150))
        screen.blit(myFighterExplanationFont.render(backgroundInformation3, False, white), (200, 200))
        screen.blit(myFighterExplanationFont.render(backgroundInformation4, False, white), (200, 250))
        screen.blit(myFighterExplanationFont.render(backgroundInformation5, False, white), (200, 300))
        textPosition += 1

        if textPosition == len(preAddedBackgroundInformation):
            # time.sleep(5)
            background = True
            break
        pygame.display.update()
        screen.fill(black)
# defining the background story


def fighterSelection(x, y):
    global selectingFighter, displayingFighterInformation, F35, Su57, J20, \
        money, additionalHealth, additionalDamage, additionalLowSpeed, additionalHighSpeed, \
        maxHealth, health, machineGunDamage, minSpeed, maxSpeed
    if 250 <= x <= 500 and 250 <= y <= 350:
        selectingFighter = False
        displayingFighterInformation = True
        return F35
    elif 550 <= x <= 800 and 250 <= y <= 350:
        selectingFighter = False
        displayingFighterInformation = True
        return Su57
    elif 850 <= x <= 1100 and 250 <= y <= 350:
        selectingFighter = False
        displayingFighterInformation = True
        return J20
    if 150 <= x <= 400 and 450 <= y <= 550 and money >= 10000:
        if additionalHealth < 1500:
            money -= 10000
            additionalHealth += 500
    if 450 <= x <= 700 and 450 <= y <= 550 and money >= 10000:
        if additionalDamage < 150:
            money -= 10000
            additionalDamage += 50
    if 750 <= x <= 1000 and 450 <= y <= 550 and money >= 10000:
        if additionalLowSpeed > -1.5:
            money -= 10000
            additionalLowSpeed -= 0.5
    if 1050 <= x <= 1300 and 450 <= y <= 550 and money >= 10000:
        if additionalHighSpeed < 1.5:
            money -= 10000
            additionalHighSpeed += 0.5
# allow the player to select 3 different fighters along with upgrades


def moveImage(fighterType, x, y, reverse):
    repetition = 30
    if reverse:
        movementX = (x - 550) / repetition
        movementY = (y - 250) / repetition
    else:
        movementX = (x - 100) / repetition
        movementY = (y - 100) / repetition
    for i in range(repetition):
        displayDollars(dollarSign)
        screen.blit(fighterType, (x, y))
        x -= movementX
        y -= movementY
        pygame.display.update()
        screen.fill(black)
# Move the image


def fighterInformationDisplay(fighterType):
    global backButton, backSquare, startButton, startSquare
    continueMovingImage = True
    textPosition = 0
    fighterExplanation1 = ""
    fighterExplanation2 = ""
    fighterExplanation3 = ""
    while True:
        displayDollars(dollarSign)
        if continueMovingImage:
            positionX = 550
            positionY = 250
            moveImage(fighterType, positionX, positionY, False)
            continueMovingImage = False
            preAddedFighterExplanation = ""

        if fighterType == F35:
            preAddedFighterExplanation = "The Lockheed Martin F-35 Lightning is an American family of single-seat, " \
                                         "single-engine, all-weather stealth multi-role combat aircraft that is " \
                                         "intended " \
                                         "to perform in strike missions. It is also able to provide electronic warfare" \
                                         "and intelligence, surveillance, and reconnaissance capabilities. The F-35 " \
                                         "specializes in suppressing its enemies with massive firepower but have " \
                                         "relatively weak armor compared to its Russian and Chinese counterparts."
        elif fighterType == Su57:
            preAddedFighterExplanation = "The Sukhoi Su-57 is a single-seat, twin-engine stealth multirole fighter " \
                                         "developed by Sukhoi. The aircraft is the product of the PAK FA fighter " \
                                         "programme. The Su-57 is the first fighter in Russian military service to " \
                                         "feature stealth technology, it has very impressive speed and agility but " \
                                         "carry less weapons compared to its American and Chinese counterparts."
        elif fighterType == J20:
            preAddedFighterExplanation = "The Chengdu J-20, also known as Mighty Dragon, is a single-seat, twin jet, " \
                                         "all-weather, stealth, fighter aircraft developed by China's Chengdu " \
                                         "Aerospace Corporation for the People's Liberation Army Air Force. The J-20 " \
                                         "have heavy armor but is slower and less agile compared to its American and " \
                                         "Russian counterparts."
        if textPosition <= 150:
            fighterExplanation1 += preAddedFighterExplanation[textPosition]
        elif 150 < textPosition <= 300:
            fighterExplanation2 += preAddedFighterExplanation[textPosition]
        elif 300 < textPosition <= 450:
            fighterExplanation3 += preAddedFighterExplanation[textPosition]

        screen.blit(myFighterExplanationFont.render(fighterExplanation1, False, white), (400, 75))
        screen.blit(myFighterExplanationFont.render(fighterExplanation2, False, white), (400, 100))
        screen.blit(myFighterExplanationFont.render(fighterExplanation3, False, white), (400, 125))
        screen.blit(fighterType, (100, 100))
        textPosition += 1

        backButton = pygame.transform.scale(pygame.image.load("BackButton.jpeg"), (100, 50)).convert_alpha()
        screen.blit(backButton, (60, height - 75))
        backSquare = pygame.Rect(50, height - 75, 100, 50)

        startButton = pygame.transform.scale(pygame.image.load("StartButton.jpeg"), (100, 100)).convert_alpha()
        screen.blit(startButton, (width - 200, height - 100))
        startSquare = pygame.Rect(width - 200, height - 100, 100, 100)

        if textPosition == len(preAddedFighterExplanation):
            pygame.display.update()
            screen.fill(black)
            screen.blit(myFighterExplanationFont.render(fighterExplanation1, False, white), (400, 75))
            screen.blit(myFighterExplanationFont.render(fighterExplanation2, False, white), (400, 100))
            screen.blit(myFighterExplanationFont.render(fighterExplanation3, False, white), (400, 125))
            screen.blit(fighterType, (100, 100))

            backButton = pygame.transform.scale(pygame.image.load("BackButton.jpeg"), (100, 50)).convert_alpha()
            screen.blit(backButton, (60, height - 75))
            backSquare = pygame.Rect(50, height - 75, 100, 50)

            startButton = pygame.transform.scale(pygame.image.load("StartButton.jpeg"), (100, 100)).convert_alpha()
            screen.blit(startButton, (width - 200, height - 100))
            startSquare = pygame.Rect(width - 200, height - 100, 100, 100)
            break
        pygame.display.update()
        screen.fill(black)
# Display fighter's background story


def displayDollars(sign):
    global playingGame
    if playingGame:
        dollars = myFont.render(str(money), False, black)
    else:
        dollars = myFont.render(str(money), False, white)
    screen.blit(dollars, (725, 35))
    screen.blit(sign, (650, 20))
# Display the amount of money player has


def individualBullet(startingPointX, startingPointY, endingPointX, endingPointY, firing):
    global continueShooting, continueShooting2, continueShooting3, continueShooting4, continueShooting5, \
        repetition, repetition2, repetition3, repetition4, repetition5, playerFighterType
    color = white
    if firing:
        if playerFighterType == F35:
            color = red
        elif playerFighterType == Su57:
            color = green
        elif playerFighterType == J20:
            color = green
        return pygame.draw.line(screen, color, (startingPointX, startingPointY), (endingPointX, endingPointY), 1)
    else:
        return pygame.Rect(startingPointX, startingPointY, 100, 100)
# draw each bullet individually


def shootingFunction(playerX, playerY):
    global setCoordinate, bulletInTheAir, finalLocation_x, finalLocation_y, enemy3Health, enemy2Health, enemyHealth, machineGunDamage, \
        repetition, times, originalRepetition, setCoordinate2, firstTime, bulletCount, continueShooting
    if setCoordinate:
        finalLocation_x = mousePosition[0]
        finalLocation_y = mousePosition[1]
        while abs(math.sqrt((finalLocation_x - playerX) ** 2 + (finalLocation_y - playerY) ** 2)) < 550:
            finalLocation_x += (mousePosition[0] - playerX) / 10
            finalLocation_y += (mousePosition[1] - playerY) / 10
        while abs(math.sqrt((finalLocation_x - playerX) ** 2 + (finalLocation_y - playerY) ** 2)) > 600:
            finalLocation_x -= (mousePosition[0] - playerX) / 10
            finalLocation_y -= (mousePosition[1] - playerY) / 10
        finalLocation_x += random.randint(-machineGunAccuracy, machineGunAccuracy)
        finalLocation_y += random.randint(-machineGunAccuracy, machineGunAccuracy)
        repetition = int(
            math.sqrt((finalLocation_x - playerX) ** 2 + (finalLocation_y - playerY) ** 2) / machineGunVelocity)
        originalRepetition = int(
            math.sqrt((finalLocation_x - playerX) ** 2 + (finalLocation_y - playerY) ** 2) / machineGunVelocity)
        times = 1
        setCoordinate = False
        bulletInTheAir = True
        firstTime = True
        bulletCount -= 1

    if repetition > 0:
        if repetition < originalRepetition * 0.7 and firstTime and machineGunReloadingTimer == 5:
            setCoordinate2 = True
            firstTime = False
        length_x = abs(finalLocation_x - playerX) / originalRepetition
        length_y = abs(finalLocation_y - playerY) / originalRepetition
        if finalLocation_x >= playerX and finalLocation_y >= playerY:
            startX = playerX + length_x + length_x * (times - 1)
            startY = playerY + length_y + length_y * (times - 1)
            endX = playerX + length_x + length_x * times
            endY = playerY + length_y + length_y * times
        elif finalLocation_x >= playerX and finalLocation_y <= playerY:
            startX = playerX + length_x + length_x * (times - 1)
            startY = playerY - length_y - length_y * (times - 1)
            endX = playerX + length_x + length_x * times
            endY = playerY - length_y - length_y * times
        elif finalLocation_x <= playerX and finalLocation_y <= playerY:
            startX = playerX - length_x - length_x * (times - 1)
            startY = playerY - length_y - length_y * (times - 1)
            endX = playerX - length_x - length_x * times
            endY = playerY - length_y - length_y * times
        else:
            startX = playerX - length_x - length_x * (times - 1)
            startY = playerY + length_y + length_y * (times - 1)
            endX = playerX - length_x - length_x * times
            endY = playerY + length_y + length_y * times

        if times == 1:
            bullet = individualBullet(playerX, playerY, endX, endY, continueShooting)
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


def shootingFunction2(playerX, playerY):
    global setCoordinate2, bullet2InTheAir, finalLocation2_x, finalLocation2_y, enemy3Health, enemy2Health, enemyHealth, machineGunDamage, \
        repetition2, times2, originalRepetition2, setCoordinate3, firstTime2, bulletCount, continueShooting2

    if setCoordinate2:
        finalLocation2_x = mousePosition[0]
        finalLocation2_y = mousePosition[1]
        while abs(math.sqrt((finalLocation2_x - playerX) ** 2 + (finalLocation2_y - playerY) ** 2)) < 550:
            finalLocation2_x += (mousePosition[0] - playerX) / 10
            finalLocation2_y += (mousePosition[1] - playerY) / 10
        while abs(math.sqrt((finalLocation2_x - playerX) ** 2 + (finalLocation2_y - playerY) ** 2)) > 600:
            finalLocation2_x -= (mousePosition[0] - playerX) / 10
            finalLocation2_y -= (mousePosition[1] - playerY) / 10
        finalLocation2_x += random.randint(-machineGunAccuracy, machineGunAccuracy)
        finalLocation2_y += random.randint(-machineGunAccuracy, machineGunAccuracy)
        repetition2 = int(
            math.sqrt((finalLocation2_x - playerX) ** 2 + (finalLocation2_y - playerY) ** 2) / machineGunVelocity)
        originalRepetition2 = int(
            math.sqrt((finalLocation2_x - playerX) ** 2 + (finalLocation2_y - playerY) ** 2) / machineGunVelocity)
        times2 = 1
        setCoordinate2 = False
        bullet2InTheAir = True
        firstTime2 = True
        bulletCount -= 1

    if repetition2 > 0:
        if repetition2 < originalRepetition2 * 0.7 and firstTime2 and machineGunReloadingTimer == 5:
            setCoordinate3 = True
            firstTime2 = False
        length_x = abs(finalLocation2_x - playerX) / originalRepetition2
        length_y = abs(finalLocation2_y - playerY) / originalRepetition2
        if finalLocation2_x >= playerX and finalLocation2_y >= playerY:
            startX = playerX + length_x + length_x * (times2 - 1)
            startY = playerY + length_y + length_y * (times2 - 1)
            endX = playerX + length_x + length_x * times2
            endY = playerY + length_y + length_y * times2
        elif finalLocation2_x >= playerX and finalLocation2_y <= playerY:
            startX = playerX + length_x + length_x * (times2 - 1)
            startY = playerY - length_y - length_y * (times2 - 1)
            endX = playerX + length_x + length_x * times2
            endY = playerY - length_y - length_y * times2
        elif finalLocation2_x <= playerX and finalLocation2_y <= playerY:
            startX = playerX - length_x - length_x * (times2 - 1)
            startY = playerY - length_y - length_y * (times2 - 1)
            endX = playerX - length_x - length_x * times2
            endY = playerY - length_y - length_y * times2
        else:
            startX = playerX - length_x - length_x * (times2 - 1)
            startY = playerY + length_y + length_y * (times2 - 1)
            endX = playerX - length_x - length_x * times2
            endY = playerY + length_y + length_y * times2

        if times2 == 1:
            bullet = individualBullet(playerX, playerY, endX, endY, continueShooting2)
            shootingEffect = pygame.transform.scale(pygame.image.load("ShootingEffect.png"), (16, 10))
            screen.blit(shootingEffect, (playerX, playerY - 5))
        else:
            bullet = individualBullet(startX, startY, endX, endY, continueShooting2)

        if bullet.colliderect(enemyList[0]) and continueShooting2:
            enemyHealth -= machineGunDamage
            continueShooting2 = False
        if bullet.colliderect(enemyList[1]) and continueShooting2:
            enemy2Health -= machineGunDamage
            continueShooting2 = False
        if bullet.colliderect(enemyList[2]) and continueShooting2:
            enemy3Health -= machineGunDamage
            continueShooting2 = False

        times2 += 1
        repetition2 -= 1

    if repetition2 <= 0:
        bullet2InTheAir = False
        continueShooting2 = True


def shootingFunction3(playerX, playerY):
    global setCoordinate3, bullet3InTheAir, finalLocation3_x, finalLocation3_y, enemy3Health, enemy2Health, enemyHealth, machineGunDamage, \
        repetition3, times3, originalRepetition3, setCoordinate4, firstTime3, bulletCount, continueShooting3

    if setCoordinate3:
        finalLocation3_x = mousePosition[0]
        finalLocation3_y = mousePosition[1]
        while abs(math.sqrt((finalLocation3_x - playerX) ** 2 + (finalLocation3_y - playerY) ** 2)) < 550:
            finalLocation3_x += (mousePosition[0] - playerX) / 10
            finalLocation3_y += (mousePosition[1] - playerY) / 10
        while abs(math.sqrt((finalLocation3_x - playerX) ** 2 + (finalLocation3_y - playerY) ** 2)) > 600:
            finalLocation3_x -= (mousePosition[0] - playerX) / 10
            finalLocation3_y -= (mousePosition[1] - playerY) / 10
        finalLocation3_x += random.randint(-machineGunAccuracy, machineGunAccuracy)
        finalLocation3_y += random.randint(-machineGunAccuracy, machineGunAccuracy)
        repetition3 = int(
            math.sqrt((finalLocation3_x - playerX) ** 2 + (finalLocation3_y - playerY) ** 2) / machineGunVelocity)
        originalRepetition3 = int(
            math.sqrt((finalLocation3_x - playerX) ** 2 + (finalLocation3_y - playerY) ** 2) / machineGunVelocity)
        times3 = 1
        setCoordinate3 = False
        bullet3InTheAir = True
        firstTime3 = True
        bulletCount -= 1

    if repetition3 > 0:
        if repetition3 < originalRepetition3 * 0.7 and firstTime3 and machineGunReloadingTimer == 5:
            setCoordinate4 = True
            firstTime3 = False
        length_x = abs(finalLocation3_x - playerX) / originalRepetition3
        length_y = abs(finalLocation3_y - playerY) / originalRepetition3
        if finalLocation3_x >= playerX and finalLocation3_y >= playerY:
            startX = playerX + length_x + length_x * (times3 - 1)
            startY = playerY + length_y + length_y * (times3 - 1)
            endX = playerX + length_x + length_x * times3
            endY = playerY + length_y + length_y * times3
        elif finalLocation3_x >= playerX and finalLocation3_y <= playerY:
            startX = playerX + length_x + length_x * (times3 - 1)
            startY = playerY - length_y - length_y * (times3 - 1)
            endX = playerX + length_x + length_x * times3
            endY = playerY - length_y - length_y * times3
        elif finalLocation3_x <= playerX and finalLocation3_y <= playerY:
            startX = playerX - length_x - length_x * (times3 - 1)
            startY = playerY - length_y - length_y * (times3 - 1)
            endX = playerX - length_x - length_x * times3
            endY = playerY - length_y - length_y * times3
        else:
            startX = playerX - length_x - length_x * (times3 - 1)
            startY = playerY + length_y + length_y * (times3 - 1)
            endX = playerX - length_x - length_x * times3
            endY = playerY + length_y + length_y * times3

        if times3 == 1:
            bullet = individualBullet(playerX, playerY, endX, endY, continueShooting3)
            shootingEffect = pygame.transform.scale(pygame.image.load("ShootingEffect.png"), (16, 10))
            screen.blit(shootingEffect, (playerX, playerY - 5))
        else:
            bullet = individualBullet(startX, startY, endX, endY, continueShooting3)

        if bullet.colliderect(enemyList[0]) and continueShooting3:
            enemyHealth -= machineGunDamage
            continueShooting3 = False
        if bullet.colliderect(enemyList[1]) and continueShooting3:
            enemy2Health -= machineGunDamage
            continueShooting3 = False
        if bullet.colliderect(enemyList[2]) and continueShooting3:
            enemy3Health -= machineGunDamage
            continueShooting3 = False

        times3 += 1
        repetition3 -= 1

    if repetition3 <= 0:
        bullet3InTheAir = False
        continueShooting3 = True


def shootingFunction4(playerX, playerY):
    global setCoordinate4, bullet4InTheAir, finalLocation4_x, finalLocation4_y, enemy3Health, enemy2Health, enemyHealth, machineGunDamage, \
        repetition4, times4, originalRepetition4, setCoordinate5, firstTime4, bulletCount, continueShooting4

    if setCoordinate4:
        finalLocation4_x = mousePosition[0]
        finalLocation4_y = mousePosition[1]
        while abs(math.sqrt((finalLocation4_x - playerX) ** 2 + (finalLocation4_y - playerY) ** 2)) < 550:
            finalLocation4_x += (mousePosition[0] - playerX) / 10
            finalLocation4_y += (mousePosition[1] - playerY) / 10
        while abs(math.sqrt((finalLocation4_x - playerX) ** 2 + (finalLocation4_y - playerY) ** 2)) > 600:
            finalLocation4_x -= (mousePosition[0] - playerX) / 10
            finalLocation4_y -= (mousePosition[1] - playerY) / 10
        finalLocation4_x += random.randint(-machineGunAccuracy, machineGunAccuracy)
        finalLocation4_y += random.randint(-machineGunAccuracy, machineGunAccuracy)
        repetition4 = int(
            math.sqrt((finalLocation4_x - playerX) ** 2 + (finalLocation4_y - playerY) ** 2) / machineGunVelocity)
        originalRepetition4 = int(
            math.sqrt((finalLocation4_x - playerX) ** 2 + (finalLocation4_y - playerY) ** 2) / machineGunVelocity)
        times4 = 1
        setCoordinate4 = False
        bullet4InTheAir = True
        firstTime4 = True
        bulletCount -= 1

    if repetition4 > 0:
        if repetition4 < originalRepetition4 * 0.7 and firstTime4 and machineGunReloadingTimer == 5:
            setCoordinate5 = True
            firstTime4 = False
        length_x = abs(finalLocation4_x - playerX) / originalRepetition4
        length_y = abs(finalLocation4_y - playerY) / originalRepetition4
        if finalLocation4_x >= playerX and finalLocation4_y >= playerY:
            startX = playerX + length_x + length_x * (times4 - 1)
            startY = playerY + length_y + length_y * (times4 - 1)
            endX = playerX + length_x + length_x * times4
            endY = playerY + length_y + length_y * times4
        elif finalLocation4_x >= playerX and finalLocation4_y <= playerY:
            startX = playerX + length_x + length_x * (times4 - 1)
            startY = playerY - length_y - length_y * (times4 - 1)
            endX = playerX + length_x + length_x * times4
            endY = playerY - length_y - length_y * times4
        elif finalLocation4_x <= playerX and finalLocation4_y <= playerY:
            startX = playerX - length_x - length_x * (times4 - 1)
            startY = playerY - length_y - length_y * (times4 - 1)
            endX = playerX - length_x - length_x * times4
            endY = playerY - length_y - length_y * times4
        else:
            startX = playerX - length_x - length_x * (times4 - 1)
            startY = playerY + length_y + length_y * (times4 - 1)
            endX = playerX - length_x - length_x * times4
            endY = playerY + length_y + length_y * times4

        if times4 == 1:
            bullet = individualBullet(playerX, playerY, endX, endY, continueShooting4)
            shootingEffect = pygame.transform.scale(pygame.image.load("ShootingEffect.png"), (16, 10))
            screen.blit(shootingEffect, (playerX, playerY - 5))
        else:
            bullet = individualBullet(startX, startY, endX, endY, continueShooting4)

        if bullet.colliderect(enemyList[0]) and continueShooting4:
            enemyHealth -= machineGunDamage
            continueShooting4 = False
        if bullet.colliderect(enemyList[1]) and continueShooting4:
            enemy2Health -= machineGunDamage
            continueShooting4 = False
        if bullet.colliderect(enemyList[2]) and continueShooting4:
            enemy3Health -= machineGunDamage
            continueShooting4 = False
        times4 += 1
        repetition4 -= 1

    if repetition4 <= 0:
        bullet4InTheAir = False
        continueShooting4 = True


def shootingFunction5(playerX, playerY):
    global setCoordinate5, bullet5InTheAir, finalLocation5_x, finalLocation5_y, enemy2Health, enemyHealth, machineGunDamage, \
        repetition5, times5, originalRepetition5, setCoordinate, firstTime5, bulletCount, continueShooting5

    if setCoordinate5:
        finalLocation5_x = mousePosition[0]
        finalLocation5_y = mousePosition[1]
        while abs(math.sqrt((finalLocation5_x - playerX) ** 2 + (finalLocation5_y - playerY) ** 2)) < 550:
            finalLocation5_x += (mousePosition[0] - playerX) / 10
            finalLocation5_y += (mousePosition[1] - playerY) / 10
        while abs(math.sqrt((finalLocation5_x - playerX) ** 2 + (finalLocation5_y - playerY) ** 2)) > 600:
            finalLocation5_x -= (mousePosition[0] - playerX) / 10
            finalLocation5_y -= (mousePosition[1] - playerY) / 10
        finalLocation5_x += random.randint(-machineGunAccuracy, machineGunAccuracy)
        finalLocation5_y += random.randint(-machineGunAccuracy, machineGunAccuracy)
        repetition5 = int(
            math.sqrt((finalLocation5_x - playerX) ** 2 + (finalLocation5_y - playerY) ** 2) / machineGunVelocity)
        originalRepetition5 = int(
            math.sqrt((finalLocation5_x - playerX) ** 2 + (finalLocation5_y - playerY) ** 2) / machineGunVelocity)
        times5 = 1
        setCoordinate5 = False
        bullet5InTheAir = True
        firstTime5 = True
        bulletCount -= 1

    if repetition5 > 0:
        if repetition5 < originalRepetition5 * 0.7 and firstTime5 and machineGunReloadingTimer == 5:
            setCoordinate = True
            firstTime5 = False
        length_x = abs(finalLocation5_x - playerX) / originalRepetition5
        length_y = abs(finalLocation5_y - playerY) / originalRepetition5
        if finalLocation5_x >= playerX and finalLocation5_y >= playerY:
            startX = playerX + length_x + length_x * (times5 - 1)
            startY = playerY + length_y + length_y * (times5 - 1)
            endX = playerX + length_x + length_x * times5
            endY = playerY + length_y + length_y * times5
        elif finalLocation5_x >= playerX and finalLocation5_y <= playerY:
            startX = playerX + length_x + length_x * (times5 - 1)
            startY = playerY - length_y - length_y * (times5 - 1)
            endX = playerX + length_x + length_x * times5
            endY = playerY - length_y - length_y * times5
        elif finalLocation5_x <= playerX and finalLocation5_y <= playerY:
            startX = playerX - length_x - length_x * (times5 - 1)
            startY = playerY - length_y - length_y * (times5 - 1)
            endX = playerX - length_x - length_x * times5
            endY = playerY - length_y - length_y * times5
        else:
            startX = playerX - length_x - length_x * (times5 - 1)
            startY = playerY + length_y + length_y * (times5 - 1)
            endX = playerX - length_x - length_x * times5
            endY = playerY + length_y + length_y * times5

        if times5 == 1:
            bullet = individualBullet(playerX, playerY, endX, endY, continueShooting5)
            shootingEffect = pygame.transform.scale(pygame.image.load("ShootingEffect.png"), (16, 10))
            screen.blit(shootingEffect, (playerX, playerY - 5))
        else:
            bullet = individualBullet(startX, startY, endX, endY, continueShooting5)

        if bullet.colliderect(enemyList[0]) and continueShooting5:
            enemyHealth -= machineGunDamage
            continueShooting5 = False
        if bullet.colliderect(enemyList[1]) and continueShooting5:
            enemy2Health -= machineGunDamage
            continueShooting5 = False
        if bullet.colliderect(enemyList[2]) and continueShooting5:
            enemy2Health -= machineGunDamage
            continueShooting5 = False

        times5 += 1
        repetition5 -= 1

    if repetition5 <= 0:
        bullet5InTheAir = False
        continueShooting5 = True


def resetShootingFunctions():
    global setCoordinate, setCoordinate2, setCoordinate3, setCoordinate4, setCoordinate5, finalLocation_x, \
        finalLocation2_x, finalLocation3_x, finalLocation4_x, finalLocation5_x, finalLocation_y, finalLocation2_y, \
        finalLocation3_y, finalLocation4_y, finalLocation5_y, repetition, repetition2, repetition3, repetition4, \
        repetition5, originalRepetition, originalRepetition2, originalRepetition3, originalRepetition4, \
        originalRepetition5, bulletInTheAir, bullet2InTheAir, bullet3InTheAir, bullet4InTheAir, bullet5InTheAir, times, \
        times2, times3, times4, times5, firstTime, firstTime2, firstTime3, firstTime4, firstTime5, continueShooting, \
        continueShooting2, continueShooting3, continueShooting4, continueShooting5

    setCoordinate = True
    setCoordinate2 = False
    setCoordinate3 = False
    setCoordinate4 = False
    setCoordinate5 = False

    finalLocation_x = 0
    finalLocation2_x = 0
    finalLocation3_x = 0
    finalLocation4_x = 0
    finalLocation5_x = 0

    finalLocation_y = 0
    finalLocation2_y = 0
    finalLocation3_y = 0
    finalLocation4_y = 0
    finalLocation5_y = 0

    repetition = 0
    repetition2 = 0
    repetition3 = 0
    repetition4 = 0
    repetition5 = 0

    originalRepetition = 0
    originalRepetition2 = 0
    originalRepetition3 = 0
    originalRepetition4 = 0
    originalRepetition5 = 10

    bulletInTheAir = False
    bullet2InTheAir = False
    bullet3InTheAir = False
    bullet4InTheAir = False
    bullet5InTheAir = False

    times = 1
    times2 = 1
    times3 = 1
    times4 = 1
    times5 = 1

    firstTime = False
    firstTime2 = False
    firstTime3 = False
    firstTime4 = False
    firstTime5 = False

    continueShooting = True
    continueShooting2 = True
    continueShooting3 = True
    continueShooting4 = True
    continueShooting5 = True
# player shooting functions


def enemyShootingFunction(enemyX, enemyY):
    global enemySetCoordinate, enemyBulletInTheAir, enemyFinalLocation_x, enemyFinalLocation_y, playerSquare, health, \
        enemyRepetition, enemyTimes, enemyOriginalRepetition, enemySetCoordinate2, enemyFirstTime, enemyBulletCount, \
        enemyContinueShooting
    if enemySetCoordinate:
        enemyFinalLocation_x = player_x + 25
        enemyFinalLocation_y = player_y + 7.5
        while abs(math.sqrt((enemyFinalLocation_x - enemyX) ** 2 + (enemyFinalLocation_y - enemyY) ** 2)) < 700:
            enemyFinalLocation_x += (enemyFinalLocation_x - enemyX) / 10
            enemyFinalLocation_y += (enemyFinalLocation_y - enemyY) / 10
        while abs(math.sqrt((enemyFinalLocation_x - enemyX) ** 2 + (enemyFinalLocation_y - enemyY) ** 2)) > 800:
            enemyFinalLocation_x -= (enemyFinalLocation_x - enemyX) / 10
            enemyFinalLocation_y -= (enemyFinalLocation_y - enemyY) / 10
        enemyFinalLocation_x += random.randint(-enemyAccuracy, enemyAccuracy)
        enemyFinalLocation_y += random.randint(-enemyAccuracy, enemyAccuracy)
        enemyRepetition = int(math.sqrt(
            (enemyFinalLocation_x - enemyX) ** 2 + (enemyFinalLocation_y - enemyY) ** 2) / enemyBulletVelocity)
        enemyOriginalRepetition = int(math.sqrt(
            (enemyFinalLocation_x - enemyX) ** 2 + (enemyFinalLocation_y - enemyY) ** 2) / enemyBulletVelocity)
        enemyTimes = 1
        enemySetCoordinate = False
        enemyBulletInTheAir = True
        enemyFirstTime = True
        enemyBulletCount -= 1
    if enemyRepetition > 0:
        if enemyRepetition < enemyOriginalRepetition * 0.8 and enemyFirstTime and enemyReloadingTimer == 3:
            enemySetCoordinate2 = True
            enemyFirstTime = False
        length_x = abs(enemyFinalLocation_x - enemyX) / enemyOriginalRepetition
        length_y = abs(enemyFinalLocation_y - enemyY) / enemyOriginalRepetition
        if enemyFinalLocation_x >= enemyX and enemyFinalLocation_y >= enemyY:
            startX = enemyX + length_x + length_x * (enemyTimes - 1)
            startY = enemyY + length_y + length_y * (enemyTimes - 1)
            endX = enemyX + length_x + length_x * enemyTimes
            endY = enemyY + length_y + length_y * enemyTimes
        elif enemyFinalLocation_x >= enemyX and enemyFinalLocation_y <= enemyY:
            startX = enemyX + length_x + length_x * (enemyTimes - 1)
            startY = enemyY - length_y - length_y * (enemyTimes - 1)
            endX = enemyX + length_x + length_x * enemyTimes
            endY = enemyY - length_y - length_y * enemyTimes
        elif enemyFinalLocation_x <= enemyX and enemyFinalLocation_y <= enemyY:
            startX = enemyX - length_x - length_x * (enemyTimes - 1)
            startY = enemyY - length_y - length_y * (enemyTimes - 1)
            endX = enemyX - length_x - length_x * enemyTimes
            endY = enemyY - length_y - length_y * enemyTimes
        else:
            startX = enemyX - length_x - length_x * (enemyTimes - 1)
            startY = enemyY + length_y + length_y * (enemyTimes - 1)
            endX = enemyX - length_x - length_x * enemyTimes
            endY = enemyY + length_y + length_y * enemyTimes
        if enemyTimes == 1:
            bullet = individualBullet(enemyX, enemyY, endX, endY, enemyContinueShooting)
            shootingEffect = pygame.transform.scale(pygame.image.load("ShootingEffect2.png"), (16, 10))
            screen.blit(shootingEffect, (enemyX, enemyY - 5))
        else:
            bullet = individualBullet(startX, startY, endX, endY, enemyContinueShooting)

        if bullet.colliderect(playerSquare) and enemyContinueShooting:
            health -= 75
            enemyContinueShooting = False
        enemyTimes += 1
        enemyRepetition -= 1
    if enemyRepetition <= 0:
        enemyBulletInTheAir = False
        enemyContinueShooting = True


def enemyShootingFunction2(enemyX, enemyY):
    global enemySetCoordinate2, enemyBullet2InTheAir, enemyFinalLocation2_x, enemyFinalLocation2_y, playerSquare, health, \
        enemyRepetition2, enemyTimes2, enemyOriginalRepetition2, enemySetCoordinate3, enemyFirstTime2, enemyBulletCount, \
        enemyContinueShooting2
    if enemySetCoordinate2:
        enemyFinalLocation2_x = player_x + 25
        enemyFinalLocation2_y = player_y + 7.5
        while abs(math.sqrt((enemyFinalLocation2_x - enemyX) ** 2 + (enemyFinalLocation2_y - enemyY) ** 2)) < 700:
            enemyFinalLocation2_x += (enemyFinalLocation2_x - enemyX) / 10
            enemyFinalLocation2_y += (enemyFinalLocation2_y - enemyY) / 10
        while abs(math.sqrt((enemyFinalLocation2_x - enemyX) ** 2 + (enemyFinalLocation2_y - enemyY) ** 2)) > 800:
            enemyFinalLocation2_x -= (enemyFinalLocation2_x - enemyX) / 10
            enemyFinalLocation2_y -= (enemyFinalLocation2_y - enemyY) / 10
        enemyFinalLocation2_x += random.randint(-enemyAccuracy, enemyAccuracy)
        enemyFinalLocation2_y += random.randint(-enemyAccuracy, enemyAccuracy)
        enemyRepetition2 = int(math.sqrt(
            (enemyFinalLocation2_x - enemyX) ** 2 + (enemyFinalLocation2_y - enemyY) ** 2) / enemyBulletVelocity)
        enemyOriginalRepetition2 = int(math.sqrt(
            (enemyFinalLocation2_x - enemyX) ** 2 + (enemyFinalLocation2_y - enemyY) ** 2) / enemyBulletVelocity)
        enemyTimes2 = 1
        enemySetCoordinate2 = False
        enemyBullet2InTheAir = True
        enemyFirstTime2 = True
        enemyBulletCount -= 1
    if enemyRepetition2 > 0:
        if enemyRepetition2 < enemyOriginalRepetition2 * 0.8 and enemyFirstTime2 and enemyReloadingTimer == 3:
            enemySetCoordinate3 = True
            enemyFirstTime2 = False
        length_x = abs(enemyFinalLocation2_x - enemyX) / enemyOriginalRepetition2
        length_y = abs(enemyFinalLocation2_y - enemyY) / enemyOriginalRepetition2
        if enemyFinalLocation2_x >= enemyX and enemyFinalLocation2_y >= enemyY:
            startX = enemyX + length_x + length_x * (enemyTimes2 - 1)
            startY = enemyY + length_y + length_y * (enemyTimes2 - 1)
            endX = enemyX + length_x + length_x * enemyTimes2
            endY = enemyY + length_y + length_y * enemyTimes2
        elif enemyFinalLocation2_x >= enemyX and enemyFinalLocation2_y <= enemyY:
            startX = enemyX + length_x + length_x * (enemyTimes2 - 1)
            startY = enemyY - length_y - length_y * (enemyTimes2 - 1)
            endX = enemyX + length_x + length_x * enemyTimes2
            endY = enemyY - length_y - length_y * enemyTimes2
        elif enemyFinalLocation2_x <= enemyX and enemyFinalLocation2_y <= enemyY:
            startX = enemyX - length_x - length_x * (enemyTimes2 - 1)
            startY = enemyY - length_y - length_y * (enemyTimes2 - 1)
            endX = enemyX - length_x - length_x * enemyTimes2
            endY = enemyY - length_y - length_y * enemyTimes2
        else:
            startX = enemyX - length_x - length_x * (enemyTimes2 - 1)
            startY = enemyY + length_y + length_y * (enemyTimes2 - 1)
            endX = enemyX - length_x - length_x * enemyTimes2
            endY = enemyY + length_y + length_y * enemyTimes2

        if enemyTimes2 == 1:
            bullet = individualBullet(enemyX, enemyY, endX, endY, enemyContinueShooting2)
            shootingEffect = pygame.transform.scale(pygame.image.load("ShootingEffect2.png"), (16, 10))
            screen.blit(shootingEffect, (enemyX, enemyY - 5))
        else:
            bullet = individualBullet(startX, startY, endX, endY, enemyContinueShooting2)

        if bullet.colliderect(playerSquare) and enemyContinueShooting2:
            health -= 75
            enemyContinueShooting2 = False
        enemyTimes2 += 1
        enemyRepetition2 -= 1
    if enemyRepetition2 <= 0:
        enemyBullet2InTheAir = False
        enemyContinueShooting2 = True


def enemyShootingFunction3(enemyX, enemyY):
    global enemySetCoordinate3, enemyBullet3InTheAir, enemyFinalLocation3_x, enemyFinalLocation3_y, playerSquare, health, \
        enemyRepetition3, enemyTimes3, enemyOriginalRepetition3, enemySetCoordinate4, enemyFirstTime3, enemyBulletCount, \
        enemyContinueShooting3
    if enemySetCoordinate3:
        enemyFinalLocation3_x = player_x + 25
        enemyFinalLocation3_y = player_y + 7.5
        while abs(math.sqrt((enemyFinalLocation3_x - enemyX) ** 2 + (enemyFinalLocation3_y - enemyY) ** 2)) < 700:
            enemyFinalLocation3_x += (enemyFinalLocation3_x - enemyX) / 10
            enemyFinalLocation3_y += (enemyFinalLocation3_y - enemyY) / 10
        while abs(math.sqrt((enemyFinalLocation3_x - enemyX) ** 2 + (enemyFinalLocation3_y - enemyY) ** 2)) > 800:
            enemyFinalLocation3_x -= (enemyFinalLocation3_x - enemyX) / 10
            enemyFinalLocation3_y -= (enemyFinalLocation3_y - enemyY) / 10
        enemyFinalLocation3_x += random.randint(-enemyAccuracy, enemyAccuracy)
        enemyFinalLocation3_y += random.randint(-enemyAccuracy, enemyAccuracy)
        enemyRepetition3 = int(math.sqrt(
            (enemyFinalLocation3_x - enemyX) ** 2 + (enemyFinalLocation3_y - enemyY) ** 2) / enemyBulletVelocity)
        enemyOriginalRepetition3 = int(math.sqrt(
            (enemyFinalLocation3_x - enemyX) ** 2 + (enemyFinalLocation3_y - enemyY) ** 2) / enemyBulletVelocity)
        enemyTimes3 = 1
        enemySetCoordinate3 = False
        enemyBullet3InTheAir = True
        enemyFirstTime3 = True
        enemyBulletCount -= 1
    if enemyRepetition3 > 0:
        if enemyRepetition3 < enemyOriginalRepetition3 * 0.8 and enemyFirstTime3 and enemyReloadingTimer == 3:
            enemySetCoordinate4 = True
            enemyFirstTime3 = False
        length_x = abs(enemyFinalLocation3_x - enemyX) / enemyOriginalRepetition3
        length_y = abs(enemyFinalLocation3_y - enemyY) / enemyOriginalRepetition3
        if enemyFinalLocation3_x >= enemyX and enemyFinalLocation3_y >= enemyY:
            startX = enemyX + length_x + length_x * (enemyTimes3 - 1)
            startY = enemyY + length_y + length_y * (enemyTimes3 - 1)
            endX = enemyX + length_x + length_x * enemyTimes3
            endY = enemyY + length_y + length_y * enemyTimes3
        elif enemyFinalLocation3_x >= enemyX and enemyFinalLocation3_y <= enemyY:
            startX = enemyX + length_x + length_x * (enemyTimes3 - 1)
            startY = enemyY - length_y - length_y * (enemyTimes3 - 1)
            endX = enemyX + length_x + length_x * enemyTimes3
            endY = enemyY - length_y - length_y * enemyTimes3
        elif enemyFinalLocation3_x <= enemyX and enemyFinalLocation3_y <= enemyY:
            startX = enemyX - length_x - length_x * (enemyTimes3 - 1)
            startY = enemyY - length_y - length_y * (enemyTimes3 - 1)
            endX = enemyX - length_x - length_x * enemyTimes3
            endY = enemyY - length_y - length_y * enemyTimes3
        else:
            startX = enemyX - length_x - length_x * (enemyTimes3 - 1)
            startY = enemyY + length_y + length_y * (enemyTimes3 - 1)
            endX = enemyX - length_x - length_x * enemyTimes3
            endY = enemyY + length_y + length_y * enemyTimes3

        if enemyTimes3 == 1:
            bullet = individualBullet(enemyX, enemyY, endX, endY, enemyContinueShooting3)
            shootingEffect = pygame.transform.scale(pygame.image.load("ShootingEffect2.png"), (16, 10))
            screen.blit(shootingEffect, (enemyX, enemyY - 5))
        else:
            bullet = individualBullet(startX, startY, endX, endY, enemyContinueShooting3)

        if bullet.colliderect(playerSquare) and enemyContinueShooting3:
            health -= 75
            enemyContinueShooting3 = False
        enemyTimes3 += 1
        enemyRepetition3 -= 1
    if enemyRepetition3 <= 0:
        enemyBullet3InTheAir = False
        enemyContinueShooting3 = True


def enemyShootingFunction4(enemyX, enemyY):
    global enemySetCoordinate4, enemyBullet4InTheAir, enemyFinalLocation4_x, enemyFinalLocation4_y, playerSquare, health, \
        enemyRepetition4, enemyTimes4, enemyOriginalRepetition4, enemySetCoordinate5, enemyFirstTime4, enemyBulletCount, \
        enemyContinueShooting4
    if enemySetCoordinate4:
        enemyFinalLocation4_x = player_x + 25
        enemyFinalLocation4_y = player_y + 7.5
        while abs(math.sqrt((enemyFinalLocation4_x - enemyX) ** 2 + (enemyFinalLocation4_y - enemyY) ** 2)) < 700:
            enemyFinalLocation4_x += (enemyFinalLocation4_x - enemyX) / 10
            enemyFinalLocation4_y += (enemyFinalLocation4_y - enemyY) / 10
        while abs(math.sqrt((enemyFinalLocation4_x - enemyX) ** 2 + (enemyFinalLocation4_y - enemyY) ** 2)) > 800:
            enemyFinalLocation4_x -= (enemyFinalLocation4_x - enemyX) / 10
            enemyFinalLocation4_y -= (enemyFinalLocation4_y - enemyY) / 10
        enemyFinalLocation4_x += random.randint(-enemyAccuracy, enemyAccuracy)
        enemyFinalLocation4_y += random.randint(-enemyAccuracy, enemyAccuracy)
        enemyRepetition4 = int(math.sqrt(
            (enemyFinalLocation4_x - enemyX) ** 2 + (enemyFinalLocation4_y - enemyY) ** 2) / enemyBulletVelocity)
        enemyOriginalRepetition4 = int(math.sqrt(
            (enemyFinalLocation4_x - enemyX) ** 2 + (enemyFinalLocation4_y - enemyY) ** 2) / enemyBulletVelocity)
        enemyTimes4 = 1
        enemySetCoordinate4 = False
        enemyBullet4InTheAir = True
        enemyFirstTime4 = True
        enemyBulletCount -= 1
    if enemyRepetition4 > 0:
        if enemyRepetition4 < enemyOriginalRepetition4 * 0.8 and enemyFirstTime4 and enemyReloadingTimer == 3:
            enemySetCoordinate5 = True
            enemyFirstTime4 = False
        length_x = abs(enemyFinalLocation4_x - enemyX) / enemyOriginalRepetition4
        length_y = abs(enemyFinalLocation4_y - enemyY) / enemyOriginalRepetition4
        if enemyFinalLocation4_x >= enemyX and enemyFinalLocation4_y >= enemyY:
            startX = enemyX + length_x + length_x * (enemyTimes4 - 1)
            startY = enemyY + length_y + length_y * (enemyTimes4 - 1)
            endX = enemyX + length_x + length_x * enemyTimes4
            endY = enemyY + length_y + length_y * enemyTimes4
        elif enemyFinalLocation4_x >= enemyX and enemyFinalLocation4_y <= enemyY:
            startX = enemyX + length_x + length_x * (enemyTimes4 - 1)
            startY = enemyY - length_y - length_y * (enemyTimes4 - 1)
            endX = enemyX + length_x + length_x * enemyTimes4
            endY = enemyY - length_y - length_y * enemyTimes4
        elif enemyFinalLocation4_x <= enemyX and enemyFinalLocation4_y <= enemyY:
            startX = enemyX - length_x - length_x * (enemyTimes4 - 1)
            startY = enemyY - length_y - length_y * (enemyTimes4 - 1)
            endX = enemyX - length_x - length_x * enemyTimes4
            endY = enemyY - length_y - length_y * enemyTimes4
        else:
            startX = enemyX - length_x - length_x * (enemyTimes4 - 1)
            startY = enemyY + length_y + length_y * (enemyTimes4 - 1)
            endX = enemyX - length_x - length_x * enemyTimes4
            endY = enemyY + length_y + length_y * enemyTimes4

        if enemyTimes4 == 1:
            bullet = individualBullet(enemyX, enemyY, endX, endY, enemyContinueShooting4)
            shootingEffect = pygame.transform.scale(pygame.image.load("ShootingEffect2.png"), (16, 10))
            screen.blit(shootingEffect, (enemyX, enemyY - 5))
        else:
            bullet = individualBullet(startX, startY, endX, endY, enemyContinueShooting4)

        if bullet.colliderect(playerSquare) and enemyContinueShooting4:
            health -= 75
            enemyContinueShooting4 = False
        enemyTimes4 += 1
        enemyRepetition4 -= 1
    if enemyRepetition4 <= 0:
        enemyBullet4InTheAir = False
        enemyContinueShooting4 = True


def enemyShootingFunction5(enemyX, enemyY):
    global enemySetCoordinate5, enemyBullet5InTheAir, enemyFinalLocation5_x, enemyFinalLocation5_y, playerSquare, health, \
        enemyRepetition5, enemyTimes5, enemyOriginalRepetition5, enemySetCoordinate, enemyFirstTime5, enemyBulletCount, \
        enemyContinueShooting5
    if enemySetCoordinate5:
        enemyFinalLocation5_x = player_x + 25
        enemyFinalLocation5_y = player_y + 7.5
        while abs(math.sqrt((enemyFinalLocation5_x - enemyX) ** 2 + (enemyFinalLocation5_y - enemyY) ** 2)) < 700:
            enemyFinalLocation5_x += (enemyFinalLocation5_x - enemyX) / 10
            enemyFinalLocation5_y += (enemyFinalLocation5_y - enemyY) / 10
        while abs(math.sqrt((enemyFinalLocation5_x - enemyX) ** 2 + (enemyFinalLocation5_y - enemyY) ** 2)) > 800:
            enemyFinalLocation5_x -= (enemyFinalLocation5_x - enemyX) / 10
            enemyFinalLocation5_y -= (enemyFinalLocation5_y - enemyY) / 10
        enemyFinalLocation5_x += random.randint(-enemyAccuracy, enemyAccuracy)
        enemyFinalLocation5_y += random.randint(-enemyAccuracy, enemyAccuracy)
        enemyRepetition5 = int(math.sqrt(
            (enemyFinalLocation5_x - enemyX) ** 2 + (enemyFinalLocation5_y - enemyY) ** 2) / enemyBulletVelocity)
        enemyOriginalRepetition5 = int(math.sqrt(
            (enemyFinalLocation5_x - enemyX) ** 2 + (enemyFinalLocation5_y - enemyY) ** 2) / enemyBulletVelocity)
        enemyTimes5 = 1
        enemySetCoordinate5 = False
        enemyBullet5InTheAir = True
        enemyFirstTime5 = True
        enemyBulletCount -= 1
    if enemyRepetition5 > 0:
        if enemyRepetition5 < enemyOriginalRepetition5 * 0.7 and enemyFirstTime5 and enemyReloadingTimer == 3:
            enemySetCoordinate = True
            enemyFirstTime5 = False
        length_x = abs(enemyFinalLocation5_x - enemyX) / enemyOriginalRepetition5
        length_y = abs(enemyFinalLocation5_y - enemyY) / enemyOriginalRepetition5
        if enemyFinalLocation5_x >= enemyX and enemyFinalLocation5_y >= enemyY:
            startX = enemyX + length_x + length_x * (enemyTimes5 - 1)
            startY = enemyY + length_y + length_y * (enemyTimes5 - 1)
            endX = enemyX + length_x + length_x * enemyTimes5
            endY = enemyY + length_y + length_y * enemyTimes5
        elif enemyFinalLocation5_x >= enemyX and enemyFinalLocation5_y <= enemyY:
            startX = enemyX + length_x + length_x * (enemyTimes5 - 1)
            startY = enemyY - length_y - length_y * (enemyTimes5 - 1)
            endX = enemyX + length_x + length_x * enemyTimes5
            endY = enemyY - length_y - length_y * enemyTimes5
        elif enemyFinalLocation5_x <= enemyX and enemyFinalLocation5_y <= enemyY:
            startX = enemyX - length_x - length_x * (enemyTimes5 - 1)
            startY = enemyY - length_y - length_y * (enemyTimes5 - 1)
            endX = enemyX - length_x - length_x * enemyTimes5
            endY = enemyY - length_y - length_y * enemyTimes5
        else:
            startX = enemyX - length_x - length_x * (enemyTimes5 - 1)
            startY = enemyY + length_y + length_y * (enemyTimes5 - 1)
            endX = enemyX - length_x - length_x * enemyTimes5
            endY = enemyY + length_y + length_y * enemyTimes5

        if enemyTimes5 == 1:
            bullet = individualBullet(enemyX, enemyY, endX, endY, enemyContinueShooting5)
            shootingEffect = pygame.transform.scale(pygame.image.load("ShootingEffect2.png"), (16, 10))
            screen.blit(shootingEffect, (enemyX, enemyY - 5))
        else:
            bullet = individualBullet(startX, startY, endX, endY, enemyContinueShooting5)

        if bullet.colliderect(playerSquare) and enemyContinueShooting5:
            health -= 75
            enemyContinueShooting5 = False
        enemyTimes5 += 1
        enemyRepetition5 -= 1
    if enemyRepetition5 <= 0:
        enemyBullet5InTheAir = False
        enemyContinueShooting5 = True


def resetEnemyShootingFunctions():
    global enemySetCoordinate, enemySetCoordinate2, enemySetCoordinate3, enemySetCoordinate4, enemySetCoordinate5, \
        enemyFinalLocation_x, enemyFinalLocation2_x, enemyFinalLocation3_x, enemyFinalLocation4_x, enemyFinalLocation5_x, \
        enemyFinalLocation_y, enemyFinalLocation2_y, enemyFinalLocation3_y, enemyFinalLocation4_y, enemyFinalLocation5_y, \
        enemyRepetition, enemyRepetition2, enemyRepetition3, enemyRepetition4, enemyRepetition5, enemyOriginalRepetition, \
        enemyOriginalRepetition2, enemyOriginalRepetition3, enemyOriginalRepetition4, enemyOriginalRepetition5, \
        enemyBulletInTheAir, enemyBullet2InTheAir, enemyBullet3InTheAir, enemyBullet4InTheAir, enemyBullet5InTheAir, \
        enemyTimes, enemyTimes2, enemyTimes3, enemyTimes4, enemyTimes5, enemyFirstTime, enemyFirstTime2, enemyFirstTime3, \
        enemyFirstTime4, enemyFirstTime5, enemyContinueShooting, enemyContinueShooting2, enemyContinueShooting3, \
        enemyContinueShooting4, enemyContinueShooting5
    enemySetCoordinate = True
    enemySetCoordinate2 = False
    enemySetCoordinate3 = False
    enemySetCoordinate4 = False
    enemySetCoordinate5 = False

    enemyFinalLocation_x = 0
    enemyFinalLocation2_x = 0
    enemyFinalLocation3_x = 0
    enemyFinalLocation4_x = 0
    enemyFinalLocation5_x = 0

    enemyFinalLocation_y = 0
    enemyFinalLocation2_y = 0
    enemyFinalLocation3_y = 0
    enemyFinalLocation4_y = 0
    enemyFinalLocation5_y = 0

    enemyRepetition = 0
    enemyRepetition2 = 0
    enemyRepetition3 = 0
    enemyRepetition4 = 0
    enemyRepetition5 = 0

    enemyOriginalRepetition = 0
    enemyOriginalRepetition2 = 0
    enemyOriginalRepetition3 = 0
    enemyOriginalRepetition4 = 0
    enemyOriginalRepetition5 = 10

    enemyBulletInTheAir = False
    enemyBullet2InTheAir = False
    enemyBullet3InTheAir = False
    enemyBullet4InTheAir = False
    enemyBullet5InTheAir = False

    enemyTimes = 1
    enemyTimes2 = 1
    enemyTimes3 = 1
    enemyTimes4 = 1
    enemyTimes5 = 1

    enemyFirstTime = False
    enemyFirstTime2 = False
    enemyFirstTime3 = False
    enemyFirstTime4 = False
    enemyFirstTime5 = False

    enemyContinueShooting = True
    enemyContinueShooting2 = True
    enemyContinueShooting3 = True
    enemyContinueShooting4 = True
    enemyContinueShooting5 = True
# enemy machine gun shooting functions


def enemyTankShootingFunction(enemyX, enemyY):
    global enemy2SetCoordinate, enemy2BulletInTheAir, enemy2FinalLocation_x, enemy2FinalLocation_y, playerSquare, health, \
        enemy2Repetition, enemy2Times, enemy2OriginalRepetition, enemy2ContinueShooting, enemy2ReloadingTimer, enemy2Accuracy

    if enemy2SetCoordinate:
        enemy2FinalLocation_x = player_x + 25
        enemy2FinalLocation_y = player_y + 7.5
        while abs(math.sqrt((enemy2FinalLocation_x - enemyX) ** 2 + (enemy2FinalLocation_y - enemyY) ** 2)) < 900:
            enemy2FinalLocation_x += (enemy2FinalLocation_x - enemyX) / 10
            enemy2FinalLocation_y += (enemy2FinalLocation_y - enemyY) / 10
        while abs(math.sqrt((enemy2FinalLocation_x - enemyX) ** 2 + (enemy2FinalLocation_y - enemyY) ** 2)) > 1000:
            enemy2FinalLocation_x -= (enemy2FinalLocation_x - enemyX) / 10
            enemy2FinalLocation_y -= (enemy2FinalLocation_y - enemyY) / 10
        enemy2FinalLocation_x += random.randint(-enemy2Accuracy, enemy2Accuracy)
        enemy2FinalLocation_y += random.randint(-enemy2Accuracy, enemy2Accuracy)
        enemy2Repetition = int(math.sqrt(
            (enemy2FinalLocation_x - enemyX) ** 2 + (enemy2FinalLocation_y - enemyY) ** 2) / enemy2BulletVelocity)
        enemy2OriginalRepetition = int(math.sqrt(
            (enemy2FinalLocation_x - enemyX) ** 2 + (enemy2FinalLocation_y - enemyY) ** 2) / enemy2BulletVelocity)
        enemy2Times = 1
        enemy2SetCoordinate = False
        enemy2BulletInTheAir = True
        enemy2ReloadingTimer = 0
    if enemy2Repetition > 0:
        length_x = abs(enemy2FinalLocation_x - enemyX) / enemy2OriginalRepetition
        length_y = abs(enemy2FinalLocation_y - enemyY) / enemy2OriginalRepetition
        if enemy2FinalLocation_x >= enemyX and enemy2FinalLocation_y >= enemyY:
            startX = enemyX + length_x + length_x * (enemy2Times - 1)
            startY = enemyY + length_y + length_y * (enemy2Times - 1)
            endX = enemyX + length_x + length_x * enemy2Times
            endY = enemyY + length_y + length_y * enemy2Times
        elif enemy2FinalLocation_x >= enemyX and enemy2FinalLocation_y <= enemyY:
            startX = enemyX + length_x + length_x * (enemy2Times - 1)
            startY = enemyY - length_y - length_y * (enemy2Times - 1)
            endX = enemyX + length_x + length_x * enemy2Times
            endY = enemyY - length_y - length_y * enemy2Times
        elif enemy2FinalLocation_x <= enemyX and enemy2FinalLocation_y <= enemyY:
            startX = enemyX - length_x - length_x * (enemy2Times - 1)
            startY = enemyY - length_y - length_y * (enemy2Times - 1)
            endX = enemyX - length_x - length_x * enemy2Times
            endY = enemyY - length_y - length_y * enemy2Times
        else:
            startX = enemyX - length_x - length_x * (enemy2Times - 1)
            startY = enemyY + length_y + length_y * (enemy2Times - 1)
            endX = enemyX - length_x - length_x * enemy2Times
            endY = enemyY + length_y + length_y * enemy2Times
        if enemy2Times == 1:
            bullet = pygame.draw.line(screen, red, (enemyX, enemyY), (endX, endY), 2)
            shootingEffect = pygame.transform.scale(pygame.image.load("ShootingEffect2.png"), (16, 10))
            screen.blit(shootingEffect, (enemyX, enemyY - 5))
        else:
            if enemy2ContinueShooting:
                bullet = pygame.draw.line(screen, red, (startX, startY), (endX, endY), 2)
            else:
                bullet = pygame.Rect(startX, startY, 100, 100)
        if bullet.colliderect(playerSquare) and enemy2ContinueShooting:
            health -= 1500
            enemy2ContinueShooting = False
        enemy2Times += 1
        enemy2Repetition -= 1
    if enemy2Repetition <= 0:
        enemy2BulletInTheAir = False
        enemy2ContinueShooting = True
# enemy tank shooting function


def enemyMissileShootingFunction(enemyX, enemyY, targetX, targetY):
    global health, enemy3SetCoordinate, missile_x, missile_y, enemy3ContinueShooting, enemy3BulletInTheAir, enemy3Timer, \
        enemy3Time, enemy3ReloadingTimer, missileRect, currentSpeed, lockedOn
    if enemy3SetCoordinate:
        missile_x = enemyX
        missile_y = enemyY
        enemy3BulletInTheAir = True
        enemy3ContinueShooting = True
        enemy3SetCoordinate = False
        lockedOn = False
        enemy3Timer = 0
    if enemy3Timer != enemy3Time and not enemy3SetCoordinate:
        if enemy3Timer >= 2 / 5:
            for i in range(10):
                if targetX * 0.9 < missile_x < targetX * 1.1 and targetY * 0.9 < missile_y < targetY * 1.1:
                    lockedOn = True
                if missile_x < targetX:
                    missile_x += (7 - (currentSpeed * 0.5)) / 10
                if missile_x > targetX and not lockedOn:
                    missile_x -= (7 + (currentSpeed * 0.5)) / 10
                if missile_y < targetY:
                    missile_y += 5 / 10
                if missile_y > targetY:
                    missile_y -= 5 / 10
                if lockedOn:
                    missile_x += (7 - (currentSpeed * 0.5)) / 10
        else:
            rotatedMissile = pygame.transform.rotate(missile, 180)
            missile_x -= 7
            missile_y -= 2.5
        if enemy3ContinueShooting:
            if not lockedOn:
                if targetX < missile_x and targetY < missile_y:
                    degrees = 180 - (57.2958 * (math.atan(abs((enemyY - targetY) / (enemyX - targetX)))))
                elif targetX > missile_x and targetY < missile_y:
                    degrees = 57.2958 * (math.atan(abs((enemyY - targetY) / (enemyX - targetX))))
                elif targetX > missile_x and targetY > missile_y:
                    degrees = 180 + (57.2958 * (math.atan(abs((enemyY - targetY) / (enemyX - targetX)))))
                else:
                    degrees = 360 - (57.2958 * (math.atan(abs((enemyY - targetY) / (enemyX - targetX)))))
            else:
                degrees = 0
            rotatedMissile = pygame.transform.rotate(missile, degrees)
            screen.blit(rotatedMissile, (missile_x, missile_y))
        if playerSquare.colliderect(missileRect) and enemy3ContinueShooting:
            health -= 1000
            enemy3ContinueShooting = False
    if enemy3Timer == enemy3Time:
        enemy3ContinueShooting = False
        enemy3BulletInTheAir = False
        enemy3ReloadingTimer = 0
#  enemy Sea-ram shooting function


def healthBar(x, y, maximumHealth, currentHealth, length, divider):
    color = green
    if currentHealth >= maximumHealth / 2:
        color = green
    elif currentHealth >= maximumHealth / 4:
        color = yellow
    else:
        color = red
    emptyBar = pygame.Rect(x + 5, y - 5, length - 10, 2)
    playerHealthBar = pygame.Rect(x + 5, y - 5, currentHealth / divider, 2)
    pygame.draw.rect(screen, black, emptyBar)
    pygame.draw.rect(screen, color, playerHealthBar)
#  healthbar for all assets in game


def speedBar(current, minimum):
    screen.blit(myFont.render("Speed:", False, black), (850, 35))
    pygame.draw.rect(screen, yellow, (950, 40, (current - minimum) * 70, 15))
# speed bar for players to know how fast they are going


def changingSpeed():
    global increasingSpeed, decreasingSpeed, currentSpeed, minSpeed, maxSpeed
    if increasingSpeed:
        if currentSpeed <= maxSpeed:
            currentSpeed += 0.1
            return currentSpeed
        else:
            currentSpeed = maxSpeed
            increasingSpeed = False
    if decreasingSpeed:
        if currentSpeed >= minSpeed:
            currentSpeed -= 0.1
        else:
            currentSpeed = minSpeed
            decreasingSpeed = False
#   if player is changing speed, this function does it for them


while True:
    clock.tick(45)
    mousePosition = pygame.mouse.get_pos()
    fpsCounter += 1
    if fpsCounter == 1:
        machineGunReloadingTimer += 1 / 45
        takeOffTimer += 1 / 45
        enemyReloadingTimer += 1 / 45
        enemy2ReloadingTimer += 1 / 45
        enemy3ReloadingTimer += 1 / 45
        if enemy3BulletInTheAir:
            enemy3Timer += 1 / 45
        fpsCounter = 0
    if machineGunReloadTime - 0.1 < machineGunReloadingTimer < machineGunReloadTime:
        bulletCount = 50
        resetShootingFunctions()
    if machineGunReloadingTimer > machineGunReloadTime:
        machineGunReloadingTimer = machineGunReloadTime
    if takeOffTimer > 3:
        takeOffTimer = 3
    if enemyReloadTime - 0.1 < enemyReloadingTimer < enemyReloadTime:
        enemyBulletCount = 50
        resetEnemyShootingFunctions()
    if enemyReloadingTimer > enemyReloadTime:
        enemyReloadingTimer = 3
    if enemy2ReloadTime - 0.1 < enemy2ReloadingTimer < enemy2ReloadTime:
        enemy2SetCoordinate = True
    if enemy2ReloadingTimer > enemy2ReloadTime:
        enemy2ReloadingTimer = enemy2ReloadTime
    if enemy3ReloadTime - 0.1 < enemy3ReloadingTimer < enemy3ReloadTime:
        enemy3SetCoordinate = True
    if enemy3ReloadingTimer > enemy3ReloadTime:
        enemy3ReloadingTimer = enemy3ReloadTime
    if enemy3Timer >= enemy3Time:
        enemy3Timer = enemy3Time
    displayDollars(dollarSign)
    # timer and various effect that uses timer

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not victory and not defeat:
                if selectingFighter:
                    playerFighterType = fighterSelection(mousePosition[0], mousePosition[1])
                    if playerFighterType == F35 or playerFighterType == Su57 or playerFighterType == J20:
                        fighterInformationDisplay(playerFighterType)
                        selectingFighter = False
                        displayingFighterInformation = True
                elif displayingFighterInformation:
                    if backSquare.collidepoint(mousePosition):
                        displayingFighterInformation = False
                        moveImage(playerFighterType, 100, 100, True)
                        selectingFighter = True
                    if startSquare.collidepoint(mousePosition):
                        if playerFighterType == F35:
                            player = pygame.transform.scale(pygame.image.load("In Game F-35.png"), (50, 15))
                            maxHealth = 2000 + additionalHealth
                            health = 2000 + additionalHealth
                            maxSpeed = 5 + additionalHighSpeed
                            minSpeed = 2 + additionalLowSpeed
                            machineGunDamage = 200 + additionalDamage
                            machineGunReloadTime = 5
                            machineGunVelocity = 40
                            machineGunAccuracy = 50
                        elif playerFighterType == Su57:
                            player = pygame.transform.scale(pygame.image.load("In Game Su-57.png"), (50, 15))
                            maxHealth = 2500 + additionalHealth
                            health = 2500 + additionalHealth
                            maxSpeed = 6 + additionalHighSpeed
                            minSpeed = 3 + additionalLowSpeed
                            machineGunDamage = 200 + additionalDamage
                            machineGunReloadTime = 5
                            machineGunVelocity = 40
                            machineGunAccuracy = 50
                        elif playerFighterType == J20:
                            player = pygame.transform.scale(pygame.image.load("In Game J-20.png"), (50, 15))
                            maxHealth = 3500 + additionalHealth
                            health = 3500 + additionalHealth
                            maxSpeed = 4 + additionalHighSpeed
                            minSpeed = 3 + additionalLowSpeed
                            machineGunDamage = 350 + additionalDamage
                            machineGunReloadTime = 5
                            machineGunVelocity = 35
                            machineGunAccuracy = 85
                        displayingFighterInformation = False
                        playingGame = True
                        takeOff = True
                        takeOffTimer = 0
                        player_x = 0
                        player_y = 675
                elif playingGame and machineGunReloadingTimer == 5:
                    shooting = True
        if event.type == pygame.MOUSEBUTTONUP:
            if playingGame:
                shooting = False
        if event.type == pygame.KEYDOWN:
            if not victory and not defeat:
                if event.key == pygame.K_UP:
                    increasingSpeed = True
                if event.key == pygame.K_DOWN:
                    decreasingSpeed = True
                if event.key == pygame.K_w:
                    if not takeOff:
                        player_y_change -= 2
                if event.key == pygame.K_a:
                    if not takeOff:
                        player_x_change -= 3
                if event.key == pygame.K_s:
                    if not takeOff:
                        player_y_change += 2
                if event.key == pygame.K_d:
                    if not takeOff:
                        player_x_change += 3
                if event.key == pygame.K_r:
                    if machineGunReloadingTimer == 5:
                        bulletCount = -1
                if event.key == pygame.K_1:
                    currentWeapon = "machineGun"
                if event.key == pygame.K_2:
                    print(maxHealth)
                    if playerFighterType == Su57:
                        currentWeapon = "Missile"
                    else:
                        currentWeapon = "Small Missile"
                if event.key == pygame.K_3:
                    if playerFighterType == J20:
                        currentWeapon = "Torpedo"
                    else:
                        currentWeapon = "Bomb"
                if event.key == pygame.K_4:
                    if playerFighterType == F35:
                        currentWeapon = "Missile"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                increasingSpeed = False
            if event.key == pygame.K_DOWN:
                decreasingSpeed = False
            player_x_change = 0
            player_y_change = 0
    # keys
    player_y += player_y_change
    player_x += player_x_change
    # change player's position after they moves
    if selectingFighter:
        screen.blit(myFont.render("Please select a fighter", False, white), (550, 75))
        if not background:
            displayBackgroundInformation()
        preEditedImage1 = pygame.image.load("F-35.png")
        preEditedImage2 = pygame.image.load("Su-57.png")
        preEditedImage3 = pygame.image.load("J-20.png")
        F35 = pygame.transform.scale(preEditedImage1, (250, 100))
        Su57 = pygame.transform.scale(preEditedImage2, (250, 100))
        J20 = pygame.transform.scale(preEditedImage3, (250, 100))
        screen.blit(missile, (250, 250))
        screen.blit(F35, (250, 250))
        screen.blit(Su57, (550, 250))
        screen.blit(J20, (850, 250))

        upgradeHealthButton = pygame.draw.rect(screen, white, (150, 450, 250, 100))
        upgradeDamageButton = pygame.draw.rect(screen, white, (450, 450, 250, 100))
        upgradeMinSpeedButton = pygame.draw.rect(screen, white, (750, 450, 250, 100))
        upgradeMaxSpeedButton = pygame.draw.rect(screen, white, (1050, 450, 250, 100))

        upgradeHealthText = myFighterExplanationFont.render("Upgrade Health (" + str(int(additionalHealth / 500)) + ") for 10000 dollars", False, black)
        upgradeDamageText = myFighterExplanationFont.render("Upgrade Damage (" + str(int(additionalDamage / 50)) + ") for 10000 dollars", False, black)
        upgradeMinSpeedText = myFighterExplanationFont.render("Upgrade Hover (" + str(int(-additionalLowSpeed * 2)) + ") for 10000 dollars", False, black)
        upgradeMaxSpeedText = myFighterExplanationFont.render("Upgrade Speed (" + str(int(additionalHighSpeed * 2)) + ") for 10000 dollars", False, black)

        screen.blit(upgradeHealthText, (150, 490))
        screen.blit(upgradeDamageText, (450, 490))
        screen.blit(upgradeMinSpeedText, (750, 490))
        screen.blit(upgradeMaxSpeedText, (1050, 490))

        pygame.display.update()
        screen.fill(black)
    # process of selecting fighter

    elif displayingFighterInformation:
        backButton = pygame.transform.scale(pygame.image.load("BackButton.jpeg"), (100, 50))
        screen.blit(backButton, (60, height - 75))
        backSquare = pygame.Rect(50, height - 75, 100, 50)

        startButton = pygame.transform.scale(pygame.image.load("StartButton.jpeg"), (100, 100))
        screen.blit(startButton, (width - 200, height - 100))
        startSquare = pygame.Rect(width - 200, height - 100, 100, 100)
    # Process of displaying fighter's background information

    elif playingGame:
        if takeOff:
            victory_x = 14000
            enemy_x = random.randint(2000, 2500)
            enemy2_x = random.randint(2000, 2500)
            enemy3_x = random.randint(2000, 2500)
            shooting = False
            takeOffTime = myTitleFont.render(str(3 - int(takeOffTimer)), False, black)
            if takeOffTimer != 3:
                screen.blit(takeOffTime, (650, 350))
            else:
                player_x += 3
                if player_x > 125:
                    player_x += 2
                    player_y -= 1
                if player_y < 500:
                    takeOff = False
        else:
            if enemyType == 1:
                enemy_x -= currentSpeed * 0.75
            else:
                enemy_x -= currentSpeed + 6
            runWay_x -= currentSpeed * 0.75
            enemy2_x -= currentSpeed * 0.75 + 0.75
            enemy3_x -= currentSpeed * 0.75

            tree_x -= currentSpeed * 0.75
            tree2_x -= currentSpeed * 0.75
            tree3_x -= currentSpeed * 0.75
            tree4_x -= currentSpeed * 0.75
            tree5_x -= currentSpeed * 0.75
            tree6_x -= currentSpeed * 0.75

            cloud_x -= currentSpeed * 0.75
            cloud2_x -= currentSpeed * 0.75
            cloud3_x -= currentSpeed * 0.75
            cloud4_x -= currentSpeed * 0.75
            cloud5_x -= currentSpeed * 0.75

            victory_x -= currentSpeed * 0.75

        if enemy_x <= -50:
            enemyType = random.randint(1, 2)
            enemy_x = random.randint(2000, 2500)
            if enemyType == 1:
                enemyMaxHealth = 1500
                enemyHealth = 1500
                enemy_y = 700 - 26
                enemySquare = pygame.Rect(enemy_x, enemy_y, 24, 26)
                enemy = pygame.transform.scale(pygame.image.load("Phalanx CIWS.png"), (24, 26))
            else:
                enemyMaxHealth = 1000
                enemyHealth = 1000
                enemy_y = random.randint(50, 500)
                enemySquare = pygame.Rect(enemy_x, enemy_y, 50, 15)
                enemy = pygame.transform.scale(pygame.image.load("J-10.png"), (50, 15))
        if enemy2_x <= -50:
            enemy2Health = enemy2MaxHealth
            enemy2_x = random.randint(2000, 3000)
        if enemy3_x <= -50:
            enemy3Health = enemy3MaxHealth
            enemy3_x = random.randint(2000, 3000)

        if tree_x <= -200:
            tree_x = random.randint(2000, 5000)
        if tree2_x <= -200:
            tree2_x = random.randint(2000, 5000)
        if tree3_x <= -200:
            tree3_x = random.randint(2000, 5000)
        if tree4_x <= -200:
            tree4_x = random.randint(2000, 5000)
        if tree5_x <= -200:
            tree5_x = random.randint(2000, 5000)
        if tree6_x <= -200:
            tree6_x = random.randint(2000, 5000)

        if cloud_x <= -500:
            cloud_x = random.randint(2000, 5000)
            cloud_y = random.randint(50, 150)
        if cloud2_x <= -500:
            cloud2_x = random.randint(2000, 5000)
            cloud2_y = random.randint(50, 150)
        if cloud3_x <= -500:
            cloud3_x = random.randint(2000, 5000)
            cloud3_y = random.randint(50, 150)
        if cloud4_x <= -500:
            cloud4_x = random.randint(2000, 5000)
            cloud4_y = random.randint(50, 150)
        if cloud5_x <= -500:
            cloud5_x = random.randint(2000, 5000)
            cloud5_y = random.randint(50, 150)

        ground = pygame.Rect(0, 700, 1400, 50)
        pygame.draw.rect(screen, brown, ground)

        runWay = pygame.Rect(runWay_x, 690, 300, 100)
        pygame.draw.rect(screen, gray, runWay)

        screen.blit(tree, (tree_x, tree_y))
        screen.blit(tree2, (tree2_x, tree_y))
        screen.blit(tree3, (tree3_x, tree_y))
        screen.blit(tree4, (tree4_x, tree_y))
        screen.blit(tree5, (tree5_x, tree_y))
        screen.blit(tree6, (tree6_x, tree_y))

        screen.blit(cloud, (cloud_x, cloud_y))
        screen.blit(cloud2, (cloud2_x, cloud2_y))
        screen.blit(cloud3, (cloud3_x, cloud3_y))
        screen.blit(cloud4, (cloud4_x, cloud4_y))
        screen.blit(cloud5, (cloud5_x, cloud5_y))

        victoryRect = pygame.Rect(victory_x, 50, 10, 650)
        pygame.draw.rect(screen, green, victoryRect)

        healthBar(player_x, player_y, maxHealth, health, 50, maxHealth / 40)
        if enemyType == 1:
            healthBar(enemy_x, enemy_y, enemyMaxHealth, enemyHealth, 24, enemyMaxHealth / 14)
        else:
            healthBar(enemy_x, enemy_y, enemyMaxHealth, enemyHealth, 50, enemyMaxHealth / 40)
        healthBar(enemy2_x, enemy2_y, enemy2MaxHealth, enemy2Health, 44, enemy2MaxHealth / 34)
        healthBar(enemy3_x, enemy3_y, enemy3MaxHealth, enemy3Health, 24, enemy3MaxHealth / 14)
        speedBar(currentSpeed, minSpeed)
        changingSpeed()

        screen.blit(enemy, (enemy_x, enemy_y))
        enemySquare = pygame.Rect(enemy_x, enemy_y, 24, 26)

        screen.blit(enemy2, (enemy2_x, enemy2_y))
        enemy2Square = pygame.Rect(enemy2_x, enemy2_y, 44, 14)

        screen.blit(enemy3, (enemy3_x, enemy3_y))
        enemy3Square = pygame.Rect(enemy3_x, enemy3_y, 24, 26)
        missileRect = pygame.Rect(missile_x, missile_y, 6.5, 1)

        enemyList[0] = enemySquare
        enemyList[1] = enemy2Square
        enemyList[2] = enemy3Square

        playerSquare = pygame.Rect(player_x, player_y, 50, 15)
        screen.blit(player, (player_x, player_y))

        if currentWeapon == "machineGun":
            if playerFighterType == J20:
                weaponType = myFont.render("ZPT-99 Machine Gun", False, black)
            else:
                weaponType = myFont.render("GAU-25 Machine Gun", False, black)

            if machineGunReloadingTimer == machineGunReloadTime:
                bullets = myFont.render("Ammunition: " + str(bulletCount), False, black)
            else:
                bullets = myFont.render("Reloading...", False, black)
            screen.blit(weaponType, (100, 15))
            screen.blit(bullets, (100, 40))

        else:
            shooting = False
        if playerSquare.colliderect(ground):
            health = 0
        health += 1
        if health > maxHealth:
            health = maxHealth
        if enemyHealth <= 0:
            resetEnemyShootingFunctions()
            money += 1000
            enemyType = random.randint(1,2)
            if enemyType == 1:
                enemyMaxHealth = 1500
                enemyHealth = 1500
                enemy_y = 700 - 26
                enemySquare = pygame.Rect(enemy_x, enemy_y, 24, 26)
                enemy = pygame.transform.scale(pygame.image.load("Phalanx CIWS.png"), (24, 26))
            else:
                enemyMaxHealth = 1000
                enemyHealth = 1000
                enemy_y = random.randint(50, 500)
                enemySquare = pygame.Rect(enemy_x, enemy_y, 50, 15)
                enemy = pygame.transform.scale(pygame.image.load("J-10.png"), (50, 15))
            enemyBulletCount = 50
            enemyReloadingTimer = 3
            enemy_x = random.randint(2000, 2500)
        if enemy2Health <= 0:
            money += 2000
            enemy2SetCoordinate = True
            enemy2Health = enemy2MaxHealth
            enemy2ReloadingTimer = enemy2ReloadTime
            enemy2_x = random.randint(2000, 2500)
        if enemy3Health <= 0:
            money += 1000
            enemy3SetCoordinate = True
            enemy3Health = enemy3MaxHealth
            enemy3_x = random.randint(2000, 2500)

        if not victory:
            if player_x < 0:
                player_x = 0
            if player_x > width - 50:
                player_x = width - 50
            if player_y < 100:
                player_y = 100
            if player_y > height - 15:
                player_y = height - 15
        if currentSpeed > maxSpeed:
            currentSpeed = maxSpeed
        if currentSpeed < minSpeed:
            currentSpeed = minSpeed

        enemyRangeRect = pygame.Rect(enemy_x - 700, enemy_y - 700, 1400, 1400)
        enemy2RangeRect = pygame.Rect(enemy2_x - 750, enemy2_y - 750, 1500, 1500)
        enemy3RangeRect = pygame.Rect(enemy3_x - 750, enemy3_y - 750, 1500, 1500)
        if playerSquare.colliderect(enemyRangeRect) and enemyReloadingTimer == 3:
            enemyShooting = True
        else:
            enemyShooting = False

        if (playerSquare.colliderect(
                enemy2RangeRect) and enemy2ReloadingTimer == enemy2ReloadTime) or enemy2BulletInTheAir:
            enemyTankShootingFunction(enemy2_x, enemy2_y + 7)
        if playerSquare.colliderect(enemy3RangeRect) and (
                enemy3ReloadingTimer == enemy3ReloadTime) or enemy3BulletInTheAir:
            enemyMissileShootingFunction(enemy3_x, enemy3_y, player_x - 75, player_y + 10)

        if enemyShooting or enemyBulletInTheAir:
            if enemyRepetition5 < enemyOriginalRepetition5 * 0.8:
                enemyShootingFunction(enemy_x - 10, enemy_y + 11)
        if enemyShooting or enemyBullet2InTheAir:
            if enemyRepetition < enemyOriginalRepetition * 0.8:
                enemyShootingFunction2(enemy_x - 10, enemy_y + 11)
        if enemyShooting or enemyBullet3InTheAir:
            if enemyRepetition2 < enemyOriginalRepetition2 * 0.8:
                enemyShootingFunction3(enemy_x - 10, enemy_y + 11)
        if enemyShooting or enemyBullet4InTheAir:
            if enemyRepetition3 < enemyOriginalRepetition3 * 0.8:
                enemyShootingFunction4(enemy_x - 10, enemy_y + 11)
        if enemyShooting or enemyBullet5InTheAir:
            if enemyRepetition4 < enemyOriginalRepetition4 * 0.8:
                enemyShootingFunction5(enemy_x - 10, enemy_y + 11)
        if enemyBulletCount < 0:
            enemyReloadingTimer = 0
            enemyBulletCount = 0

        if shooting or bulletInTheAir:
            if repetition5 < originalRepetition5 * 0.7:
                shootingFunction(player_x + 50, player_y + 10)
        if shooting or bullet2InTheAir:
            if repetition < originalRepetition * 0.7:
                shootingFunction2(player_x + 50, player_y + 10)
        if shooting or bullet3InTheAir:
            if repetition2 < originalRepetition2 * 0.7:
                shootingFunction3(player_x + 50, player_y + 10)
        if shooting or bullet4InTheAir:
            if repetition3 < originalRepetition3 * 0.7:
                shootingFunction4(player_x + 50, player_y + 10)
        if shooting or bullet5InTheAir:
            if repetition4 < originalRepetition4 * 0.7:
                shootingFunction5(player_x + 50, player_y + 10)
        if bulletCount < 0:
            machineGunReloadingTimer = 0
            bulletCount = 0

        if player_y > 650:
            enemy2Accuracy = 50
        else:
            enemy2Accuracy = 500
        if health <= 0 and not victory:
            defeat = True
        if defeat:
            healthBar(player_x, player_y, maxHealth, health, 50, maxHealth / 40)
            displayDefeat = myTitleFont.render("Defeat", False, black)
            screen.blit(displayDefeat, (600, 300))
            explosion = pygame.transform.scale(pygame.image.load("Explosion.png"), (50, 15))
            screen.blit(explosion, (player_x, player_y))
            player_y += 5
            if player_y >= 700:
                defeat = False
                runWay_x = 0
                playingGame = False
                selectingFighter = True
                pygame.display.update()
                screen.fill(blue)
                time.sleep(2)
        if playerSquare.colliderect(victoryRect):
            victory = True
        if victory:
            displayVictory = myTitleFont.render("Victory", False, black)
            screen.blit(displayVictory, (600, 300))
            player_x += 10
            if player_x >= 1500:
                victory = False
                money += 5000
                runWay_x = 0
                playingGame = False
                selectingFighter = True
                pygame.display.update()
                screen.fill(blue)
                time.sleep(2)
        pygame.display.update()
        screen.fill(blue)
#  the main gameplay
