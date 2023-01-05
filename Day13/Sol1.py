
def load_input() -> list:
    inp = [[]]
    for line in open('input', 'r').readlines():
        line = line.strip()
        if len(line) == 0:
            inp.append([])
        else:
            inp[-1].append(eval(line))
    return inp


def check(left, right):
    if isinstance(left, list):
        if not isinstance(right, list):
            return check(left, [right])
        for item0, item1 in zip(left, right):
            r = check(item0, item1)
            if r == 0:
                continue
            return r
        return len(right) - len(left)
    elif isinstance(right, list):
        return check([left], right)
    else:
        if left < right:
            return 1
        elif left == right:
            return 0
        return -1


def main() -> None:
    data = load_input()
    
    res = 0
    for index, (left, right) in enumerate(data):
        if check(left, right) > 0:
            res += index+1
    print(res)



if __name__ == '__main__':
    main()

