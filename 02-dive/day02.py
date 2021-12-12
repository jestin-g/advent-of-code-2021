commands = []

with open("raw_data") as raw_data:
    for line in raw_data.readlines():
        line_partitioned = line.partition(" ")
        commands.append([
            line_partitioned.__getitem__(0),
            int(line_partitioned.__getitem__(2)[:-1])
        ])

commands_consolidated = dict()

for command in commands:
    if command[0] in commands_consolidated:
        commands_consolidated[command[0]] += command[1]
    else:
        commands_consolidated[command[0]] = command[1]

final_horizontal_position = commands_consolidated["forward"]

final_depth = commands_consolidated["down"] - commands_consolidated["up"]

print("Answer part one:", final_horizontal_position * final_depth)

horizontal_position = 0
depth = 0
aim = 0
for command in commands:
    if command[0] == "down":
        aim += command[1]
    elif command[0] == "up":
        aim -= command[1]
    elif command[0] == "forward":
        horizontal_position += command[1]
        depth += aim * command[1]

print("Answer part one:", horizontal_position * depth)
