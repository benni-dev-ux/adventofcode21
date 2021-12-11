import re


def read_input(filename):
    '''reading text file line by line'''
    with open(filename) as f:
        list = []
        for line in f.read().splitlines():
            list.append(re.findall(r'\b\d+\b', line))

        return list
