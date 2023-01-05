from heapq import heapify, heappush, heappop
import re


def load_input():
    inp = {}
    for line in open('input', 'r').readlines():
        line = line.strip()
        line = list(map(int, re.findall(r'(\d+)', line)))
        inp[line[0]] = [[(0, line[1])], [(0, line[2])], [(0, line[3]), (1, line[4])], [(0, line[5]), (2, line[6])]]
    return inp


def maximize_geodes(icolectors, iores, costs, itime):
    max_ore_cost = max(i[0][1] for i in costs)
    max_costs = [max_ore_cost, costs[2][1][1], costs[3][1][1]]

    heap = []
    heapify(heap)
    heappush(heap, (iores, icolectors, itime))
    max_score = 0
    visited = set()
    while len(heap):
        ores, colectors, time = heappop(heap)

        if time == 0:
            max_score = max(max_score, ores[-1])
            continue
        
        for i, cost in enumerate(max_costs):
            if colectors[i] >= cost:
                colectors[i] = cost
            if ores[i] >= time * cost - colectors[i] * (time - 1):
                ores[i] = time * cost - colectors[i] * (time - 1)

        key = (*ores, *colectors, time)
        if key in visited:
            continue
        visited.add(key)

        time -= 1
        old_ores = ores.copy()
        for i, colector in enumerate(colectors):
            ores[i] += colector
        for i, cost in enumerate(costs):
            if all(old_ores[ore] >= value for ore, value in cost):
                nores = ores.copy()
                ncolectors = colectors.copy()
                for ore, value in cost:
                    nores[ore] -= value
                ncolectors[i] += 1
                heappush(heap, (nores, ncolectors, time))
        heappush(heap, (ores.copy(), colectors.copy(), time))
    return max_score


def main() -> None:
    data = load_input()
    max_score = 1
    for blueprint in range(1, 4):
        geodes = maximize_geodes([1, 0, 0, 0], [0, 0, 0, 0], data[blueprint], 32)
        max_score *= geodes
    print(max_score)


if __name__ == '__main__':
    main()

