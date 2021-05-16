import argparse

sample_dataset = "AAAACCCGGT"
sample_output = "ACCGGGTTTT"


def reverse_complement(dna_string):
    dna_string = dna_string.strip()
    reverse = dna_string[::-1]
    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
    reverse_complement = "".join([complements[base] for base in reverse])
    return reverse_complement


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    solution = reverse_complement(input_dataset)

    print(solution)
