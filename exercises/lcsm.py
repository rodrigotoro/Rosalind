import argparse
from utils.fasta import Fasta

sample_dataset = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""

sample_output = "AC"


def get_longest_common_substring(multi_fasta_string):
    fastas = [
        Fasta(">" + line) for line in multi_fasta_string.split(">") if len(line) > 0
    ]

    sorted_fastas = sorted(fastas, key=lambda x: len(x))

    common_kmers = set()

    for i, fasta in enumerate(sorted_fastas):
        max_kmer_length = None
        if len(common_kmers) > 0:
            max_kmer_length = len(max(common_kmers, key=len))

        kmers = fasta.get_kmers(max_length=max_kmer_length)
        if i == 0:
            common_kmers = kmers
        else:
            common_kmers = common_kmers & kmers

    return max(common_kmers, key=len)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    solution = get_longest_common_substring(input_dataset)

    print(solution)
