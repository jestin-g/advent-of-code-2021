depths = list()

with open("raw_data") as raw_data:
    for line in raw_data.readlines():
        depths.append(int(line))

count_greater_depths = 0
for i in range(len(depths) - 1):
    if depths[i] < depths[i+1]:
        count_greater_depths += 1

print("Answer part one:", count_greater_depths)

count_greater_depths_sliding_window = 0
for i in range(len(depths) - 1):
    current_window = sum(depths[i:i+3])
    next_window = sum(depths[i+1:i+4])
    if current_window < next_window:
        count_greater_depths_sliding_window += 1

print("Answer part two:", count_greater_depths_sliding_window)
