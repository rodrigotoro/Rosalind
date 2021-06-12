import argparse
from math import factorial

sample_dataset = "2 1"

sample_output = "0.684"


def heterozygous_organisms_prob(k, n):
    prob_double_het = 0.25
    prob_other = 1 - prob_double_het
    num_organisms = 2 ** k

    prob = 0

    for i in range(n, num_organisms + 1):
        k_combinations = factorial(num_organisms) / (
            factorial(num_organisms - i) * factorial(i)
        )
        prob += (
            k_combinations
            * (prob_double_het ** i)
            * (prob_other ** (num_organisms - i))
        )

    return f"{prob:.3}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    k, n = [int(item) for item in input_dataset.split() if len(item) > 0]
    solution = heterozygous_organisms_prob(k, n)

    print(solution)
