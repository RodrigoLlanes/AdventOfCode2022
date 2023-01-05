
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
    N = 2022
    for i in range(N):
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
                break
    print(max_y+1)


if __name__ == '__main__':
    main()

