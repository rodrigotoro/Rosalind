import argparse

sample_dataset = "2 2 2"

sample_output = 0.78333


def calculate_mating_probabilities(k, m, n):
    organisms = {"k": k, "m": m, "n": n}
    total_organisms = k + m + n
    mating_probabilities = {}
    for organism_one in organisms.keys():
        first_choice_probability = organisms[organism_one] / total_organisms
        for organism_two in organisms.keys():
            if organism_one == organism_two:
                second_choice_probability = (organisms[organism_two] - 1) / (
                    total_organisms - 1
                )
            else:
                second_choice_probability = organisms[organism_two] / (
                    total_organisms - 1
                )
            mating_probabilities[f"{organism_one}{organism_two}"] = (
                first_choice_probability * second_choice_probability
            )
    return mating_probabilities


def probability_dominant_allele(k, m, n):
    mating_probabilities = calculate_mating_probabilities(k, m, n)

    carries_dominant_allele_probabilities = {
        "kk": 1,
        "km": 1,
        "kn": 1,
        "mk": 1,
        "mm": 0.75,
        "mn": 0.5,
        "nk": 1,
        "nm": 0.5,
        "nn": 0,
    }

    overall_probability_of_dominant_allele = 0
    for mate_pair in mating_probabilities.keys():
        overall_probability_of_dominant_allele += (
            mating_probabilities[mate_pair]
            * carries_dominant_allele_probabilities[mate_pair]
        )

    return f"{overall_probability_of_dominant_allele:.5f}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    k, m, n = [int(item) for item in input_dataset.split() if len(item) > 0]
    solution = probability_dominant_allele(k, m, n)

    print(solution)
