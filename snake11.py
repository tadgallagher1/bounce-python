
# Import package
import pygame 
import time 
import random  

# Initializes all of the imported Pygame 
# modules (returns a tuple indicating success and failure of initializations)
pygame.init()

dis_width = 600  
dis_height = 400

# Takes a tuple or a list as its parameter to 
# create a surface (tuple preferred)
dis = pygame.display.set_mode((dis_width, dis_height))

# This is the titile
pygame.display.set_caption('This is my Snake Game!')


# Define some colors
blue = (0, 0, 255)
red =  (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 102)
green = (50, 153, 213)
purple = (184, 151, 219)

# Updates the screen
pygame.display.update()

snake_block = 10
snake_speed = 15

# Helps track time time
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0,0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/6])

def gameLoop():
    
    game_over = False
    game_close = False
    
    x1 = dis_width / 2
    y1 = dis_height / 2
        
    x1_change = 0
    y1_change = 0  
    
    snake_List = []
    Length_of_snake = 1
    
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        
    while not game_over:
        
        while game_close == True:  
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake-1)
            pygame.display.update()  
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_q:
                         game_over = True
                         game_close = False  
                     if event.key == pygame.K_c:     
                         gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True   
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10            
            
        if x1 >= dis_width or x1 < 0 or y1 >=  dis_height or y1 < 0:
            game_close = True
                    
        x1 = x1 + x1_change
        y1 = y1 + y1_change 
        dis.fill(blue)
                
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])        
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])    
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        
        pygame.display.update()  
        
        if x1 == foodx and y1 == foody:
            print("Thanks - that was delicious")
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        
        clock.tick(snake_speed) 

    message("You lost", red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()

    # Used to uninitialize everything
    quit()
    
gameLoop()    