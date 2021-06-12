import argparse
from .utils.fasta import Fasta

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
    shortest_fasta_len = len(sorted_fastas[0])

    common_kmers = set()

    for i in range(shortest_fasta_len, 0, -1):
        if not common_kmers:
            kmers1 = sorted_fastas[0].get_kmers(length=i)
            for fasta in sorted_fastas[1:]:
                kmers2 = fasta.get_kmers(length=i)
                if not common_kmers:
                    common_kmers = kmers1 & kmers2
                else:
                    common_kmers = common_kmers & kmers2
                if not common_kmers:
                    break
        else:
            return common_kmers


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
