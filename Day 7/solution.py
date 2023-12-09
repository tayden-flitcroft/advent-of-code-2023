face_card_value = {
    'T': 10,
    # 'J': 11,
    # Part 2: J's are worth whatever makes the hand strongest
    'J': 1,
    'Q': 12,
    'K': 13,
    'A': 14
}

def score_hand(data = {}, override = None):
    if ('5OAK' in data and data["5OAK"]) or override == "5OAK":
        return 6
    elif ('4OAK' in data and data["4OAK"]) or override == "4OAK":
        return 5
    elif ('FH' in data and data["FH"]) or override == "FH":
        return 4
    elif ("3OAK" in data and data["3OAK"]) or override == "3OAK":
        return 3
    elif ("2_PAIR" in data and data["2_PAIR"]) or override == "2_PAIR":
        return 2
    elif ("PAIR" in data and data["PAIR"]) or override == "PAIR":
        return 1
    else:
        return 0

def create_map(hand):
    hand_map = {}
    tracker = {
        "5OAK": 0,
        "4OAK": 0,
        "FH": 0,
        "3OAK": 0,
        "2_PAIR": 0,
        "PAIR": 0,
        "HC": 0
    }

    j_counter = hand.count('J')

    current_state = None

    for i in range(len(hand)):
        current = hand[i]
        hand_map[current] = hand_map[current] + 1 if current in hand_map else 1
        

        if current != 'J':
            match hand_map[current]:
                case 5:
                    tracker["5OAK"] = tracker["5OAK"] + 1
                    tracker["4OAK"] = tracker["4OAK"] - 1
                    current_state = "5OAK"
                case 4:
                    tracker["4OAK"] = tracker["4OAK"] + 1
                    tracker["3OAK"] = tracker["3OAK"] - 1
                    current_state = "4OAK"
                case 3:
                    tracker['3OAK'] = tracker['3OAK'] + 1
                    tracker['PAIR'] = tracker['PAIR'] - 1
                    current_state = "3OAK"

                    if tracker['PAIR'] == 1 or tracker['2_PAIR'] >= 1:
                        tracker['FH'] = tracker['FH'] + 1
                        current_state = "FH"
                case 2:
                    tracker['PAIR'] = tracker['PAIR'] + 1
                    current_state = 'PAIR'

                    if tracker['PAIR'] == 2:
                        tracker["2_PAIR"] = tracker["2_PAIR"] + 1
                        tracker["PAIR"] = 0
                        current_state = '2_PAIR'

                    if tracker['3OAK'] >= 1:
                        tracker['FH'] = tracker['FH'] + 1
                        current_state = "FH"
                case _:
                    if single_card_value(current) > single_card_value(tracker['HC']):
                        tracker['HC'] = current
    if j_counter:
        order_of_power = ["HC", "PAIR", "3OAK", "4OAK", "5OAK"]
        power = score_hand({}, current_state)

        match current_state:
            case "2_PAIR":
                if j_counter == 1:
                    tracker["FH"] = tracker["FH"] + 1
                else:
                    tracker["4OAK"] = tracker["4OAK"] + 1
                tracker["2_PAIR"] = 0
            case "FH":
                tracker["5OAK"] = tracker["5OAK"] + 1
            case _:
                current_state = current_state if current_state else 'HC'

                if j_counter == 5:
                    tracker["5OAK"] = tracker["5OAK"] + 1
                else:
                    tracker[order_of_power[order_of_power.index(current_state) + j_counter]] = tracker[order_of_power[order_of_power.index(current_state) + j_counter]] + 1
                
                tracker[current_state] = 0
    return tracker

def parse_data(input):
    lines = input.split('\n')
    split = [x.split(' ') for x in lines]
    new_data = []
    for item in split:
        new_data.append([*item, create_map(item[0])])
    
    return new_data

def single_card_value(card):
    card = str(card)
    if card.isdigit():
        return int(card)
    else:
        return face_card_value[str(card)]

def calculate_total_winnings(data):
    total = 0

    for i in range(len(data)):
        total += int(data[i][1]) * (i + 1)
    
    return total

with open('input.txt', 'r') as input:
    data = parse_data(input.read())

    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):

            left_score = score_hand(data[j][2])
            right_score = score_hand(data[j + 1][2])

            if left_score == right_score:
                for idx in range(len(data[j][0])):
                    left_card_score = single_card_value(data[j][0][idx])
                    right_card_score = single_card_value(data[j + 1][0][idx])

                    if left_card_score == right_card_score:
                        continue

                    if left_card_score > right_card_score:
                        data[j], data[j + 1] = data[j + 1], data[j]
                    break
            elif left_score > right_score:
                data[j], data[j + 1] = data[j + 1], data[j]

    part_1 = calculate_total_winnings(data) # 248453531

    print(part_1)