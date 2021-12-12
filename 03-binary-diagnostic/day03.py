binaries = []
with open("raw_data") as raw_data:
    for line in raw_data.readlines():
        binaries.append(line[:-1])

longest_binary = len(max(binaries, key=len))


def list_of_zeros(size=longest_binary):
    return [0] * longest_binary


count_0 = list_of_zeros(longest_binary)
count_1 = list_of_zeros(longest_binary)

for i in range(len(binaries)):
    for j in range(len(binaries[i])):
        if binaries[i][j] == "1":
            count_1[j] += 1
        else:
            count_0[j] += 1

gamma_binary = list_of_zeros(longest_binary)
epsilon_binary = list_of_zeros(longest_binary)

for i in range(len(count_1)):
    if count_1[i] > count_0[i]:
        gamma_binary[i] = 1

for i in range(len(epsilon_binary)):
    if gamma_binary[i] == 0:
        epsilon_binary[i] = 1

gamma_decimal = list_of_zeros(longest_binary)
epsilon_decimal = list_of_zeros(longest_binary)

for i, j in zip(reversed(range(len(gamma_binary))), range(len(gamma_binary))):
    gamma_decimal[i] = gamma_binary[i] * 2 ** j
    epsilon_decimal[i] = epsilon_binary[i] * 2 ** j

gamma_decimal_value = sum(gamma_decimal)
epsilon_decimal_value = sum(epsilon_decimal)

print("Answer part one:", gamma_decimal_value * epsilon_decimal_value)
