# Fill in the grid with a pattern of black and white squares, so that the numbers in each row and column match the lengths of consecutive runs of black squares. 

from gettext import find
from operator import index

import numpy as np


grid = np.array([#['0','0','0','0','0','0','0','0'],
                 ['1','1','1','1','1','1','1','1'],
                 ['0','0','0','0','0','0','1','0'],
                 ['0','0','0','0','0','1','0','0'],
                 ['0','0','0','0','1','0','0','0'],
                 ['0','0','0','1','0','0','0','0'],
                 ['0','0','1','0','0','0','0','0']])


def scan_for_ones(grid):
    #print (grid)
    row_headings = []
    for row in grid:
        row = ''.join(row)
        
        try:
            items = row.split('1')            
            row_headings.append([len(substr) for substr in items if len(substr) != 0])
            continue
        except:
            row_headings.append([len(row)])
            continue
        
    return row_headings


if __name__ == '__main__':
    row_headings = scan_for_ones(grid)
    #print (np.flip(grid.T, 1))
    col_headings = scan_for_ones(grid.T)
    print (row_headings)
    print (col_headings)