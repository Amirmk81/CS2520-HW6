# Imports
import pygame
import math
import random

from graphics import*

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Config
lights_on = True
day = True

stars = []
for n in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 200)
    r = random.randrange(1, 2)
    stars.append([x, y, r, r])

clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0, 150)
    clouds.append([x, y])

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_d:
                day = not day

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now '''
    if lights_on:
        SetLightColor(YELLOW)
    else:
        SetLightColor(SILVER)

    if day:
        sky_color = BLUE
        field_color = GREEN
        stripe_color = DAY_GREEN
        SetCloudColor(WHITE)
    else:
        sky_color = DARK_BLUE
        field_color = DARK_GREEN
        stripe_color = NIGHT_GREEN
        SetCloudColor(NIGHT_GRAY)

    for c in clouds:
        c[0] -= 0.5

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 150)

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)

    if not day:
    #stars
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)


    #draw ground
    pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])






    if day:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40])
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])



    for c in clouds:
        draw_cloud(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0))


    drawFence(0,170,800,15)

    drawScoreBoard()

    drawGoal()


    drawLights(110,20,1)

    drawLights(590,20,1)

    drawFlagR(125,190,1)
    drawFlagL(660,190,1)

    drawStandsR(680,100,1)
    drawStandsL(0,100,1)

    drawField(0,220,1)
    #people




    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))

    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
