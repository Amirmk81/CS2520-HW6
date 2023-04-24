import pygame
import math


# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Major League Soccer"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
refresh_rate = 60

# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (52, 166, 36)
BLUE = (29, 116, 248)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
DARK_BLUE = (18, 0, 91)
DARK_GREEN = (0, 94, 0)
GRAY = (130, 130, 130)
YELLOW = (255, 255, 110)
SILVER = (200, 200, 200)
DAY_GREEN = (41, 129, 29)
NIGHT_GREEN = (0, 64, 0)
BRIGHT_YELLOW = (255, 244, 47)
NIGHT_GRAY = (104, 98, 115)
ck = (127, 33, 33)

DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

SEE_THROUGH = pygame.Surface((800, 180))
SEE_THROUGH.set_alpha(150)
SEE_THROUGH.fill((124, 118, 135))



#object prefabs
def drawGoal():

    s = 1; #scale

    x = 320
    x = x-320

    y = 200
    y = y-200



    #goalbox
    pygame.draw.rect(screen, WHITE, [320+x, 140+y, 160*s, 80*s], 5*s)
    pygame.draw.line(screen, WHITE, [340+x, 200+y], [460+x, 200+y], 3*s)
    pygame.draw.line(screen, WHITE, [320+x, 220+y], [340+x, 200+y], 3*s)
    pygame.draw.line(screen, WHITE, [480+x, 220+y], [460+x, 200+y], 3*s)
    pygame.draw.line(screen, WHITE, [320+x, 140+y], [340+x, 200+y], 3*s)
    pygame.draw.line(screen, WHITE, [480+x, 140+y], [460+x, 200+y], 3*s)

    #net
    pygame.draw.line(screen, WHITE, [325+x, 140+y], [341+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [330+x, 140+y], [344+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [335+x, 140+y], [347+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [340+x, 140+y], [350+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [345+x, 140+y], [353+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [350+x, 140+y], [356+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [355+x, 140+y], [359+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [360+x, 140+y], [362+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [364+x, 140+y], [365+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [368+x, 140+y], [369+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [372+x, 140+y], [373+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [376+x, 140+y], [377+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [380+x, 140+y], [380+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [384+x, 140+y], [384+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [388+x, 140+y], [388+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [392+x, 140+y], [392+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [396+x, 140+y], [396+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [400+x, 140+y], [400+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [404+x, 140+y], [404+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [408+x, 140+y], [408+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [412+x, 140+y], [412+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [416+x, 140+y], [416+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [420+x, 140+y], [420+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [424+x, 140+y], [423+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [428+x, 140+y], [427+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [432+x, 140+y], [431+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [440+x, 140+y], [438+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [445+x, 140+y], [441+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [450+x, 140+y], [444+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [455+x, 140+y], [447+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [460+x, 140+y], [450+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [465+x, 140+y], [453+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [470+x, 140+y], [456+x, 200+y], 1*s)
    pygame.draw.line(screen, WHITE, [475+x, 140+y], [459+x, 200+y], 1*s)

    #net part 2
    pygame.draw.line(screen, WHITE, [320+x, 140+y], [324+x, 216+y], 1*s)
    pygame.draw.line(screen, WHITE, [320+x, 140+y], [326+x, 214+y], 1*s)
    pygame.draw.line(screen, WHITE, [320+x, 140+y], [328+x, 212+y], 1*s)
    pygame.draw.line(screen, WHITE, [320+x, 140+y], [330+x, 210+y], 1*s)
    pygame.draw.line(screen, WHITE, [320+x, 140+y], [332+x, 208+y], 1*s)
    pygame.draw.line(screen, WHITE, [320+x, 140+y], [334+x, 206+y], 1*s)
    pygame.draw.line(screen, WHITE, [320+x, 140+y], [336+x, 204+y], 1*s)
    pygame.draw.line(screen, WHITE, [320+x, 140+y], [338+x, 202+y], 1*s)

    #net part 3
    pygame.draw.line(screen, WHITE, [480+x, 140+y], [476+x, 216+y], 1*s)
    pygame.draw.line(screen, WHITE, [480+x, 140+y], [474+x, 214+y], 1*s)
    pygame.draw.line(screen, WHITE, [480+x, 140+y], [472+x, 212+y], 1*s)
    pygame.draw.line(screen, WHITE, [480+x, 140+y], [470+x, 210+y], 1*s)
    pygame.draw.line(screen, WHITE, [480+x, 140+y], [468+x, 208+y], 1*s)
    pygame.draw.line(screen, WHITE, [480+x, 140+y], [466+x, 206+y], 1*s)
    pygame.draw.line(screen, WHITE, [480+x, 140+y], [464+x, 204+y], 1*s)
    pygame.draw.line(screen, WHITE, [480+x, 140+y], [462+x, 202+y], 1*s)

    #net part 4
    pygame.draw.line(screen, WHITE, [324+x, 144+y], [476+x, 144+y], 1*s)
    pygame.draw.line(screen, WHITE, [324+x, 148+y], [476+x, 148+y], 1*s)
    pygame.draw.line(screen, WHITE, [324+x, 152+y], [476+x, 152+y], 1*s)
    pygame.draw.line(screen, WHITE, [324+x, 156+y], [476+x, 156+y], 1*s)
    pygame.draw.line(screen, WHITE, [324+x, 160+y], [476+x, 160+y], 1*s)
    pygame.draw.line(screen, WHITE, [324+x, 164+y], [476+x, 164+y], 1*s)
    pygame.draw.line(screen, WHITE, [324+x, 168+y], [476+x, 168+y], 1*s)
    pygame.draw.line(screen, WHITE, [324+x, 172+y], [476+x, 172+y], 1*s)
    pygame.draw.line(screen, WHITE, [324+x, 176+y], [476+x, 176+y], 1*s)
    pygame.draw.line(screen, WHITE, [335+x, 180+y], [470+x, 180+y], 1*s)
    pygame.draw.line(screen, WHITE, [335+x, 184+y], [465+x, 184+y], 1*s)
    pygame.draw.line(screen, WHITE, [335+x, 188+y], [465+x, 188+y], 1*s)
    pygame.draw.line(screen, WHITE, [335+x, 192+y], [465+x, 192+y], 1*s)
    pygame.draw.line(screen, WHITE, [335+x, 196+y], [465+x, 196+y], 1*s)


def drawScoreBoard():

    s = 1; #scale

    x = 300
    x = x-300

    y = 40
    y = y-40

    #score board pole
    pygame.draw.rect(screen, GRAY, [390+x, 120+y, 20*s, 70*s])

    #score board
    pygame.draw.rect(screen, BLACK, [300+x, 40+y, 200*s, 90*s])
    pygame.draw.rect(screen, WHITE, [302+x, 42+y, 198*s, 88*s], 2*s)


light_color = RED
def SetLightColor(c):
    global light_color
    light_color = c

def drawLights(x, y, s):

    x = x-110

    y = y-20

    #light pole
    pygame.draw.rect(screen, GRAY, [150+x, 60+y, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [150+x, 195+y, 20, 10])

    #lights
    pygame.draw.line(screen, GRAY, [110+x, 60+y], [210+x, 60+y], 2)
    pygame.draw.ellipse(screen, light_color, [110+x, 40+y, 20, 20])
    pygame.draw.ellipse(screen, light_color, [130+x, 40+y, 20, 20])
    pygame.draw.ellipse(screen, light_color, [150+x, 40+y, 20, 20])
    pygame.draw.ellipse(screen, light_color, [170+x, 40+y, 20, 20])
    pygame.draw.ellipse(screen, light_color, [190+x, 40+y, 20, 20])
    pygame.draw.line(screen, GRAY, [110+x, 40+y], [210+x, 40+y], 2)
    pygame.draw.ellipse(screen, light_color, [110+x, 20+y, 20, 20])
    pygame.draw.ellipse(screen, light_color, [130+x, 20+y, 20, 20])
    pygame.draw.ellipse(screen, light_color, [150+x, 20+y, 20, 20])
    pygame.draw.ellipse(screen, light_color, [170+x, 20+y, 20, 20])
    pygame.draw.ellipse(screen, light_color, [190+x, 20+y, 20, 20])
    pygame.draw.line(screen, GRAY, [110+x, 20+y], [210+x, 20+y], 2)


def drawFlagR(x,y,s):
    x = x-125
    y = y-190
    #corner flag right
    pygame.draw.line(screen, BRIGHT_YELLOW, [140+x, 220+y], [135+x, 190+y], 3*s)
    pygame.draw.polygon(screen, RED, [[132+x, 190+y], [125+x, 196+y], [135+x, 205+y]])

def drawFlagL(x,y,s):
    x = x-660
    y = y-190
    #corner flag left
    pygame.draw.line(screen, BRIGHT_YELLOW, [660+x, 220+y], [665+x, 190+y], 3*s)
    pygame.draw.polygon(screen, RED, [[668+x, 190+y], [675+x, 196+y], [665+x, 205+y]])

def drawStandsR(x,y,s):
    x = x-680
    y = y-100
    #stands right
    pygame.draw.polygon(screen, RED, [[680+x, 220+y], [800+x, 340+y], [800+x, 290+y], [680+x, 180+y]])
    pygame.draw.polygon(screen, WHITE, [[680+x, 180+y], [800+x, 100+y], [800+x, 290+y]])

def drawStandsL(x,y,s):
    x=x-0
    y=y-100
    pygame.draw.polygon(screen, RED, [[120+x, 220+y], [0+x, 340+y], [0+x, 290+y], [120+x, 180+y]])
    pygame.draw.polygon(screen, WHITE, [[120+x, 180+y], [0+x, 100+y], [0+x, 290+y]])

def drawFence(x,y,length,height):
    '''fence'''
    for x in range(5, length, 30):
        pygame.draw.polygon(screen, NIGHT_GRAY, [[x + 2, y], [x + 2, y + height], [x, y + height], [x, y]])

    for x in range(5, length, 3):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x, y + height], 1)

    for y in range(170, 170+height, 4):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x +length, y], 1)


def drawField(x,y,s):
    y=y-220
    #out of bounds lines
    pygame.draw.line(screen, WHITE, [0+x, 580+y], [800+x, 580+y], 5*s)
    #left
    pygame.draw.line(screen, WHITE, [0+x, 360+y], [140+x, 220+y], 5*s)
    pygame.draw.line(screen, WHITE, [140+x, 220+y], [660+x, 220+y], 3*s)
    #right
    pygame.draw.line(screen, WHITE, [660+x, 220+y], [800+x, 360+y], 5*s)

    #safety circle
    pygame.draw.ellipse(screen, WHITE, [240+x, 500+y, 320, 160], 5)

    #18 yard line goal box
    pygame.draw.line(screen, WHITE, [260+x, 220+y], [180+x, 300+y], 5*s)
    pygame.draw.line(screen, WHITE, [180+x, 300+y], [620+x, 300+y], 3*s)
    pygame.draw.line(screen, WHITE, [620+x, 300+y], [540+x, 220+y], 5*s)

    #arc at the top of the goal box
    pygame.draw.arc(screen, WHITE, [330+x, 280+y, 140, 40], math.pi, 2 * math.pi, 5)

    #6 yard line goal box
    pygame.draw.line(screen, WHITE, [310+x, 220+y], [270+x, 270+y], 3*s)
    pygame.draw.line(screen, WHITE, [270+x, 270+y], [530+x, 270+y], 2*s)
    pygame.draw.line(screen, WHITE, [530+x, 270+y], [490+x, 220+y], 3*s)

    


cloud_color = RED

def SetCloudColor(c):
    global cloud_color
    cloud_color = c

def draw_cloud(x, y):
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])

