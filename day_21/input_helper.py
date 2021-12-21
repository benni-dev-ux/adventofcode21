def read_input(filename):
    '''reading text file line by line'''
    with open(filename) as f:
        return [str(line) for line in f.read().splitlines()]


def read_input_single_line(filename):
    '''reading text file line by line'''
    with open(filename) as f:
        line = f.read()
        return [int(x) for x in line.split(",")]
        return numbers
