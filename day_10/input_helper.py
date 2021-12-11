def read_input(filename):
    '''reading text file line by line'''
    with open(filename) as f:
        result=[]
        for line in f.read().splitlines():
         result.append([str(a) for a in str(line)])
        return result


def read_input_single_line(filename):
    '''reading text file line by line'''
    with open(filename) as f:
        line = f.read()
        return [int(x) for x in line.split(",")]
        return numbers
