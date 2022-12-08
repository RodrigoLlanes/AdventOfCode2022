
# [Día 8](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
|   8 | 00:04:52 |  129 |     0 | 00:13:38 |  277 |     0 |

## [Parte 1](./Sol1.py)

Para esta primera parte, debemos comprobar para cuantos arboles es "visible" el
exterior.

```python3
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        inp.append(line)
    return inp


def main() -> None:
    data = load_input()
    visible = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if all(tree < data[i][j] for tree in data[i][:j]):
                visible += 1
            elif all(tree < data[i][j] for tree in data[i][j+1:]):
                visible += 1
            elif all(data[a][j] < data[i][j] for a in range(i)):
                visible += 1
            elif all(data[a][j] < data[i][j] for a in range(i+1, len(data[i]))):
                visible += 1
    print(visible)


if __name__ == '__main__':
    main()
```

La carga de datos es trivial, así que nos centraremos en el calculo de la solución.

Iteramos para cada elemento de la matriz y comprobamos si desde el es visible
cualquiera de los extremos. O lo que es lo mismo, iteramos en la parte superior 
de la columna, la parte inferior, la parte derecha de la fila y la parte izquierda,
y comprobamos si todos los elementos de alguna de ellas son menores estrictamente
al arbol actual.

```python3
def main() -> None:
    data = load_input()
    visible = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if all(tree < data[i][j] for tree in data[i][:j]):
                visible += 1
            elif all(tree < data[i][j] for tree in data[i][j+1:]):
                visible += 1
            elif all(data[a][j] < data[i][j] for a in range(i)):
                visible += 1
            elif all(data[a][j] < data[i][j] for a in range(i+1, len(data[i]))):
                visible += 1
    print(visible)
```

## [Parte 2](./Sol2.py)

Para esta segunda parte, debemos encontrar el mayor score (producto del número de
arboles visibles en cada dirección).

```python3
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        inp.append(line)
    return inp


def main() -> None:
    data = load_input()
    _max = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            score = 1
            curr = 0
            for tree in reversed(data[i][:j]):
                curr += 1
                if tree >= data[i][j]:
                    break
            
            score *= curr
            curr = 0
            for tree in data[i][j+1:]:
                curr += 1
                if tree >= data[i][j]:
                    break
            
            score *= curr
            curr = 0
            for a in range(i-1, -1, -1):
                curr += 1
                if data[a][j] >= data[i][j]:
                    break

            score *= curr
            curr = 0
            for a in range(i+1, len(data[i])):
                curr += 1
                if data[a][j] >= data[i][j]:
                    break

            _max = max(_max, score * curr)
    print(_max)


if __name__ == '__main__':
    main()
```

Básicamente hacemos lo mismo que en el apartado anterior, pero en lugar de comprobar
que todos sean menores estrictamente, contamos cuantos lo son seguidos desde el
elemento seleccionado, en cuanto uno es mayor o igual, dejamos de contar esa fila
o columna y pasamos a la siguiente.

```python3
def main() -> None:
    data = load_input()
    _max = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            score = 1
            curr = 0
            for tree in reversed(data[i][:j]):
                curr += 1
                if tree >= data[i][j]:
                    break
            
            score *= curr
            curr = 0
            for tree in data[i][j+1:]:
                curr += 1
                if tree >= data[i][j]:
                    break
            
            score *= curr
            curr = 0
            for a in range(i-1, -1, -1):
                curr += 1
                if data[a][j] >= data[i][j]:
                    break

            score *= curr
            curr = 0
            for a in range(i+1, len(data[i])):
                curr += 1
                if data[a][j] >= data[i][j]:
                    break

            _max = max(_max, score * curr)
    print(_max)
```

Cualquiera de los cuatro fors, se podría reemplazar por una única linea empleando
la función `takewhile` del itertools, como por ejemplo:

```python3
curr = 0
for a in range(i+1, len(data[i])):
    curr += 1
    if data[a][j] >= data[i][j]:
        break
```

Es equivalente a:

```python3
curr = len(list(takewhile(lambda x: data[x][j] < data[i][j], range(i+1, len(data[i]))))) + (i+1 < len(data[i]))
```

