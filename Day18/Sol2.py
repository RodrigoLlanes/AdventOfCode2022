
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


def is_surrounded(point, points, bounds):
    stack = [point]
    visited = set()
    while len(stack):
        p = stack.pop()
        if p in visited:
            continue
        visited.add(p)
        for x, (lb, ub) in zip(p, bounds):
            if x < lb or x > ub:
                return False
        if p not in points:
            stack.extend(neightbours(p))
            continue
    return True
        



def main() -> None:
    data = load_input()
    max_y, min_y = max(map(lambda x: x[1], data)), min(map(lambda x: x[1], data))
    max_x, min_x = max(map(lambda x: x[0], data)), min(map(lambda x: x[0], data))
    max_z, min_z = max(map(lambda x: x[2], data)), min(map(lambda x: x[2], data))
    bounds = ((min_x, max_x), (min_y, max_y), (min_z, max_z))
    
    stack = []
    stack.extend(data)
    area = 0
    while len(stack):
        point = stack.pop()
        neight = neightbours(point)
        empty = neight - data
        empty = set(filter(lambda p: not is_surrounded(p, data, bounds), empty))
        area += len(empty)
    print(area)



if __name__ == '__main__':
    main()

