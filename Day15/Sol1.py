import re


def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = list(map(int, re.findall(r'-?\d+', line.strip())))
        inp.append(line)
    return inp


def main() -> None:
    data = load_input()
    n = 2000000
    positions = set()
    for sx, sy, bx, by in data:
        d = abs(sx - bx) + abs(sy - by)
        dy = abs(n - sy)
        diff = d - dy
        if dy > d:
            continue
        for x in range(sx - diff, sx + diff + 1):
            if (x, n) == (bx, by):
                continue
            positions.add(x)
    print(len(positions))


if __name__ == '__main__':
    main()

