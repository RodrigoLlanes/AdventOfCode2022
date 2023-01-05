
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip().split()
        if len(line) == 2:
            line[1] = int(line[1])
        inp.append(line)
    return inp


def main() -> None:
    data = load_input()
    
    res = 0

    cycle = 0
    x = 1
    for line in data:
        cycle += 1
        if (cycle - 20) % 40 == 0:
            res += cycle * x
        if len(line) == 2:
            cycle += 1
            if (cycle - 20) % 40 == 0:
                res += cycle * x
            x += line[1]
    print(res)


if __name__ == '__main__':
    main()

