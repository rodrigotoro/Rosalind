import argparse
import collections
from utils.fasta import Fasta

sample_dataset = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""

sample_output = """ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""

NUCLEOTIDES = ["A", "C", "G", "T"]


def consensus(multiline_fasta_string):
    # Parse multiline fasta string into Fasta objects
    fastas = [
        Fasta(">" + line) for line in multiline_fasta_string.split(">") if len(line) > 0
    ]

    # Compute profile matrix and consensus sequence
    profile_matrix = collections.defaultdict(list)
    consensus = ""

    for locus in zip(*fastas):
        locus_counter = collections.Counter(locus)
        locus_nucleotide_count = locus_counter.most_common()

        consensus += locus_nucleotide_count[0][0]

        for nucleotide in NUCLEOTIDES:
            profile_matrix[nucleotide].append(locus_counter.get(nucleotide, 0))

    # Construct string with solution
    to_print = consensus
    for nucleotide, profile in profile_matrix.items():
        to_print += "\n"
        to_print += f"{nucleotide}: "
        to_print += " ".join(map(str, profile))

    return to_print


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    solution = consensus(input_dataset)

    print(solution)
