rules = {
        "red": 12,
        "green": 13,
        "blue": 14
}

def create_roll_map(rolls):
        roll_map = {}
        for roll in rolls.split(","):
            clean = roll.strip().split(' ')
            number_of_rolls = clean[0]
            color = clean[1]
            roll_map[color] = number_of_rolls
        return roll_map

def sanitize_data(data):
        game_id = int("".join(str for str in data.split(":")[0] if str.isdigit()))
        list_of_rolls = data.split(":")[1].split(";")
        sanitized_data = list(map(create_roll_map, list_of_rolls))
        return {"id": game_id, "rolls": sanitized_data}

def main(input):
        total = 0
        total_power = 0
        for line in input:
                sanitized_data = sanitize_data(line)
                is_possible = True
                lowest_possible = {
                       "red": 0,
                       "green": 0,
                       "blue": 0
                }
                for rolls in sanitized_data["rolls"]:
                       keys = rolls.keys()

                       for key in keys:
                                if int(rolls[key]) > int(rules[key]):
                                    is_possible = False
                                if lowest_possible[key] == 0 or lowest_possible[key] < int(rolls[key]):
                                       lowest_possible[key] = int(rolls[key])
                            

                power = 1

                for value in lowest_possible.values():
                       power = power * value 
                total_power += power

                if is_possible:
                       total += sanitized_data["id"]
        return {"total": total, "total_power": total_power}

with open('input.txt', 'r') as input:
        print(main(input))