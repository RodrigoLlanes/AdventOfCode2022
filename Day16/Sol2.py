from collections import defaultdict
from heapq import heapify, heappush, heappop
import re


def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        valve = line[len('Valve '): len('Valve ')+2]
        flow_rate = int(re.findall(r'\d+', line)[0])
        if 'valves ' in line:
            n = line.index('valves ') + len('valves ')
        else:
            n = line.index('valve ')+ len('valve ')
        neightbours = line[n:].split(', ')
        inp.append((valve, flow_rate, neightbours))
    return inp


def main() -> None:
    data = load_input()
    graph = defaultdict(dict)
    candidates = set()
    rates = {}

    for valve, rate, neightbours in data:
        if rate > 0:
            candidates.add(valve)
            rates[valve] = rate
        for neightbour in neightbours:
            graph[valve][neightbour] = 1
    
    paths = defaultdict(lambda: 10e12)
    for i, neigh in graph.items():
        paths[i, i] = 0
        for j in neigh.keys():
            paths[i, j] = 1

    for k in graph.keys():
        for i in graph.keys():
            for j in graph.keys():
                paths[i, j] = min(paths[i, j], paths[i, k] + paths[k, j])

    heap = []
    heapify(heap)
    heappush(heap, [0, (26, 'AA'), (26, 'AA'), set()])
    max_score = 0
    bests = defaultdict(lambda: -1)
    while len(heap):
        score, ts1, ts2, visited = heappop(heap)
        score = -score
        
        (time, state), ts2 = sorted([ts1, ts2], reverse=True)
    
        if score > max_score:
            max_score = score

        key = frozenset(visited)
        key = (key, (time, state), ts2)

        if score > bests[key]:
            bests[key] = score
        else:
            continue

        options = candidates - visited
        for option in options:
            distance = paths[state, option]

            if time <= distance + 1:
                continue

            t = time - (distance + 1)
            s = score + rates[option] * t
            heappush(heap, [-s, (t, option), ts2, visited.union({option})])

    print(max_score)


if __name__ == '__main__':
    main()

