from utils import *

myGrid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

#Harder Sudoku
grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'

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

    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def only_choice(values):

    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):

    stalled = False
    while not stalled:

        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):

            return False
    return values

def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False #
    if all(len(values[s]) == 1 for s in boxes):
        return values
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

# print(eliminate(grid_values(myGrid)))
# only_choice(eliminate(grid_values(myGrid)))
# display(eliminate(grid_values(myGrid)))
print('My Sudoku\n')
display(search(grid_values(myGrid)))
print('\n')
print('Harder Sudoku\n')
display(search(grid_values(grid2)))
