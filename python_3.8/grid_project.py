grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print(grid[0][0])

for counter_one in range(len(grid[0])):
    for counter_two in range(len(grid)):
        print(grid[counter_two][counter_one], end='')
    print()

for counter_one in range(len(grid[1])):
    for counter_two in range(len(grid[0])):
        print(grid[counter_one][counter_two], end='')
    print()
