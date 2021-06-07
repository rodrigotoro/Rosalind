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

    def get_kmers(self, length=None, min_length=2, max_length=None):
        kmers = set()
        if length is None:
            for kmer_length in range(min_length, len(self)):
                if max_length:
                    if kmer_length == max_length + 1:
                        break
                for pos in range(len(self) + 1 - kmer_length):
                    kmers.add(self.sequence[pos : pos + kmer_length])
        else:
            for pos in range(len(self) + 1 - length):
                kmers.add(self.sequence[pos : pos + length])

        return kmers


if __name__ == "__main__":
    fasta_string = ">Test1\nACTGAACTGTAGCTGGTGGTAC"
    f = Fasta(fasta_string)
    a = f.get_kmers(min_length=10)
    print(a)
