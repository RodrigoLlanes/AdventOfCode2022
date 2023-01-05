
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        inp.append(line)
    return inp


def main() -> None:
    data = load_input()


if __name__ == '__main__':
    main()

