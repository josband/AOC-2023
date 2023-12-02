WORDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_calibration_sum() -> int:
    res = 0
    with open('./input/input1.txt', 'r') as file:
        for line in file:
            value = ''
            for i in range(len(line)):
                if line[i].isnumeric():
                    value += line[i]
                    break

            for i in range(len(line) - 1, -1, -1):
                if line[i].isnumeric():
                    value += line[i]
                    break
            res += int(value)
    return res

def get_true_calibration_sum() -> int:
    res = 0
    with open('./input/input1.txt', 'r') as file:
        for line in file:
            value = ''
            start = len(line)
            for i, word in enumerate(WORDS):
                index = line.find(word)
                if index != -1 and index < start:
                    start = index
                    value = str(i + 1)
            
            for i in range(start):
                if line[i].isnumeric():
                    value = line[i]
                    break

            next_value = ''
            start = -1
            for i, word in enumerate(WORDS):
                index = line.rfind(word)
                if index != -1 and index > start:
                    start = index
                    next_value = str(i + 1)
            
            for i in range(len(line) - 1, start - 1, -1):
                if line[i].isnumeric():
                    next_value = line[i]
                    break
            res += int(value + next_value)

    return res

if __name__ == '__main__':
    sum = get_calibration_sum()
    print('Old sum is:', sum)

    sum = get_true_calibration_sum()
    print('True sum is:', sum)