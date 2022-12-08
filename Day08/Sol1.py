
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        inp.append(line)
    return inp


def main() -> None:
    data = load_input()
    visible = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if all(tree < data[i][j] for tree in data[i][:j]):
                visible += 1
            elif all(tree < data[i][j] for tree in data[i][j+1:]):
                visible += 1
            elif all(data[a][j] < data[i][j] for a in range(i)):
                visible += 1
            elif all(data[a][j] < data[i][j] for a in range(i+1, len(data[i]))):
                visible += 1
    print(visible)


if __name__ == '__main__':
    main()

