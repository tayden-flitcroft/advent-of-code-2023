import re
from math import lcm

instructions_map = {
    'R': 1,
    'L': 0
}

start = 'AAA'
end = 'ZZZ'

def parse_data(input):
    lines = [x for x in input.strip().split('\n')]
    instructions = lines[0]

    steps_idx = 2
    steps_map = {}

    while steps_idx < len(lines):
        step = [x.strip() for x in lines[steps_idx].split('=')]
        key, connections = step
        regex = re.compile('[^a-zA-Z0-9 ]')
        connections_list = regex.sub('', connections).split(' ')
        steps_map[key] = connections_list
        steps_idx += 1

    return [x for x in instructions], steps_map

with open('input.txt') as input:
    instructions, connections = parse_data(input.read())

    # # # # # # # # 
    # part 1
    # steps = 0
    # key = start
    #
    # while key != end:
    #     instruction = instructions[0]
    #     key = connections[key][instructions_map[instruction]]
    #     instructions.append(instructions.pop(0))
    #     steps += 1
    #
    # print(steps)
    # # # # # # # # 

    connection_keys = list(filter(lambda x: x[-1] == 'A', connections))
    total_steps = []

    for key in connection_keys:
        steps = 0
        key_copy = key
        instructions_copy = instructions

        while not key_copy.endswith('Z'):
            steps += 1
            key_copy = connections[key_copy][instructions_map[instructions_copy[0]]]
            instructions_copy.append(instructions_copy.pop(0))
        
        total_steps.append(steps)
    
    print(lcm(*total_steps))
