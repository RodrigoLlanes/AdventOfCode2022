import re


def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = list(map(int, re.findall(r'-?\d+', line.strip())))
        inp.append(line)
    return inp


def main() -> None:
    data = load_input()
    n = 4000000

    for y in range(n+1):
        areas = []
        for sx, sy, bx, by in data:
            d = abs(sx - bx) + abs(sy - by)
            dy = abs(y - sy)
            diff = d - dy
            if diff > 0:
                x_min, x_max = sx - diff, sx + diff
                areas.append((x_min, x_max))
        prev = -1 
        i = 0
        while prev != i:
            prev = i
            for a_min, a_max in areas:
                if a_min <= i <= a_max:
                    i = a_max + 1
        if i <= n:
            print(i * 4000000 + y)
            return


if __name__ == '__main__':
    main()

