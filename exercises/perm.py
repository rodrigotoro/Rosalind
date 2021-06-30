import argparse
from itertools import permutations

sample_dataset = 3

sample_output = """6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""


def calculate_perms(n):
    integers = [i + 1 for i in range(n)]
    perms = permutations(integers)
    return list(perms)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    input_dataset = int(input_dataset)
    solution = calculate_perms(input_dataset)

    print(len(solution))
    for i in range(len(solution)):
        print(*solution[i])
