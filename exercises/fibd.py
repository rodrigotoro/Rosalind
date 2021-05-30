import argparse

sample_dataset = "6 3"
sample_output = 4


def mortal_fibonacci(n, m):
    adults = [0]
    babies = [1]
    for i in range(1, n):
        babies.append(adults[i - 1])
        adults.append(adults[i - 1] + babies[i - 1])
        if i - m >= 0:
            adults[i] -= babies[i - m]

    mortal_fib = [x + y for x, y in zip(adults, babies)]
    return mortal_fib[-1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    input_dataset = [int(item) for item in input_dataset.split()]

    solution = mortal_fibonacci(*input_dataset)

    print(solution)
