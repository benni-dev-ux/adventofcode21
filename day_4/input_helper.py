def read_input(filename):
    '''reading text file line by line'''
    with open(filename) as f:
        return [int(line) for line in f.read().splitlines()]

def read_bingo_input(filename):
    lines = [line.strip() for line in open(filename, 'r').readlines()]

    sequence = [int(value) for value in lines[0].split(",")]
    boards = []

    chunks = [lines[i:i + 5] for i in range(2, len(lines), 6)]
    for chunk in chunks:
        board = []
        for i, line in enumerate(chunk):
            board.append([])
            for j, value in enumerate([value for value in line.strip().split(" ") if not value == '']):
                board[i].append((int(value), False))  #every cell is false at initialization
        boards.append(board)
    return sequence, boards

