
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip().split(',')
        first, second = line[0].split('-'), line[1].split('-')
        first = set(range(int(first[0]), int(first[1])+1))
        second = set(range(int(second[0]), int(second[1])+1))
        inp.append((first, second))
    return inp


def main() -> None:
    data = load_input()
    overlaps = 0
    for a, b in data:
        if len(a - b) == 0 or len(b - a) == 0:
            overlaps += 1
    print(overlaps)


if __name__ == '__main__':
    main()

