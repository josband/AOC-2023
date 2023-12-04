import re

def task_1() -> int:
    total_points = 0
    f = open('./input/input4.txt').read().splitlines()
    for line in f:
        values = re.split('Card\s+[0-9]+:\s+', line)[1]
        left, right = re.split('\s+\|\s+', values)
        winning = set()
        for val in re.finditer("\d+", left):
            winning.add(int(val.group()))
        
        count = 0
        for val in re.finditer('\d+', right):
            if int(val.group()) in winning:
                count = 1 if count == 0 else count * 2
        
        
        total_points += count

    return total_points

def task_2() -> int:
    total_points = 0
    f = open('./input/input4.txt').read().splitlines()
    cards_won = [1] * len(f)
    for i, line in enumerate(f):
        values = re.split('Card\s+[0-9]+:\s+', line)[1]
        left, right = re.split('\s+\|\s+', values)
        winning = set()
        for val in re.finditer("\d+", left):
            winning.add(int(val.group()))
        
        count = 0
        for val in re.finditer('\d+', right):
            if int(val.group()) in winning:
                count += 1
        
        if count < len(f) - i:
            stop = i + count + 1
        else:
            stop = len(f)

        for j in range(i + 1, stop):
            cards_won[j] += cards_won[i]
        
        total_points += cards_won[i]

    return total_points

if __name__ == "__main__":
    print("Task 1 output:", task_1())
    print("Task 2 output:", task_2())