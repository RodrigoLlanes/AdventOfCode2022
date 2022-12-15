

def sign(x):
    return x // abs(x)


def load_input():
    grid = set()
    max_y = 0
    for line in open('input', 'r').readlines():
        line = list(map(lambda x: list(map(int, x.split(','))), line.strip().split(' -> ')))
        px, py = line[0]
        grid.add((px, py))
        max_y = max(max_y, py)
        for x, y in line[1:]:
            if x - px != 0:
                for nx in range(x, px + sign(px - x), sign(px - x)):
                    grid.add((nx, y))
            else:
                for ny in range(y, py + sign(py - y), sign(py - y)):
                    grid.add((x, ny))
            px, py = x, y
            max_y = max(max_y, py)

    return grid, max_y


def main() -> None:
    grid, max_y = load_input()    
    
    src = (500, 0)
    count = 0
    while True:
        x, y = src
        while y < max_y:
            if (x, y+1) not in grid:
                y += 1
            elif (x-1, y+1) not in grid:
                x -= 1
                y += 1
            elif (x+1, y+1) not in grid:
                x += 1
                y += 1
            else:
                count += 1
                grid.add((x, y))
                break
        if y >= max_y:
            break
    print(count)


if __name__ == '__main__':
    main()

