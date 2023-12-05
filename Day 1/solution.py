wordToNum = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0
}
       
def convert_to_nums (line):
        new_line = line
        for word in list(wordToNum):
                substring_indexes = [index for index in range(len(line)) if line.startswith(word, index)]
                for index in substring_indexes:
                        new_line = new_line[:index + 1] + str(wordToNum[word]) + new_line[index + 2:]
        
        new_line = ''.join(str for str in new_line if str.isdigit())
        return new_line


def main (input):
        total = 0
        for line in input:
                converted_string = convert_to_nums(line)
                converted_digits = converted_string[0] + converted_string[-1]
                total += int(converted_digits)
        return total

with open('input.txt', 'r') as input:
        print(main(input))