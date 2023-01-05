
def load_input() -> str:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        inp.append(line)
    return inp[0]


def check(grid, figure):
    for x, y in figure:
        if (x, y) in grid:
            return False
        if 0 > x or 6 < x:
            return False
        if 0 > y:
            return False
    return True


def main() -> None:
    line = [[x, 0] for x in range(4)]
    cross = [[0, 1], [1, 1], [2, 1], [1, 0], [1, 2]]
    corner = [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]]
    vline = [[0, y] for y in range(4)]
    square = [[0, 0], [0, 1], [1, 0], [1, 1]]
    
    figures = [line, cross, corner, vline, square]

    pushes = load_input()
    max_y = -1
    grid = set()
    j = 0
    rows = []
    N = 1000000000000
    _i = 0
    add = 0
    while _i < N:
        i = _i
        _i += 1
        figg = figures[i % len(figures)]
        figg = [[x + 2, y + max_y + 4] for x, y in figg]
        while True:
            push = pushes[j]
            j += 1
            j %= len(pushes)
            if push == '>':
                _figg = [[x + 1, y] for x, y in figg]
            else:
                _figg = [[x - 1, y] for x, y in figg]
            if check(grid, _figg):
                figg = _figg
            _figg = [[x, y - 1] for x, y in figg]
            if check(grid, _figg):
                figg = _figg
            else:
                for x, y in figg:
                    max_y = max(max_y, y)
                    grid.add((x, y))
                
                if add == 0 and check_row(grid, figg):
                    rows.append((i % len(figures), i, max_y))
                    if len(rows) > 10 and check_pattern(rows):
                        di, dh = check_pattern(rows)
                        inc = (N - i) // di
                        _i += inc * di
                        add = inc * dh
                break
    print(max_y+1+add)


def check_row(grid, figg):
    for _, y in figg:
        if all((x, y) in grid for x in range(7)):
            return y
    return False


def check_pattern(rows):
    indexes = [i for i, _, _ in rows]
    for i in range(len(rows)//3):
        if indexes[-i:] == indexes[-2*i:-i] and indexes[-2*i:-i] == indexes[-3*i:-2*i]:
            return rows[-i][1] - rows[-2*i][1], rows[-i][2] - rows[-2*i][2]
    return False


if __name__ == '__main__':
    main()

