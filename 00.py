rotations: list[tuple[str, int]] = []

with open("./data/00.txt", "r") as infile:
    rotations_raw = infile.readlines()

for rotation in rotations_raw:
    stripped = rotation.strip()
    direction = stripped[0]
    amount = int(stripped[1:])
    rotations.append((direction, amount))
    
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

print(count)
