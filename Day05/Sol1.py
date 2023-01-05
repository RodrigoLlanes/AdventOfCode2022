
def load_input() -> tuple:
    crates = [[] for _ in range(9)]
    instructions = []
    inp = open('input', 'r').readlines()
 
    while True:
        line = inp.pop(0)
        if len(line.strip()) == 0:
            break
        for ind, i in enumerate(range(1, len(line), 4)):
            if line[i].isalpha():
                crates[ind].append(line[i])
    
    for line in inp:
        line = line.split()
        instructions.append((int(line[1]), int(line[3])-1, int(line[5])-1))
    
    return crates, instructions


def main() -> None:
    crates, instructions = load_input()
    for a, b, c in instructions:
        crate = crates[b][:a]
        crates[b] = crates[b][a:]
        crates[c] = list(reversed(crate)) + crates[c]

    for crate in crates:
        print(crate[0] if len(crate) else " ", end='')
    print() 


if __name__ == '__main__':
    main()

