
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        inp.append(line)
    return inp


def main() -> None:
    data = load_input()
    res = 0
    for number in data:
        n = len(number)-1
        v = 0
        for i, digit in zip(range(n, -1, -1), number):
            if digit.isnumeric():
                d = int(digit)
            elif digit == '-':
                d = -1
            else:
                d = -2
            v += d * 5 ** i
        res += v
    
    n = 1
    while sum(3 * 5 ** i for i in range(n)) < res:
        n += 1
    
    tras = ''
    curr = 0
    for digit in range(n-1, -1, -1):
        max_next = sum(2 * 5 ** i for i in range(digit))
        if curr + max_next + -2 * 5 ** digit >= res:
            curr += -2 * 5 ** digit
            tras += '='
        elif curr + max_next + -1 * 5 ** digit >= res:
            curr += -1 * 5 ** digit
            tras += '-'
        elif curr + max_next + 0 * 5 ** digit >= res:
            curr += 0 * 5 ** digit
            tras += '0' 
        elif curr + max_next + 1 * 5 ** digit >= res:
            curr += 1 * 5 ** digit
            tras += '1' 
        elif curr + max_next + 2 * 5 ** digit >= res:
            curr += 2 * 5 ** digit
            tras += '2'
    print(tras)




if __name__ == '__main__':
    main()

