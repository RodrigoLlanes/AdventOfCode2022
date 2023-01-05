
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        inp.append(int(line))
    return inp


def main() -> None:
    data = load_input()
    N = len(data)

    indexes = list(range(len(data)))
    for _ in range(1):
        for n in range(len(data)):
            n = n % len(data)
            i = indexes[n]
            inc = data[n]

            j = (i + inc)
            while j >= len(data):
                inc = j // (N-1)
                j -= inc * (N-1)
            while j < 0:
                inc = j // (N-1)
                j -= (inc - 1) * (N - 1)
            for index, v in enumerate(indexes):
                if v == i:
                    indexes[index] = j
                elif i < v <= j:
                    indexes[index] -= 1
                elif j <= v < i:
                    indexes[index] += 1
    d = [-1 for _ in range(len(data))]
    for n, i in enumerate(indexes):
        d[i] = data[n]
    z_index = d.index(0)
    print(d[(z_index + 1000) % len(d)], d[(z_index + 2000) % len(d)], d[(z_index + 3000) % len(d)])
    print(d[(z_index + 1000) % len(d)] + d[(z_index + 2000) % len(d)] + d[(z_index + 3000) % len(d)])


if __name__ == '__main__':
    main()

