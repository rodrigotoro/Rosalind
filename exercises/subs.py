import argparse

sample_dataset = """GATATATGCATATACTT
ATAT
"""

sample_output = "2 4 10"


def locate_substring(string, substring):
    locations = []
    subs_len = len(substring)

    for i in range(0, len(string) - subs_len):
        if string[i : i + subs_len] == substring:
            locations.append(i + 1)

    return " ".join(map(str, locations))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            input_dataset = f.read()
    else:
        input_dataset = sample_dataset

    string, substring = [
        item.strip() for item in input_dataset.split("\n") if len(item) > 0
    ]
    solution = locate_substring(string, substring)

    print(solution)
