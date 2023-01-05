from heapq import heapify, heappush, heappop


def load_input():
    inp = []
    S = None
    E = None
    for y, line in enumerate(open('input', 'r').readlines()):
        line = line.strip()
        if (x := line.find('S')) >= 0:
            S = [y, x]
            line = line.replace('S', 'a')
        if (x := line.find('E')) >= 0:
            E = [y, x]
            line = line.replace('E', 'z')
        line = [ord(char) - ord('a') for char in line]
        inp.append(line)
    return inp, S, E


def main() -> None:
    grid, _, E = load_input()
    m = 1000
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell == 0:
                m = min(m, find(grid, [y, x], E))
    print(m)


def find(grid, S, E):
    heap = []
    heapify(heap)
    heappush(heap, [0, S])
    visited = set()
    while len(heap):
        d, (y, x) = heappop(heap)
        if (y, x) in visited:
            continue
        visited.add((y, x))
        if [y, x] == E:
            return d

        if x > 0 and grid[y][x-1] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y, x-1]])
        if x < len(grid[0]) - 1 and  grid[y][x+1] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y, x+1]])
        if y > 0 and grid[y-1][x] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y-1, x]])
        if y < len(grid) - 1 and  grid[y+1][x] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y+1, x]])

    return 1000


if __name__ == '__main__':
    main()

