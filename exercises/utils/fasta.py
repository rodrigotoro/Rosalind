import sys


class Fasta:
    def __init__(self, fasta_string):
        if not fasta_string.startswith(">"):
            raise ValueError('Provided FASTA string does not start with ">"')

        split = fasta_string.split("\n")
        self.identifier = split[0].lstrip(">")
        self.sequence = "".join(split[1:]).upper()
        if len(self.sequence) == 0:
            raise ValueError("FASTA sequence must be at least 1 bp long")

    def __repr__(self):
        return self.sequence

    def __len__(self):
        return len(self.sequence)

    def __iter__(self):
        return iter(self.sequence)

    def __getitem__(self, key):
        return self.sequence[key]
