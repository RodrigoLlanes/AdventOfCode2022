
# [Día 12](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
|  12 | 00:27:08 | 1771 |     0 | 00:30:59 | 1590 |     0 |

## [Parte 1](./Sol1.py)

El problema de hoy es básicamente la busqueda del camino más corto, por lo que
podemos simplemente aplicar [Dijkstra](https://es.wikipedia.org/wiki/Algoritmo_de_Dijkstra)
o [A\*](https://es.wikipedia.org/wiki/Algoritmo_de_b%C3%BAsqueda_A*).

```python3
from heapq import heapify, heappush, heappop


def load_input():
    inp = []
    S = None
    E = None
    for y, line in enumerate(open('input', 'r').readlines()):
        line = line.strip()
        if (x := line.find('S')) >= 0:
            S = [y, x]
            line = line.replace('S', 'a')
        if (x := line.find('E')) >= 0:
            E = [y, x]
            line = line.replace('E', 'z')
        line = [ord(char) - ord('a') for char in line]
        inp.append(line)
    return inp, S, E


def main() -> None:
    grid, S, E = load_input()
    
    heap = []
    heapify(heap)
    heappush(heap, [0, S])
    visited = set()
    while len(heap):
        d, (y, x) = heappop(heap)
        if (y, x) in visited:
            continue
        visited.add((y, x))
        if [y, x] == E:
            print(d)
            return

        if x > 0 and grid[y][x-1] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y, x-1]])
        if x < len(grid[0]) - 1 and  grid[y][x+1] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y, x+1]])
        if y > 0 and grid[y-1][x] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y-1, x]])
        if y < len(grid) - 1 and  grid[y+1][x] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y+1, x]])

    print('Error')


if __name__ == '__main__':
    main()
```

Para la carga de datos, reemplazamos cada letra por su valor, y nos guardamos
la posición inicial y el destino.

```python3
def load_input():
    inp = []
    S = None
    E = None
    for y, line in enumerate(open('input', 'r').readlines()):
        line = line.strip()
        if (x := line.find('S')) >= 0:
            S = [y, x]
            line = line.replace('S', 'a')
        if (x := line.find('E')) >= 0:
            E = [y, x]
            line = line.replace('E', 'z')
        line = [ord(char) - ord('a') for char in line]
        inp.append(line)
    return inp, S, E
```

Dados estos datos, aplicamos nuestro algoritmo de busqueda de camino mínimo,
teniendo en cuenta que solo podemos movernos a casillas 4-adyacentes con una altura
menor o igual a la actual más uno.

```python3
def main() -> None:
    grid, S, E = load_input()
    
    heap = []
    heapify(heap)
    heappush(heap, [0, S])
    visited = set()
    while len(heap):
        d, (y, x) = heappop(heap)
        if (y, x) in visited:
            continue
        visited.add((y, x))
        if [y, x] == E:
            print(d)
            return

        if x > 0 and grid[y][x-1] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y, x-1]])
        if x < len(grid[0]) - 1 and  grid[y][x+1] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y, x+1]])
        if y > 0 and grid[y-1][x] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y-1, x]])
        if y < len(grid) - 1 and  grid[y+1][x] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y+1, x]])

    print('Error')
```

## [Parte 2](./Sol2.py)

Para la parte dos mi solución no es especialmente eficiente, itero en cada posible
posición inicial y calculo su camino mínimo, y nos quedamos con el mínimo total.

Una alternativa más eficiente, por ejemplo, sería recorrer el camino a la inversa
y parar al llegar a una altura 0.

```python3
from heapq import heapify, heappush, heappop


def load_input():
    inp = []
    S = None
    E = None
    for y, line in enumerate(open('input', 'r').readlines()):
        line = line.strip()
        if (x := line.find('S')) >= 0:
            S = [y, x]
            line = line.replace('S', 'a')
        if (x := line.find('E')) >= 0:
            E = [y, x]
            line = line.replace('E', 'z')
        line = [ord(char) - ord('a') for char in line]
        inp.append(line)
    return inp, S, E


def main() -> None:
    grid, _, E = load_input()
    m = 1000
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell == 0:
                m = min(m, find(grid, [y, x], E))
    print(m)


def find(grid, S, E):
    heap = []
    heapify(heap)
    heappush(heap, [0, S])
    visited = set()
    while len(heap):
        d, (y, x) = heappop(heap)
        if (y, x) in visited:
            continue
        visited.add((y, x))
        if [y, x] == E:
            return d

        if x > 0 and grid[y][x-1] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y, x-1]])
        if x < len(grid[0]) - 1 and  grid[y][x+1] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y, x+1]])
        if y > 0 and grid[y-1][x] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y-1, x]])
        if y < len(grid) - 1 and  grid[y+1][x] <= grid[y][x] + 1:
            heappush(heap, [d+1, [y+1, x]])

    return 1000


if __name__ == '__main__':
    main()

```

