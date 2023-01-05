
def load_input():
    inp = set()
    for line in open('input', 'r').readlines():
        line = tuple(map(int, line.strip().split(',')))
        inp.add(line)
    return inp


def neightbours(p):
    x, y, z = p
    return set([
            (x+1, y, z),
            (x-1, y, z),
            (x, y+1, z),
            (x, y-1, z),
            (x, y, z+1),
            (x, y, z-1),
            ])


def main() -> None:
    data = load_input()
    
    stack = []
    stack.extend(data)
    area = 0
    while len(stack):
        point = stack.pop()
        neight = neightbours(point)
        empty = neight - data
        area += len(empty)
    print(area)



if __name__ == '__main__':
    main()

