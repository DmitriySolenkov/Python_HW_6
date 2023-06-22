from random import randint


def get_cells_list(axis_x, axis_y):
    x = axis_x
    y = axis_y
    cells_list = set()
    for i in range(1, 9):
        cells_list.add((x, i))
        cells_list.add((i, y))
    while (x < 9 and y < 9):
        cells_list.add((x, y))
        x += 1
        y += 1
    x = axis_x
    y = axis_y
    while (x > 0 and y > 0):
        cells_list.add((x, y))
        x -= 1
        y -= 1
    x = axis_x
    y = axis_y
    while (x < 9 and y > 0):
        cells_list.add((x, y))
        x += 1
        y -= 1
    x = axis_x
    y = axis_y
    while (x > 0 and y < 9):
        cells_list.add((x, y))
        x -= 1
        y += 1
    cells_list.discard((axis_x, axis_y))
    return (cells_list)


def queens_generator():
    queens = set()
    for i in range(1, 9):
        queens.add((i, randint(1, 8)))
    return queens


counts = 0
tries = 0
while counts < 4:
    tries += 1
    queens = queens_generator()
    # queens=((1,3),(2,6),(3,4),(4,1),(5,8),(6,5),(7,7),(8,2))
    check = True
    for element in queens:
        cells_list = get_cells_list(element[0], element[1])
        for element_2 in queens:
            if element_2 in cells_list:
                check = False
                break
        if check == False:
            break

    if check == True:
        counts += 1
        print(queens)
print(f"Total tries= {tries}")
