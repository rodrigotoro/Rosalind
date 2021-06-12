import argparse
from .utils.genetic_code import aminoacids


sample_dataset = "MA"

sample_output = 12


def mrna_possibilities(protein_string):
    possibilities = 1

    for aminoacid in protein_string:
        num_codons = len(aminoacids[aminoacid])
        possibilities = (possibilities * num_codons) % 1000000

    num_stop_codons = len(aminoacids["Stop"])
    possibilities = (possibilities * num_stop_codons) % 1000000

    return possibilities


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    solution = mrna_possibilities(input_dataset.strip())

    print(solution)
