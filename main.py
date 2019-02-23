from utils import *

myGrid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

def grid_values(grid):

    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)

    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(boxes,values))

def eliminate(values):

    for box in values.keys():
        if len(values[box])==1:
            for peer_box in peers[box]:
                values[peer_box] = values[peer_box].replace(values[box],'')
    return(values)

print(eliminate(grid_values(myGrid)))
display(eliminate(grid_values(myGrid)))
