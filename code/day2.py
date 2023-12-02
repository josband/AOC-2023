import re

RED, GREEN, BLUE= 12, 13, 14

def count_possible() -> int:
    possible_sum = 0
    with open('./input/input2.txt', 'r') as file:
        for line in file:
            sets = re.split('Game [0-9]+:', line)[1][:-1].split(';')
            game = int(line.split(':')[0][5:])
            valid = True
            for item in sets:
                colors = item[1:].split(', ')
                for color in colors:
                    split_color = color.split(' ')
                    match split_color[1]:
                        case 'red':
                            if int(split_color[0]) > RED:
                                valid = False
                                break
                        case 'green':
                            if int(split_color[0]) > GREEN:
                                valid = False
                                break
                        case 'blue':
                            if int(split_color[0]) > BLUE:
                                valid = False
                                break
                        case _:
                            continue
                if not valid:
                    break
            if valid:
                possible_sum += game
    
    return possible_sum

def count_game_powers() -> int:
    powers_sum = 0
    with open('./input/input2.txt', 'r') as file:
        for line in file:
            sets = re.split('Game [0-9]+:', line)[1][:-1].split(';')
            max_R, max_G, max_B = 0, 0, 0
            for item in sets:
                colors = item[1:].split(', ')
                for color in colors:
                    split_color = color.split(' ')
                    match split_color[1]:
                        case 'red':
                            max_R = max(max_R, int(split_color[0]))
                        case 'green':
                            max_G = max(max_G, int(split_color[0]))
                        case 'blue':
                            max_B = max(max_B, int(split_color[0]))
                        case _:
                            continue
            powers_sum += max_R * max_G * max_B
    
    return powers_sum

if __name__ == '__main__':
    print("First task answer:", count_possible())
    print("Second task answer:", count_game_powers())