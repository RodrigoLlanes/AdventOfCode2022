
OPTIONS = ['A', 'B', 'C']


def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip().translate(str.maketrans({'X': 'A', 'Y': 'B', 'Z': 'C'}))
        inp.append(line.split())
    return inp


def get_score(act, resp):
    score = OPTIONS.index(resp) + 1
    p = (OPTIONS.index(act) - OPTIONS.index(resp)) % 3
    if p == 0:
        score += 3
    if p == 2:
        score += 6
    return score


def main() -> None:
    data = load_input()
    score = 0

    for (act, resp) in data:     
        score += get_score(act, resp)
    print(score)


if __name__ == '__main__':
    main()

