
# [Día 9](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
|   9 | 00:15:15 | 1041 |     0 | 00:20:09 |  416 |     0 |

## [Parte 1](./Sol1.py)

El reto de hoy consiste en mover la "cabeza" de una cuerda y calcular el movimiento
de su "cola", para despues contar las casillas distintas por las que pasa dicha
cola.

```python3
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        d, n = line.strip().split()
        inp.append((d, int(n)))
    return inp


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def touching(a, b):
    return distance(a, b) < 2 or (distance(a, b) == 2 and a[0] != b[0] and a[1] != b[1])


def main() -> None:
    data = load_input()
    
    visited = {(0, 0)}
    h = [0, 0]
    t = [0, 0]

    for d, n in data:
        for _ in range(n):
            if d == 'U':
                h[1] += 1
            elif d == 'D':
                h[1] -= 1
            elif d == 'R':
                h[0] += 1
            elif d == 'L':
                h[0] -= 1

            if not touching(h, t):
                if h[0] != t[0]:
                    t[0] += (h[0] - t[0]) // abs(h[0] - t[0])
                if h[1] != t[1]:
                    t[1] += (h[1] - t[1]) // abs(h[1] - t[1])
            visited.add(tuple(t))
    print(len(visited))


if __name__ == '__main__':
    main()
```

Para la carga de los datos, simplemente leemos cada linea, la dividimos por el espacio
y convertimos a int la segunda parte.

```python3
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        d, n = line.strip().split()
        inp.append((d, int(n)))
    return inp
```

Creamos las funciones `distance` y `touching`, la primera calcula la [distancia Manhattan](https://es.wikipedia.org/wiki/Geometr%C3%ADa_del_taxista)
entre dos vectores y la segunda determina si "se están tocando" dos vectores. En
el [subredit oficial de AOC](https://www.reddit.com/r/adventofcode/) he descubierto
que esto se llama [distncia de Chebyshov](https://es.wikipedia.org/wiki/Distancia_de_Chebyshov).

```python3
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def touching(a, b):
    return distance(a, b) < 2 or (distance(a, b) == 2 and a[0] != b[0] and a[1] != b[1])
```

Mediante estas funciones, podemos ir moviendo la cabeza de una en una casilla y 
si no se toca con la cola, mover también esta. En cada iteración, convertimos a 
tupla la posición de la cola y la añadimos a un set, para poder llevar la cuenta.

```python3
def main() -> None:
    data = load_input()
    
    visited = {(0, 0)}
    h = [0, 0]
    t = [0, 0]

    for d, n in data:
        for _ in range(n):
            if d == 'U':
                h[1] += 1
            elif d == 'D':
                h[1] -= 1
            elif d == 'R':
                h[0] += 1
            elif d == 'L':
                h[0] -= 1

            if not touching(h, t):
                if h[0] != t[0]:
                    t[0] += (h[0] - t[0]) // abs(h[0] - t[0])
                if h[1] != t[1]:
                    t[1] += (h[1] - t[1]) // abs(h[1] - t[1])
            visited.add(tuple(t))
    print(len(visited))
```

## [Parte 2](./Sol2.py)

Para esta segunda parte, la carga de datos no varía y la resolución varía muy poco.

```python3
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        d, n = line.strip().split()
        inp.append((d, int(n)))
    return inp


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def touching(a, b):
    return distance(a, b) < 2 or (distance(a, b) == 2 and a[0] != b[0] and a[1] != b[1])


def main() -> None:
    data = load_input()
    
    visited = {(0, 0)}
    points = [[0, 0] for _ in range(10)]
    
    for d, n in data:
        for _ in range(n):
            if d == 'U':
                points[0][1] += 1
            elif d == 'D':
                points[0][1] -= 1
            elif d == 'R':
                points[0][0] += 1
            elif d == 'L':
                points[0][0] -= 1
            
            for i in range(1, 10):
                h = points[i-1]
                t = points[i] 
                if not touching(h, t):
                    if h[0] != t[0]:
                        t[0] += (h[0] - t[0]) // abs(h[0] - t[0])
                    if h[1] != t[1]:
                        t[1] += (h[1] - t[1]) // abs(h[1] - t[1])
            visited.add(tuple(points[-1]))
    print(len(visited))


if __name__ == '__main__':
    main()
```

El único cambio es que ahora en lugar de trabajar con dos nodos, trabajamos con 10,
en cada movimiento de la cabeza, movemos el primero y vamos iterando en el resto,
de modo que el n siga al n-1.

```python3
def main() -> None:
    data = load_input()
    
    visited = {(0, 0)}
    points = [[0, 0] for _ in range(10)]
    
    for d, n in data:
        for _ in range(n):
            if d == 'U':
                points[0][1] += 1
            elif d == 'D':
                points[0][1] -= 1
            elif d == 'R':
                points[0][0] += 1
            elif d == 'L':
                points[0][0] -= 1
            
            for i in range(1, 10):
                h = points[i-1]
                t = points[i] 
                if not touching(h, t):
                    if h[0] != t[0]:
                        t[0] += (h[0] - t[0]) // abs(h[0] - t[0])
                    if h[1] != t[1]:
                        t[1] += (h[1] - t[1]) // abs(h[1] - t[1])
            visited.add(tuple(points[-1]))
    print(len(visited))
```

