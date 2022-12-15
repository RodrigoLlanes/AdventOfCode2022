
def load_input() -> list:
    inp = []
    data = open('input', 'r').read().strip().split('\n\n')
    for monkey in data:
        monkey = monkey.split('\n')
        items = list(map(int, monkey[1][len('  Starting items: '):].strip().split(',')))
        operation = monkey[2][len('  Operation: new = '):].strip()
        test = int(monkey[3][len('  Test: divisible by '):].strip())
        true_test = int(monkey[4][len('    If true: throw to monkey '):].strip())
        false_test = int(monkey[5][len('    If false: throw to monkey '):].strip())
        inp.append([items, operation, test, true_test, false_test])
    return inp


def main() -> None:
    data = load_input()
    inspected = [0] * len(data)
    for _ in range(20):
        for i, monkey in enumerate(data):
            for item in monkey[0][:]:
                inspected[i] += 1
                old = item
                old = eval(monkey[1])
                old //= 3
                if (old % monkey[2] == 0):
                    data[monkey[3]][0].append(old)
                else:
                    data[monkey[4]][0].append(old)
            monkey[0] = []
    inspected.sort()
    print(inspected[-1] * inspected[-2])


if __name__ == '__main__':
    main()

