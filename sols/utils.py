def read_file(input_file):
    input = []
    with open(input_file) as f:
        for l in f:
            input.append(l.strip())
    return input
