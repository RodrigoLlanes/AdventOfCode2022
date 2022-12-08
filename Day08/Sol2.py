
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        inp.append(line)
    return inp


def main() -> None:
    data = load_input()
    _max = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            score = 1
            curr = 0
            for tree in reversed(data[i][:j]):
                curr += 1
                if tree >= data[i][j]:
                    break
            
            score *= curr
            curr = 0
            for tree in data[i][j+1:]:
                curr += 1
                if tree >= data[i][j]:
                    break
            
            score *= curr
            curr = 0
            for a in range(i-1, -1, -1):
                curr += 1
                if data[a][j] >= data[i][j]:
                    break

            score *= curr
            curr = 0
            for a in range(i+1, len(data[i])):
                curr += 1
                if data[a][j] >= data[i][j]:
                    break

            _max = max(_max, score * curr)
    print(_max)


if __name__ == '__main__':
    main()

