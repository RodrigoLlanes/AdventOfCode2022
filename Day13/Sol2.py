from functools import cmp_to_key


def load_input() -> list:
    inp = [[[2]], [[6]]]
    for line in open('input', 'r').readlines():
        line = line.strip()
        if len(line) == 0:
            continue
        else:
            inp.append(eval(line))
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
        v = len(right) - len(left)
        return (v) / abs(v) if v != 0 else 0
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
    data.sort(key=cmp_to_key(check), reverse=True)
    print((data.index([[2]])+1) * (data.index([[6]])+1))



if __name__ == '__main__':
    main()

