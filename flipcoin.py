import random

def flip_coin(num_flips):
    if not isinstance(num_flips, int) or num_flips <= 0:
        return "enter a positive integer: "

    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):
        if random.random() < 0.5:
            heads_count += 1
        else:
            tails_count += 1

    heads_percentage = (heads_count / num_flips) * 100
    tails_percentage = (tails_count / num_flips) * 100

    result = f"Heads: {heads_percentage:.2f}%\nTails: {tails_percentage:.2f}%"
    return result

num_flips = int(input("enter the flips: "))
output = flip_coin(num_flips)
print(output)