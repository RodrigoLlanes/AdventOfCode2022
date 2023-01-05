
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
    points = [[0, 0] for _ in range(10)]
    
    for d, n in data:
        for _ in range(n):
            if d == 'U':
                points[0][1] += 1
            elif d == 'D':
                points[0][1] -= 1
            elif d == 'R':
                points[0][0] += 1
            elif d == 'L':
                points[0][0] -= 1
            
            for i in range(1, 10):
                h = points[i-1]
                t = points[i] 
                if not touching(h, t):
                    if h[0] != t[0]:
                        t[0] += (h[0] - t[0]) // abs(h[0] - t[0])
                    if h[1] != t[1]:
                        t[1] += (h[1] - t[1]) // abs(h[1] - t[1])
            visited.add(tuple(points[-1]))
    print(len(visited))


if __name__ == '__main__':
    main()

