import argparse

sample_dataset = '5 3'
sample_output = 19

def fibonacci(n, k):
    sequence = [1, 1]
    i = len(sequence)
    while len(sequence) < n:
        next_gen = (sequence[i - 2] * k) + sequence[i - 1]
        sequence.append(next_gen)
        i += 1
    return sequence[n - 1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    args = parser.parse_args()

    if args.input:
        with open(args.input, 'r') as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    input_dataset = [int(item) for item in input_dataset.split()]

    solution = fibonacci(*input_dataset)
    
    print(solution)