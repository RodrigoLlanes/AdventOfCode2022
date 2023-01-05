from collections import defaultdict


def load_input():
    grid = defaultdict(lambda: '.')
    for y, line in enumerate(open('input', 'r').readlines()):
        for x, char in enumerate(line.strip()):
            if char == '#':
                grid[x, y] = '#'
    return grid


def main() -> None:
    grid = load_input()
    checks = [((-1, -1), (0, -1), ( 1, -1)),
              ((-1,  1), (0,  1), ( 1,  1)),
              ((-1, -1), (-1, 0), (-1,  1)),
              (( 1, -1), ( 1, 0), ( 1,  1))]
    i = 0
    while True:
        i += 1
        targets = {}
        aux = grid.copy()
        for (x, y), char in aux.items():
            if char != '#':
                continue
            if all(grid[x+dx, y+dy] == '.' for check in checks for dx, dy in check):
                continue
            for check in checks:
                if all(grid[x+dx, y+dy] == '.' for dx, dy in check):
                    dx, dy = check[1]
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in targets.keys():
                        targets[nx, ny] = (None, None)
                    else:
                        targets[nx, ny] = (x, y)
                    break

        if len(targets) == 0 or all(x is None for (x, y) in targets.keys()):
            print(i)
            break
        for (nx, ny), (x, y) in targets.items():
            if x is None:
                continue
            grid[x, y] = '.'
            grid[nx, ny] = '#'
        
        checks = checks[1:] + checks[:1]

if __name__ == '__main__':
    main()

