def sanitize_input_part_1(input_data) -> list:
    lines = input_data.split('\n')

    times = []
    distances = []

    for line in lines:
        values = line.split()
        if not values:
            continue

        label = values[0]
        numeric_values = [int(value) for value in values[1:]]

        if label == "Time:":
            times = numeric_values
        elif label == "Distance:":
            distances = numeric_values

    return times, distances

def part_1(times, distances) -> str:
    total_number_of_wins = 1 # multiplied

    for i in range(len(times)):
        time = int(times[i])
        distance = int(distances[i])

        total_ways_to_win = 0 # added

        travel_speed = 1

        while travel_speed != time:
                if (time - travel_speed) * travel_speed > distance:
                    total_ways_to_win += 1
                travel_speed += 1

        total_number_of_wins *= total_ways_to_win
    return total_number_of_wins

def part_2(time, distance) -> int:
    first, last = 0, 0
    for i in range(time):
        reverse = time - i

        if not first and (time - i) * i > distance:
            first = i

        if not last and (time - reverse) * reverse > distance:
            last = reverse
        
        if (first and last):
            break

    return last - first + 1


with open('input.txt', 'r') as input:
    read = input.read()
    times_1, distances_1 = sanitize_input_part_1(read)
    times_2, distances_2 = '', ''

    for i in times_1:
        times_2 += str(i)
        
    for i in distances_1:
        distances_2 += str(i)

    print(part_1(times_1, distances_1), part_2(int(times_2), int(distances_2)))