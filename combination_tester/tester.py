from itertools import combinations

pinout = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'GND']

num_pins_to_test = 2

combo_list = list(combinations(pinout, num_pins_to_test))

print(f"Number of combinations to test: {len(combo_list)}")

for combo in combo_list:
    print(combo)