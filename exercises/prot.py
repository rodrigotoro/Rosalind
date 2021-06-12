import argparse
from .utils.genetic_code import codons

sample_dataset = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

sample_output = "MAMAPRTEINSTRING"


def translate(mrna):
    polypeptide = ""
    remainder = len(mrna) % 3
    for i in range(0, len(mrna) - remainder, 3):
        codon = mrna[i : i + 3]
        aminoacid = codons[codon]
        if aminoacid != "Stop":
            polypeptide += aminoacid
    return polypeptide


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    solution = translate(input_dataset.strip())

    print(solution)
