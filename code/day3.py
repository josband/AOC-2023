DELTAS = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

def sum_schematic() -> int:
    with open('./input/input3.txt', 'r') as f:
        lines = list()
        for line in f:
            lines.append(line.rstrip('\n'))
    
    indicies = set()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] != '.' and not lines[r][c].isnumeric():
                for dr, dc in DELTAS:
                    row, col = r + dr, c + dc
                    if 0 <= row < len(lines) and 0 <= col < len(lines[0]) and lines[row][col].isnumeric():
                        # Get number
                        rp = lp = col
                        while lp > 0 and lines[row][lp - 1].isnumeric():
                            lp -= 1

                        while rp < len(lines[0]) - 1 and lines[row][rp+1].isnumeric():
                            rp += 1

                        # Add to set
                        indicies.add((row, lp, rp))

    return sum([int(lines[row][lp:rp+1]) for row, lp, rp in indicies])

def sum_gear_ratios() -> int:
    with open('./input/input3.txt', 'r') as f:
        lines = list()
        for line in f:
            lines.append(line.rstrip('\n'))
    
    ratios = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] != '.' and not lines[r][c].isnumeric():
                indicies = set()
                for dr, dc in DELTAS:
                    row, col = r + dr, c + dc
                    if 0 <= row < len(lines) and 0 <= col < len(lines[0]) and lines[row][col].isnumeric():
                        # Get number
                        rp = lp = col
                        while lp > 0 and lines[row][lp - 1].isnumeric():
                            lp -= 1

                        while rp < len(lines[0]) - 1 and lines[row][rp+1].isnumeric():
                            rp += 1

                        # Add to set
                        indicies.add((row, lp, rp))
                if len(indicies) == 2:
                    # Calculate and add ratio
                    ratio = 1
                    for row, lp, rp in indicies:
                        ratio *= int(lines[row][lp:rp+1])
                    ratios += ratio

    return ratios

if __name__ == "__main__":
    print("First task answer:", sum_schematic())

    print("Second task answer:", sum_gear_ratios())