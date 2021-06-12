import sys


class Fasta:
    def __init__(self, fasta_string):
        if not fasta_string.startswith(">"):
            raise ValueError('Provided FASTA string does not start with ">"')

        split = fasta_string.split("\n")
        self.identifier = split[0]
        self.sequence = "".join(split[1:]).upper()
        if len(self.sequence) == 0:
            raise ValueError("FASTA sequence must be at least 1 character long")

    def __repr__(self):
        return self.identifier

    def __len__(self):
        return len(self.sequence)

    def __iter__(self):
        return iter(self.sequence)

    def __getitem__(self, key):
        return self.sequence[key]

    def get_kmers(self, length=None, min_length=2, max_length=None):
        kmers = set()
        len_seq = len(self)
        if length is None:
            if max_length is None or max_length > len_seq:
                max_length = len_seq
            for kmer_length in range(min_length, max_length + 1):
                for pos in range(len_seq + 1 - kmer_length):
                    kmer = self.sequence[pos : pos + kmer_length]
                    kmers.add(kmer)
        else:
            if max_length:
                raise ValueError(
                    'Arguments "length" and "max_length" are mutually exclusive'
                )
            if length > len_seq:
                raise ValueError(
                    f"Requested length is longer than length of sequence (length {len(self)})"
                )
            for pos in range(len_seq + 1 - length):
                kmers.add(self.sequence[pos : pos + length])

        return kmers


if __name__ == "__main__":
    fasta_string = ">Test1\nACTGA"
    f = Fasta(fasta_string)
    a = f.get_kmers(length=6)
    print(a)
