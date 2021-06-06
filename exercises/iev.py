import argparse

sample_dataset = "1 0 0 1 0 1"

sample_output = 3.5


def dominant_allele_offspring(population_ints_string):
    population_gt = [
        int(count) for count in population_ints_string.split(" ") if len(count) > 0
    ]

    offspring_probabilities = [
        1,  # AA-AA
        1,  # AA-Aa
        1,  # AA-aa
        0.75,  # Aa-Aa
        0.5,  # Aa-aa
        0,  # aa-aa
    ]

    expected_offspring = 0
    for i in range(6):
        expected_offspring += population_gt[i] * offspring_probabilities[i] * 2

    return expected_offspring


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    solution = dominant_allele_offspring(input_dataset)

    print(solution)
