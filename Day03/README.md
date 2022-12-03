
# [Día ](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
| 1   | 00:02:22 |  655 |     0 | 00:03:26 |  513 |     0 |

## [Parte 1](./Sol1.py)

Seguimos con los retos de calentamiento, para esta primera parte simplemente
hay que calcular la intersección entre dos sets.

```python3
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        n = len(line)//2
        inp.append((set(line[:n]), set(line[n:])))
    return inp


def main() -> None:
    data = load_input()
    result = 0
    for a, b in data:
        s = list(a.intersection(b))[0]
        if s.isupper():
            result += ord(s) - 38
        else:
            result += ord(s)

    print(result)


if __name__ == '__main__':
    main()
```

A la hora de cargar los datos, aprovechamos para dividir cada línea por la mitad
y convertir cada parte en un set.

```python3
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        n = len(line)//2
        inp.append((set(line[:n]), set(line[n:])))
    return inp
```

Para cada par de sets, calculamos su intersección y sumamos el valor de ese símbolo.

```python3
def main() -> None:
    data = load_input()
    result = 0
    for a, b in data:
        s = list(a.intersection(b))[0]
        if s.isupper():
            result += ord(s) - 38
        else:
            result += ord(s)

    print(result)
```

## [Parte 2](./Sol2.py)

Esta segunda parte es trivial, en lugar de calcular la intersección de dos sets,
hay que calcularla de 3.

```python3
def load_input() -> list:
    inp = []
    for i, line in enumerate(open('input', 'r').readlines()):
        if i%3 == 0:
            inp.append([])
        line = line.strip()
        inp[-1].append(set(line))
    return inp


def main() -> None:
    data = load_input()
    result = 0
    for a, b, c in data:
        s = list(a.intersection(b).intersection(c))[0]
        if s.isupper():
            result += ord(s) - 38
        else:
            result += ord(s) - 96
    print(result)


if __name__ == '__main__':
    main()

```

Al cargar los datos en lugar de dividir cada línea en dos, agrupamos las lineas
de tres en tres.

```python3
def load_input() -> list:
    inp = []
    for i, line in enumerate(open('input', 'r').readlines()):
        if i%3 == 0:
            inp.append([])
        line = line.strip()
        inp[-1].append(set(line))
    return inp
```

Y calculamos el resultado como la suma del valor de las intersecciónes de cada 
grupo de tres.

```python3
def main() -> None:
    data = load_input()
    result = 0
    for a, b, c in data:
        s = list(a.intersection(b).intersection(c))[0]
        if s.isupper():
            result += ord(s) - 38
        else:
            result += ord(s) - 96
    print(result)
```


