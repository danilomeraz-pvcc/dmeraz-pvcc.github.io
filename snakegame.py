import pygame
import time
import random
import sys

pygame.init()

width = 600
height = 400

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)


block_size = 20
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 30)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

def score_display(score):
    value = score_font.render("Score: " + str(score), True, white)
    screen.blit(value, [10,10])

def message(msg, color, y_displace=0):
    msg = font_style.render(msg, True, color)
    screen.blit(msg, [width / 6, height / 3 + y_displace])

def draw_snake(snake_blocks):
    for block in snake_blocks:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])
        

def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_blocks = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size


    while not game_over:

        while game_close:
            screen.fill(black)
            message("Game Over... Press Q to Quit or C to Play again", red)
            score_display(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        x += x_change
        y += y_change

        if x < 0 or x >= width or y < 0 or y >= height:
            game_over = True    


        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_blocks.append(snake_head)

        if len(snake_blocks) > snake_length:
            del snake_blocks[0]

        for block in snake_blocks[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_blocks)
        score_display(snake_length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
            snake_length += 1

        clock.tick(15)

    pygame.quit()
    quit()

game_loop()    
                
