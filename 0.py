
def read_rotations(example: bool = False) -> list[tuple[str, int]]:
    rotations: list[tuple[str, int]] = []
    if example:
        fname = "./data/0-test.txt"
    else:
        fname = "./data/0-0.txt"

    with open(fname, "r") as infile:
        rotations_raw = infile.readlines()

    for rotation in rotations_raw:
        stripped = rotation.strip()
        direction = stripped[0]
        amount = int(stripped[1:])
        rotations.append((direction, amount))

    return rotations
    
def solve0() -> int:
    rotations = read_rotations()
    pos = 50
    count = 0
    for direction, amount in rotations:
        if direction == "L":
            pos -= amount
        elif direction == "R":
            pos += amount
        pos = pos % 100
        if pos == 0:
            count += 1
    return count

def solve1() -> int:
    rotations = read_rotations()
    pos = 50
    count = 0
    for direction, amount in rotations:
        new_pos = pos
        if direction == "L":
            new_pos -= amount
        elif direction == "R":
            new_pos += amount
        if new_pos <= 0 or new_pos >= 100:
            clicks_0 = 0
            # move to 0
            if pos == 0:
                # don't need to normalize to 0 
                pass
            elif new_pos <= 0:
                amount -= pos
                count += 1 
            else:
                amount -= 100 - pos
                count += 1

            count += abs(amount // 100)
        pos = new_pos % 100
    return count

print(solve0())
print(solve1())
