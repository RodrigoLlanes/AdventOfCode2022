
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
    
    screen = [['.']*40 for _ in range(6)]

    cycle = -1
    x = 1
    for line in data:
        cycle += 1
        if abs(cycle % 40 - x) < 2:
            screen[cycle // 40][cycle % 40] = '#'
        if len(line) == 2:
            cycle += 1
            if abs((cycle % 40) - x) < 2:
                screen[cycle // 40][cycle % 40] = '#'
            x += line[1]
    for line in screen:
        print(''.join(line))


if __name__ == '__main__':
    main()

