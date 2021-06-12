import argparse
from .utils.fasta import Fasta

sample_dataset = """>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
"""
sample_output = """Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""


def is_adjacent(fasta1, fasta2, overlap=3):
    if fasta1 is fasta2:
        return False

    fasta1_end = fasta1[-overlap:]
    if fasta2.sequence.startswith(fasta1_end):
        return True
    else:
        return False


def create_adjacency_list(multi_fasta_string):
    # Parse input fasta string into Fasta objects
    fastas = [
        Fasta(">" + fasta_string)
        for fasta_string in multi_fasta_string.split(">")
        if len(fasta_string) > 0
    ]

    # Build overlap graph
    adjacency_list = []

    for fasta in fastas:
        for secondary_fasta in fastas:
            if is_adjacent(fasta, secondary_fasta):
                adjacency_list.append((fasta.identifier, secondary_fasta.identifier))

    # Format string to print
    to_print = ""
    for edge in adjacency_list:
        to_print += " ".join(edge)
        to_print += "\n"

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

    solution = create_adjacency_list(input_dataset)

    print(solution)
