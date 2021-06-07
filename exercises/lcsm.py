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

TOTAL_CHECKS = 0


def get_shortest_fasta(fasta_list):
    sorted_fasta_list = sorted(fasta_list, key=lambda x: len(x))
    return sorted_fasta_list[0]


def get_all_possible_kmers(fasta, kmer_length):
    number_of_possible_kmers = len(fasta) + 1 - kmer_length
    kmers = []
    for i in range(number_of_possible_kmers):
        kmers.append(fasta[i : i + kmer_length])
    return kmers


def get_longest_common_substring(multi_fasta_string):
    fastas = [
        Fasta(">" + line) for line in multi_fasta_string.split(">") if len(line) > 0
    ]

    shortest_fasta = get_shortest_fasta(fastas)

    for kmer_length in range(len(shortest_fasta), 0, -1):
        kmers = get_all_possible_kmers(shortest_fasta, kmer_length)
        for kmer in kmers:
            kmer_is_common = []
            for fasta in fastas:
                if fasta is not shortest_fasta:
                    if kmer in fasta.sequence:
                        kmer_is_common.append(True)
                    else:
                        kmer_is_common.append(False)
                    global TOTAL_CHECKS
                    TOTAL_CHECKS += 1
            if all(kmer_is_common):
                return kmer

    return None


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
    print(TOTAL_CHECKS)
