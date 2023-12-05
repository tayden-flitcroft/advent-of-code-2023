from collections import deque

def create_lists(line):
    card_id, cards = str(line).split(":")
    winners, my_numbers = cards.split("|")
    winners_arr = winners.strip().split()
    my_numbers_arr = my_numbers.strip().split()
    card_string, new_card_id = card_id.split()
    return winners_arr, my_numbers_arr, int(new_card_id)  # Convert card_id to integer

def count_matches(winners, my_nums):
    winners_set = set(winners)  # Convert to set for faster lookup
    return sum(num in winners_set for num in my_nums)

def main(card_data):
    total_scratchcards = len(card_data)  # Start with the number of original scratchcards
    card_queue = deque(range(1, len(card_data) + 1))  # Queue initialized with card indices

    while card_queue:
        card_index = card_queue.popleft()  # Get the current card index
        winners, my_nums = card_data[card_index]
        match_count = count_matches(winners, my_nums)

        # Add subsequent scratchcards based on the number of matches
        for i in range(1, match_count + 1):
            next_card_index = card_index + i
            if next_card_index <= len(card_data):  # Check boundary
                card_queue.append(next_card_index)  # Add the next card
                total_scratchcards += 1  # Increment the total count

    return total_scratchcards

with open('input.txt', 'r') as input_file:
    card_data = {}
    for line in input_file:
        winners, my_nums, card_id = create_lists(line)
        card_data[card_id] = (winners, my_nums)

total = main(card_data)
print(total)
