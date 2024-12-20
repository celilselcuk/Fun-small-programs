import pygame
import random

pygame.init()

brown = [82, 50, 27]
white = [255, 255, 255]
red = [237, 22, 7]
blue = [5, 7, 99]
yellow = [201, 195, 10]
purple = [131, 5, 235]
green = [17, 184, 33]
orange = [255, 165, 0]
pink = [255, 105, 180]
cyan = [0, 255, 255]
magenta = [255, 0, 255]
light_blue = [173, 216, 230]
dark_green = [0, 100, 0]

deco_colours = [red, blue, yellow, purple, green, orange, pink, cyan, magenta, light_blue]


screen = pygame.display.set_mode((800, 650)) 
pygame.display.set_caption('Christmas Time')

x1,x2 = 250,520
y1,y2, y3 = 430,430, 250

snowflakes = []
tree_tip_x = []
tree_tip_y = []

check = False

def draw_tree(num, x1, x2, y1, y2, y3):
    if num >= 4:
        num = 3

    pygame.draw.rect(screen, brown, (360, 430, 50, 200 ))

    for i in range(0, num):
        if i == 0:
            x_change = 0
        else:
            x_change = 250*0.07*i 

        x1,x2 = x1+x_change, x2-x_change
        y3 -= 50

        if i == 0:
            y1,y2 = 430,430
        else:
            y1 -= 80
            y2 -= 80
        

        tree_tip_x.append(x1)
        tree_tip_x.append(x2)
        tree_tip_x.append(385)
        tree_tip_y.append(y1)
        tree_tip_y.append(y2)
        if num == 1:
            tree_tip_y.append(250)
        else:
            tree_tip_y.append(250-(50*(num)))
        pygame.draw.polygon(screen,dark_green, ((x1, y1), (x2, y2), (385, y3)))
    

def snow():
    x = random.randint(25, 775)
    y = 0
    num = random.randint(0,4)
    if num == random.randint(0,4):
        snowflakes.append([x, y])

def update_snowflakes():
    for snowflake in snowflakes:
        snowflake[1] += 0.2
        pygame.draw.circle(screen, white, (snowflake[0], snowflake[1]), random.randrange(1,4))
        if snowflake[1] > 550:
            screen.set_at((random.randrange(snowflake[0]-5, snowflake[0]+5), random.randrange(550, 600)), white)
            snowflakes.remove(snowflake)

def draw_deco(tree_tip_x, tree_tip_y, deco_colours):
    i = random.randint(0, 9)
    colour = deco_colours[i]

    for j in range(0, 9):
        pygame.draw.circle(screen, colour, (tree_tip_x[j], tree_tip_y[j]), 10)


running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    screen.fill(blue, (0, 0, 800, 550)) 
    if not check:
        pygame.draw.rect(screen, green, (0, 550, 800, 100))
        check = True
    snow()
    update_snowflakes()
    draw_tree(3, x1, x2, y1, y2, y3)
    draw_deco(tree_tip_x, tree_tip_y, deco_colours)
    
    pygame.display.flip()

pygame.quit()
