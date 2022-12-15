
# [Día 11](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
|  11 | 00:22:15 |  738 |     0 | 00:41:13 | 1352 |     0 |

## [Parte 1](./Sol1.py)

La parte más "complicada" de hoy es la carga de los datos, una vez los tengamos,
solo hay que aplicar las reglas en orden.

```python3
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
```

Para cada mono, guardamos sus objetos, la operación que aplica, el número por el
que comprueba si es divisible y el destinatario en caso positivo y en caso negativo.

```python3
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
```

A la hora de obtener la solución, iteramos sobre los objetos de cada mono,
los contamos, aplicamos las operaciones pertinentes y se los pasamos a quien
corresponda.

Repetimos este proceso veinte veces, ordenamos la suma todas las actualizaciones
realizadas por cada mono y multiplicamos las dos últimas.

```python3
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
```

## [Parte 2](./Sol2.py)

Para esta segunda parte, deberemos realizar 10000 iteraciones en lugar de 20 y
no hay que dividir los valores entre 3, lo que hará que se dispare el tamaño
de las variables, por lo que habrá que idear algún mecanismo para mantener los
valores manejables.

```python3
from math import prod


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
    p = prod(monkey[2] for monkey in data)
    for _ in range(10000):
        for i, monkey in enumerate(data):
            for item in monkey[0][:]:
                inspected[i] += 1
                old = item
                old = eval(monkey[1])
                old %= p
                if (old % monkey[2] == 0):
                    data[monkey[3]][0].append(old)
                else:
                    data[monkey[4]][0].append(old)
            monkey[0] = []
    inspected.sort()
    print(inspected[-1] * inspected[-2])


if __name__ == '__main__':
    main()
```

Para mantener los valores acotados, calculamos el producto del divisor de cada
mono `p`, y lo empleamos para acotar los valores al modulo `p`.

```python3
def main() -> None:
    data = load_input()
    inspected = [0] * len(data)
    p = prod(monkey[2] for monkey in data)
    for _ in range(10000):
        for i, monkey in enumerate(data):
            for item in monkey[0][:]:
                inspected[i] += 1
                old = item
                old = eval(monkey[1])
                old %= p
                if (old % monkey[2] == 0):
                    data[monkey[3]][0].append(old)
                else:
                    data[monkey[4]][0].append(old)
            monkey[0] = []
    inspected.sort()
    print(inspected[-1] * inspected[-2])
```

