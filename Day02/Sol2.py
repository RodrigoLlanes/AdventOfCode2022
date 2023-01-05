
OPTIONS = ['A', 'B', 'C']


def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
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
        i = OPTIONS.index(act)
        if resp == 'X':
            resp = OPTIONS[i-1]
        elif resp == 'Y':
            resp = act
        else:
            resp = OPTIONS[(i+1)%3]
        score += get_score(act, resp)

    print(score)


if __name__ == '__main__':
    main()

