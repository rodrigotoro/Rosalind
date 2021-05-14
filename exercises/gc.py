import argparse

sample_dataset = '''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
'''

sample_output = '''Rosalind_0808
60.919540
'''

def split_multiline_fasta(multiline_fasta):
    split_multiline = [line for line in multiline_fasta.split('>') if len(line) > 0]
    fasta_list = {}
    for raw_fasta in split_multiline:
        split_raw_fasta = raw_fasta.split('\n')
        fasta_id = split_raw_fasta[0]
        fasta_sequence = ''.join(split_raw_fasta[1:])
        fasta_list[fasta_id] = fasta_sequence.upper()
    return fasta_list


def largest_gc(multiline_fasta):
    fasta_list = split_multiline_fasta(multiline_fasta)
    highest_gc = (None, 0)
    for fasta_id, sequence in fasta_list.items():
        g = sequence.count('G')
        c = sequence.count('C')
        gc_content = (g + c) / len(sequence)
        if gc_content > highest_gc[1]:
            highest_gc = (fasta_id, gc_content)
    
    return f'{highest_gc[0]}\n{highest_gc[1]*100:.6f}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    args = parser.parse_args()

    if args.input:
        with open(args.input, 'r') as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    solution = largest_gc(input_dataset)
    
    print(solution)