import argparse

from utils.fasta import Fasta
from utils.genetic_code import codons
from utils.nucleic_acids import Dna

sample_dataset = """>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
"""

sample_output = """MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""


def translate_orfs(rna_sequence):
    peptides = []

    for i in range(len(rna_sequence) - 2):
        start = rna_sequence[i: i + 3]
        if start == "AUG":
            peptide = ""
            for j in range(i, len(rna_sequence) - 2, 3):
                codon = rna_sequence[j: j + 3]
                if codons[codon] == "Stop":
                    peptides.append(peptide)
                    break
                else:
                    peptide += codons[codon]

    return peptides


def find_candidate_proteins(fasta_string):
    fasta = Fasta(fasta_string)
    dna = Dna(fasta.sequence)
    reverse_complement = dna.reverse_complement()

    candidate_proteins = []
    for sequence in [dna, reverse_complement]:
        rna = sequence.transcribe()
        candidate_proteins += translate_orfs(rna)

    return set(candidate_proteins)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    solution = find_candidate_proteins(input_dataset)

    for item in solution:
        print(item)
