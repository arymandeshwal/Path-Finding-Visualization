import pygame
import sys
from bfs import *
#from AstarAlgo import *
pygame.init()

algo_choice = 0
#print("Choose algorithm to use:")
#try:
    #algo_choice = int(input("[1] for BFS\n[2] for A* search(shortest distance)\n"))
#except:
    #print("Incorrect value enter again!!")
    #algo_choice = int(input("[1] for BFS\n[2] for A* search(shortest distance)\n"))

algo_choice = 1
#constant variables
##colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (0,255,255)
##size of window
size = width, height = 705,705
## size of each block and margin
block_w,block_h = 20,20
margin = 5

##displaying pygame screen
screen = pygame.display.set_mode(size)

##click counter
click_count = 0

##starting point and ending for search
start = (0,0)
end = (0,0)

grid = []
for i in range(28):
    l=[]
    for j in range(28):
        l.append(0)
    grid.append(l)

#fucntions

##algorithms
def algo():
    if algo_choice == 1:
        print("BSF chosen")
        path = bfs_algo(grid,start)
##    elif algo_choice == 2:
##        print("Astar chosen")
##        path = astar_algo(grid,start,end)
##    ##    print(path)
    try:
        for i in path:
            if i != path[0] and i!= path[-1]:
                grid[i[0]][i[1]] = 5
    except:
        print("No path can be found")
        pygame.quit()
        sys.exit()
    
        
        
        

##display grid
def display():
    for i in grid:
        print(i)

#main loop
while True:
    #Event detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space pressed")
                display()
                algo()
                
                print("start: {}\tend: {}".format(start,end))

        elif pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            column = pos[0]//(block_w + margin)
            row = pos[1] // (block_h + margin)
            click_count+=1
            if click_count == 1:
                grid[row][column] = 2
                start = (row,column)
            elif click_count == 2:
                grid[row][column] = 3
                end = (row,column)
            else:
                try:
                    if grid[row][column] != 2 and grid[row][column] != 3:
                        grid[row][column] = 1
                except:
                    print("out of bounds")
##            print("row:{}\tcol:{}\tclicks:{}".format(row,column,click_count))
            

    # background black
    screen.fill(BLACK)



    #grid coloring
    for row in range(28):
        for col in range(28):
            color = WHITE
            if grid[row][col] == 1:
                color = GREEN
            elif grid[row][col] == 2:
                color = RED
            elif grid[row][col] == 3:
                color = BLACK
            elif grid[row][col] == 5:
                color = CYAN
            pygame.draw.rect(screen,color,[(margin+block_w)*col + margin,(margin+block_h)*row+margin,block_w,block_h])
            

    pygame.display.flip()

pygame.quit()
