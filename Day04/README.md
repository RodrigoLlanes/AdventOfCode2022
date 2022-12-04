
# [Día 4](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
| 4   | 00:12:03 | 5744 |     0 | 00:14:31 | 4533 |     0 |

## [Parte 1](./Sol1.py)

Seguimos con el calentamiento, la primera parte de hoy consiste en comprobar si 
de dos rangos, uno es subconjunto de otro.

```python3
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip().split(',')
        first, second = line[0].split('-'), line[1].split('-')
        first = set(range(int(first[0]), int(first[1])+1))
        second = set(range(int(second[0]), int(second[1])+1))
        inp.append((first, second))
    return inp


def main() -> None:
    data = load_input()
    overlaps = 0
    for a, b in data:
        if len(a - b) == 0 or len(b - a) == 0:
            overlaps += 1
    print(overlaps)


if __name__ == '__main__':
    main()

```

Para la carga de los datos, podríamos trabajar solo con los extremos de cada
rango, pero por comodidad, vamos a generar para cada rango, un set que contenga
todos los elementos en ese rango.

```python3
inp = []
for line in open('input', 'r').readlines():
    line = line.strip().split(',')
    first, second = line[0].split('-'), line[1].split('-')
    first = set(range(int(first[0]), int(first[1])+1))
    second = set(range(int(second[0]), int(second[1])+1))
    inp.append((first, second))    
```

Para comprobar si un conjunto es subconjunto de otro, comprobamos si su resta es
el conjunto vacío.

```python3
overlaps = 0
for a, b in data:
    if len(a - b) == 0 or len(b - a) == 0:
        overlaps += 1
print(overlaps)
```

## [Parte 2](./Sol2.py)

Para la segunda parte comprobamos si existe intersección entre ambos rangos.

```python3
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip().split(',')
        first, second = line[0].split('-'), line[1].split('-')
        first = set(range(int(first[0]), int(first[1])+1))
        second = set(range(int(second[0]), int(second[1])+1))
        inp.append((first, second))
    return inp


def main() -> None:
    data = load_input()
    overlaps = 0
    for a, b in data:
        if len(a.intersection(b)):
            overlaps += 1
    print(overlaps)


if __name__ == '__main__':
    main()
```

La carga de datos es identica a la de la parte anterior y para comprobar si
existe intersección entre dos rangos, comprobamos si la longitud de la 
intersección de sus sets es mayor que zero.

```python3
overlaps = 0
for a, b in data:
    if len(a.intersection(b)):
        overlaps += 1
print(overlaps)
```


