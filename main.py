#A standard Sudoku contains:
 #81 cells 
 #in a 9×9 grid
 #and has 9 boxes
 #each box being the intersection of the first, middle, or last 3 rows, and the first, middle, or last 3 columns. 
 #Each cell may contain a number from one to nine, and each number can only occur once in each row, column, and box. 
 #A Sudoku starts with some cells containing numbers (clues), and the goal is to solve the remaining cells. 

import numpy as np
grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
grid_array=np.matrix(grid)
for i in range(0,8):
  for j in range(0,8):
    print(grid_array[i,j])

#Minimum number of numbers that aren't 0 in this grid is 17. Anything less and we can't solve the puzzle.

for list in grid:
   if 9 in list:
     print(1)
     
