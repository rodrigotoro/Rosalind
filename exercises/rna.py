import argparse

sample_dataset = 'GATGGAACTTGACTACGTAAATT'
sample_output = 'GAUGGAACUUGACUACGUAAAUU'

def transcribe(dna_string):
    print(dna_string.replace('T', 'U'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    args = parser.parse_args()

    if args.input:
        with open(args.input, 'r') as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    transcribe(input_dataset)