# Ficheiros

import board, dog

from pybricks.tools import wait
import random
     
#Return 0 or 1 with 50% chance for each
def rand():
    return random.randrange(2)

# Valores de inicialização
starting_location = [0,0]
starting_facing = 1
board_dimension = (6,6)

b = board(board_dimension[0],board_dimension[1])
d = dog(starting_location,starting_facing)

while True:
    
    wait(2000)
    d.isOnMargin()
    if(not(d.move(b))):
        if ( d.spot() and not (d.front == [5,5]) ):
            if (rand() == 1):
                d.bark()
            else:
                d.touch()
        elif (rand() == 1):
            d.turn(1)
        else:
            d.turn(-1)
            
            