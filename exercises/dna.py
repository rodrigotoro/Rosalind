import argparse

sample_dataset = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
sample_output = '20 12 17 21'

def count_nucleotides(dna_string):
    nucleotides = ['A', 'C', 'G', 'T']
    counts = [str(dna_string.count(nucleotide)) for nucleotide in nucleotides]
    print(' '.join(counts))
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    args = parser.parse_args()

    if args.input:
        with open(args.input, 'r') as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    count_nucleotides(input_dataset)