def read_input(filename):
    '''reading text file line by line'''
    with open(filename) as f:
        return [str(line) for line in f.read().splitlines()]