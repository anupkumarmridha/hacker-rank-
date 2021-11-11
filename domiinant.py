#!/bin/python3

"""There is a given list of lists of integers that represent a 2- dimensional grid 
with n rows and m columns. A cell is called a dominant cell if it has a strictly greater 
value than all of its neighbors. Two cells are neighbors when they share a common side or 
a common corner, so a cell can have up to 8 neighbors. 
Find the number of dominant cells in the grid."""

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here
    res=0
    for i in range(len(grid)):
        for k in range(len(grid[0])):
            val=grid[i][k]
            flag=1
            for j in range(max(0,i-1),min(len(grid),i+2)):
                for l in range(max(0,k-1),min(len(grid[0]),k+2)):
                    if(j,l)!=(i,k) and val<=grid[j][l]:
                        flag=0
                        break
                if flag==0:
                    break
            else:
                    res+=1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
