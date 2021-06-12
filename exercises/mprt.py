import argparse
import requests
from utils.fasta import Fasta
import re
import collections

sample_dataset = """A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
"""

sample_output = """B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""


def get_uniprot_fasta(uniprot_id):
    uniprot_url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(uniprot_url)
    if response.status_code == 200:
        fasta = Fasta(response.text)
        return fasta
    else:
        raise Exception(
            f"Status code {response.status_code} for the following URL request: {uniprot_url} "
        )


def find_n_glycosylation_motif(uniprot_ids: list):
    n_glycosylation = collections.defaultdict(list)
    n_glyc_pattern = "N[^P][ST][^P]"
    motif_length = 4

    for uniprot_id in uniprot_ids:
        fasta = get_uniprot_fasta(uniprot_id)
        for i in range(len(fasta) + 1 - motif_length):
            match = re.match(n_glyc_pattern, fasta.sequence[i:])
            if match:
                n_glycosylation[uniprot_id].append(i + 1)

    return n_glycosylation


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    uniprot_ids = [
        uniprot_id.strip()
        for uniprot_id in input_dataset.split()
        if len(uniprot_id) > 0
    ]
    solution = find_n_glycosylation_motif(uniprot_ids)

    for key, values in solution.items():
        print(key)
        print(*values)
