class NucleicAcid:
    def __init__(self, nucleotide_string):
        self.sequence = nucleotide_string.upper()

    def __repr__(self):
        return self.sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, key):
        return self.sequence[key]

    def gc_content(self):
        g = self.sequence.count("G")
        c = self.sequence.count("C")
        return (g + c) / len(self.sequence)


class Dna(NucleicAcid):
    def __init__(self, nucleotide_string):
        super().__init__(nucleotide_string)
        allowed_nucleotides = ["A", "T", "C", "G"]
        for nucleotide in self.sequence:
            if nucleotide not in allowed_nucleotides:
                raise ValueError(f"Nucleotide {nucleotide} is not present in DNA")

    def transcribe(self):
        return self.sequence.replace("T", "U")

    def reverse_complement(self):
        reverse = self.sequence[::-1]
        complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
        reverse_complement = "".join([complements[base] for base in reverse])
        return Dna(reverse_complement)
