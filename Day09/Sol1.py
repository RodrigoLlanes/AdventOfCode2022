
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        d, n = line.strip().split()
        inp.append((d, int(n)))
    return inp


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def touching(a, b):
    return distance(a, b) < 2 or (distance(a, b) == 2 and a[0] != b[0] and a[1] != b[1])


def main() -> None:
    data = load_input()
    
    visited = {(0, 0)}
    h = [0, 0]
    t = [0, 0]

    for d, n in data:
        for _ in range(n):
            if d == 'U':
                h[1] += 1
            elif d == 'D':
                h[1] -= 1
            elif d == 'R':
                h[0] += 1
            elif d == 'L':
                h[0] -= 1

            if not touching(h, t):
                if h[0] != t[0]:
                    t[0] += (h[0] - t[0]) // abs(h[0] - t[0])
                if h[1] != t[1]:
                    t[1] += (h[1] - t[1]) // abs(h[1] - t[1])
            visited.add(tuple(t))
    print(len(visited))


if __name__ == '__main__':
    main()

