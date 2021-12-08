def read_input(filename):
    '''reading text file line by line'''
    with open(filename) as f:
        line = f.read()
        return [int(x) for x in line.split(",")]
        return numbers
