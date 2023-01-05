
import re
from collections import defaultdict


def load_input():
    dependencies = defaultdict(set)
    depend_of = defaultdict(set)
    ops = {}
    calculated = set()
    for line in open('input', 'r').readlines():
        line = line.strip()
        monkey, data = line.split(': ')
        if re.match(r'\d+', data):
            ops[monkey] = int(data)
            calculated.add(monkey)
        else:
            for i, symb in enumerate(['+', '-', '*', '/']):
                if data.find(symb) > 0:
                    a, b = data.split(f' {symb} ')
                    dependencies[monkey] = {a, b}
                    ops[monkey] = (i, a, b)
                    depend_of[a].add(monkey)
                    depend_of[b].add(monkey)
    return dependencies, ops, depend_of, calculated


def main():
    dependencies, ops, depend_of, calculated = load_input()
    
    del ops['humn']
    calculated.remove('humn')

    stack = []
    for c in calculated:
        stack.extend(depend_of[c])
    
    target = node = None
    while len(stack):
        monkey = stack.pop()

        if monkey in calculated:
            continue
        if len(dependencies[monkey] - calculated) > 0:
            continue

        op, a, b = ops[monkey]
        if op == 0:
            ops[monkey] = ops[a] + ops[b]
        elif op == 1:
            ops[monkey] = ops[a] - ops[b]
        elif op == 2:
            ops[monkey] = ops[a] * ops[b]
        else:
            ops[monkey] = ops[a] / ops[b]

        calculated.add(monkey)
        for m in depend_of[monkey]:
            stack.append(m)
    
    _, a, b = ops['root']
    if a in calculated:
        target = ops[a]
        node = b
    else:
        target = ops[b]
        node = a

    while True:
        if node == 'humn':
            break

        op, a, b = ops[node]
        if a in calculated:
            val = ops[a]
            node = b
        elif b in calculated:
            val = ops[b]
            node = a
        
        if op == 0:
            target -= val
        elif op == 1:
            if a in calculated:
                target = val - target
            elif b in calculated:
                target += val
        elif op == 2:
            target /= val
        else: 
            if a in calculated:
                target = val / target
            elif b in calculated:
                target *= val
    print(target)


if __name__ == '__main__':
    main()

