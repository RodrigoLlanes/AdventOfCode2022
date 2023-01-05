from collections import defaultdict
import enum
from heapq import heapify, heappush, heappop

def load_input():
    grid = defaultdict(set)
    bad = set()
    lines = open('input', 'r').readlines()
    size = len(lines), len(lines[-1])-1
    for row, line in enumerate(lines):
        for col, char in enumerate(line.strip()):
            if char != '.':
                bad.add((row, col))
                grid[row, col].add(char)
    grid[-1, 1].add('#')
    bad.add((-1, 1))
    grid[size[0], size[1]-2].add('#')
    bad.add((size[0], size[1]-2))
    return grid, size, bad


def get_blizzard(blizzard, row, col, size):
    if blizzard == 'v':
        if row == size[0] - 2:
            row = 0
        return [row+1, col]
    if blizzard == '>':
        if col == size[1] - 2:
            col = 0
        return [row, col+1]
    if blizzard == '^':
        if row == 1:
            row = size[0]-1
        return [row-1, col]
    if blizzard == '<':
        if col == 1:
            col = size[1]-1
        return [row, col-1]


def update_grid(grid, size):
    res = defaultdict(set)
    bad = set()
    for (row, col), blizzards in grid.items():
        for blizzard in blizzards:
            if blizzard == '#':
                res[row, col].add('#')
                bad.add((row, col))
            else:
                nr, nc = get_blizzard(blizzard, row, col, size)
                res[nr, nc].add(blizzard)
                bad.add((nr, nc))
    return res, bad


def get_moves(grid, row, col, size):
    moves = []
    if (row, col) not in grid:
        moves.append((row, col))
    if (row-1, col) not in grid:
        moves.append((row-1, col))
    if (row+1, col) not in grid:
        moves.append((row+1, col))
    if (row, col-1) not in grid:
        moves.append((row, col-1))
    if (row, col+1) not in grid:
        moves.append((row, col+1))
    return moves

def print_grid(grid, size, pr, pc):
    for row in range(size[0]):
        for col in range(size[1]):
            if row == pr and col == pc:
                if len(grid[row, col]) == 0:
                    print('E', end='')
                else:
                    print('X', end='')
            elif len(grid[row, col]) == 0:
                print('.', end='')
            elif len(grid[row, col]) == 1:
                print(list(grid[row, col])[0], end='')
            else:
                print(str(len(grid[row, col])), end='')
        print()

def main() -> None:
    grid, size, bad = load_input()
    start = 0, 1
    end = size[0] - 1, size[1] - 2
    
    mem = defaultdict(lambda: 10e10)
    
    grids, bads = {}, {}
    queue = []
    score = 10e10
    grids[0] = grid
    bads[0] = bad
    queue.append((*start, 0, False, False))
    while len(queue):
        row, col, time, reach_start, reach_end = queue.pop(0)
        grid = bads[time]
        if (row, col) in grid:
            continue
        if time >= mem[(row, col, time, reach_start, reach_end)]:
            continue
        mem[(row, col, time, reach_start, reach_end)] = time

        if (row, col) == end:
            if reach_end:
                score = time
                print(score)
                break
            else:
                reach_start = True
        if (row, col) == start and reach_start:
            reach_end = True

        time = time+1
        if time in grids:
            grid = bads[time]
        else:
            grid, bad = update_grid(grids[time-1], size)
            grids[time] = grid
            bads[time] = bad
            grid = bad
        for move in get_moves(bad, row, col, size):
            queue.append((*move, time, reach_start, reach_end))


if __name__ == '__main__':
    main()

