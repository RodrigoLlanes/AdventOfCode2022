
def load_input() -> list:
    inp = [0]
    for line in open('input', 'r').readlines():
        line = line.strip()
        if len(line) == 0:
            inp.append(0)
        else:
            inp[-1] += int(line)
    return inp


def main() -> None:
    data = load_input()
    print(max(data))


if __name__ == '__main__':
    main()

