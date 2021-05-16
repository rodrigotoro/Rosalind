import argparse
import sys

sample_dataset = '''GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
'''

sample_output = 7

def hamming_distance(s, t):
    if len(s) != len(t):
        sys.exit('Aborting: strings are not the same length.')
    
    distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            distance += 1
    
    return distance


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    args = parser.parse_args()

    if args.input:
        with open(args.input, 'r') as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset
    
    s, t = [item.strip() for item in input_dataset.split('\n') if len(item) > 0]
    solution = hamming_distance(s, t)
    
    print(solution)