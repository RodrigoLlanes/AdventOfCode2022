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
    for _ in range(10):
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

        for (nx, ny), (x, y) in targets.items():
            if x is None:
                continue
            grid[x, y] = '.'
            grid[nx, ny] = '#'
        
    max_x, min_x = max(x for (x, _), char in grid.items() if char == '#'), min(x for (x, _), char in grid.items() if char == '#')
    max_y, min_y = max(y for (_, y), char in grid.items() if char == '#'), min(y for (_, y), char in grid.items() if char == '#')
    s = 0
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if grid[x, y] == '.':
                s += 1
    print(s)


if __name__ == '__main__':
    main()

