import itertools
import math
import random



grid_width = 3
grid_height = math.floor(20 * (11/8.5))

items = '#%&@<$?!{}'

grid = [random.sample(items, grid_width, counts=[4 for _ in range(len(items))]) for _ in range(grid_height)]

'''
for line in grid:
    print (''.join(line))
   ''' 

# now put in code word
code_word = 'EIGHT'
margin = 2

# seems to not actually work?
assert len(code_word) < grid_width - 2*margin, 'word wont fit in this size of grid width'
assert len(code_word) < grid_height - 2*margin, 'word wont fit in this size of grid height'


# this ensures the same coordinate isn't repeated
coordinates = list( itertools.product(range(margin, grid_width-margin), range(margin, grid_height-margin)) )

replacement_coordinates = list(random.sample(coordinates, k=len(code_word)))
replacement_coordinates = sorted(replacement_coordinates, key=lambda x: x[0]+x[1]/grid_height)

for letter, (c, r) in zip(code_word, replacement_coordinates):
    grid[r][c] = letter

for line in grid:
    print (''.join(line))