
def load_input() -> list:
    inp = []
    for i, line in enumerate(open('input', 'r').readlines()):
        if i%3 == 0:
            inp.append([])
        line = line.strip()
        inp[-1].append(set(line))
    return inp


def main() -> None:
    data = load_input()
    result = 0
    for a, b, c in data:
        s = list(a.intersection(b).intersection(c))[0]
        if s.isupper():
            result += ord(s) - 38
        else:
            result += ord(s) - 96
    print(result)


if __name__ == '__main__':
    main()

