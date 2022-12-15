
# [Día 13](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
|  13 | 00:17:57 |  771 |     0 | 00:31:49 | 1304 |     0 |

## [Parte 1](./Sol1.py)

El problema de hoy no tiene mayor complicación, solo debemos definir una función
recursiva `check`, que comprueba si dos "paquetes" están ordenados o no.

```python3
def load_input() -> list:
    inp = [[]]
    for line in open('input', 'r').readlines():
        line = line.strip()
        if len(line) == 0:
            inp.append([])
        else:
            inp[-1].append(eval(line))
    return inp


def check(left, right):
    if isinstance(left, list):
        if not isinstance(right, list):
            return check(left, [right])
        for item0, item1 in zip(left, right):
            r = check(item0, item1)
            if r == 0:
                continue
            return r
        return len(right) - len(left)
    elif isinstance(right, list):
        return check([left], right)
    else:
        if left < right:
            return 1
        elif left == right:
            return 0
        return -1


def main() -> None:
    data = load_input()
    
    res = 0
    for index, (left, right) in enumerate(data):
        if check(left, right) > 0:
            res += index+1
    print(res)


if __name__ == '__main__':
    main()
```

Para la carga de datos empleo `eval` para parsear las listas, sería mejor emplear
`json.load`, pero en el momento era más rápido de escribir.

```python3
def load_input() -> list:
    inp = [[]]
    for line in open('input', 'r').readlines():
        line = line.strip()
        if len(line) == 0:
            inp.append([])
        else:
            inp[-1].append(eval(line))
    return inp
```

La función check, comprueba de manera recursiva, los criterios del enunciado del 
problema, devolviendo -1 si están mal ordenadas, 0 si son iguales y 1 si están 
bien ordenadas.

Empleamos esta función para contar el número de paquetes que están bien ordenados.

```python3
def check(left, right):
    if isinstance(left, list):
        if not isinstance(right, list):
            return check(left, [right])
        for item0, item1 in zip(left, right):
            r = check(item0, item1)
            if r == 0:
                continue
            return r
        return len(right) - len(left)
    elif isinstance(right, list):
        return check([left], right)
    else:
        if left < right:
            return 1
        elif left == right:
            return 0
        return -1


def main() -> None:
    data = load_input()
    
    res = 0
    for index, (left, right) in enumerate(data):
        if check(left, right) > 0:
            res += index+1
    print(res)
```

## [Parte 2](./Sol2.py)

Para esta segunda parte, cargamos todos los paquetes en la misma lista, añadiendo
los dos nuevos paquetes `[[2]]` y `[[6]]`. Despues empleamos la función `cmp_to_key`
para convertir `check` en una función key, para organizar la lista y posteriormente 
obtener los indices de los dos nuevos paquetes.

```python3
from functools import cmp_to_key


def load_input() -> list:
    inp = [[[2]], [[6]]]
    for line in open('input', 'r').readlines():
        line = line.strip()
        if len(line) == 0:
            continue
        else:
            inp.append(eval(line))
    return inp


def check(left, right):
    if isinstance(left, list):
        if not isinstance(right, list):
            return check(left, [right])
        for item0, item1 in zip(left, right):
            r = check(item0, item1)
            if r == 0:
                continue
            return r
        v = len(right) - len(left)
        return (v) / abs(v) if v != 0 else 0
    elif isinstance(right, list):
        return check([left], right)
    else:
        if left < right:
            return 1
        elif left == right:
            return 0
        return -1


def main() -> None:
    data = load_input() 
    data.sort(key=cmp_to_key(check), reverse=True)
    print((data.index([[2]])+1) * (data.index([[6]])+1))



if __name__ == '__main__':
    main()
```

