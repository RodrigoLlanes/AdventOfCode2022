
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        n = len(line)//2
        inp.append((set(line[:n]), set(line[n:])))
    return inp


def main() -> None:
    data = load_input()
    result = 0
    for a, b in data:
        s = list(a.intersection(b))[0]
        if s.isupper():
            result += ord(s) - 38
        else:
            result += ord(s)

    print(result)


if __name__ == '__main__':
    main()

