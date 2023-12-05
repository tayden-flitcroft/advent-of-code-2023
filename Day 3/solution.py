import re

def is_symbol(input):
    return bool(re.compile("[^.0-9]").match(input))

def create_2d_array(lines):
    return [list(line.strip()) for line in lines]

def near_number(row, column, matrix):
    rows, cols = len(matrix), len(matrix[0])
    adjacent_indices = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx, ny = row + dx, column + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny].isdigit():
                adjacent_indices.append((nx, ny))
    return adjacent_indices

def build_entire_number(index, matrix, visited):
    x, y = index
    if (x, y) in visited:
        return 0

    num_str = ''
    while y >= 0 and matrix[x][y].isdigit():
        if (x, y) in visited:
            break
        num_str = matrix[x][y] + num_str
        visited.add((x, y))
        y -= 1

    y = index[1] + 1
    while y < len(matrix[x]) and matrix[x][y].isdigit():
        if (x, y) in visited:
            break
        num_str += matrix[x][y]
        visited.add((x, y))
        y += 1

    return int(num_str)

def calculate_total(input_lines):
    matrix = create_2d_array(input_lines)
    grand_total = 0
    gear_ratio = 0
    visited = set()

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if is_symbol(matrix[row][column]):
                is_gear = matrix[row][column] == '*'
                whole_numbers = set()
                for index in range(len(near_number(row, column, matrix))):
                    number_index = near_number(row, column, matrix)[index]
                    whole_number = build_entire_number(number_index, matrix, visited)
                    if whole_number:
                        whole_numbers.add(whole_number)
                        grand_total += whole_number

                        if is_gear and len(whole_numbers) == 2:
                            gear_ratio += list(whole_numbers)[0] * list(whole_numbers)[1]


    return grand_total, gear_ratio


with open('input.txt', 'r') as input:
        print(calculate_total(input))