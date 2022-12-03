
# [Día 2](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
| 2   | 02:36:29 |28447 |     0 | 02:39:15 | 25494|     0 |

## [Parte 1](./Sol1.py)

Segundo día, al igual que ayer, de calentamiento (aunque como se puede observar,
a alguien no le ha sonado el despertador). Para el problema de hoy tendremos que 
calcular el resultado de varias partidas a piedra papel o tijeras y sumarlas.

```python3
OPTIONS = ['A', 'B', 'C']


def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip().translate(str.maketrans({'X': 'A', 'Y': 'B', 'Z': 'C'}))
        inp.append(line.split())
    return inp


def get_score(act, resp):
    score = OPTIONS.index(resp) + 1
    p = (OPTIONS.index(act) - OPTIONS.index(resp)) % 3
    if p == 0:
        score += 3
    if p == 2:
        score += 6
    return score


def main() -> None:
    data = load_input()
    score = 0

    for (act, resp) in data:     
        score += get_score(act, resp)
    print(score)


if __name__ == '__main__':
    main()
```

Para la carga de los datos iteramos en cada linea del fichero, y sustituimos 
'X', 'Y' y 'Z' por 'A', 'B' y 'C', para calcular el resultado con mas facilidad.

```python3
OPTIONS = ['A', 'B', 'C']


def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip().translate(str.maketrans({'X': 'A', 'Y': 'B', 'Z': 'C'}))
        inp.append(line.split())
    return inp
```

Sumamos la puntuación de cada partida, siendo esta la puntuación del 'palo' 
elegido más la puntuación de la propia partida.

```python3
def get_score(act, resp):
    score = OPTIONS.index(resp) + 1
    p = (OPTIONS.index(act) - OPTIONS.index(resp)) % 3
    if p == 0:
        score += 3
    if p == 2:
        score += 6
    return score


def main() -> None:
    data = load_input()
    score = 0

    for (act, resp) in data:     
        score += get_score(act, resp)
    print(score)
```
## [Parte 2](./Sol2.py)

En esta segunda parte, nos darán el resultado de la partida en lugar de la
elección del jugador, por lo que tendremos que calcularla.

```python3
OPTIONS = ['A', 'B', 'C']


def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        inp.append(line.split())
    return inp


def get_score(act, resp):
    score = OPTIONS.index(resp) + 1
    p = (OPTIONS.index(act) - OPTIONS.index(resp)) % 3
    if p == 0:
        score += 3
    if p == 2:
        score += 6
    return score


def main() -> None:
    data = load_input()
    score = 0

    for (act, resp) in data:
        i = OPTIONS.index(act)
        if resp == 'X':
            resp = OPTIONS[i-1]
        elif resp == 'Y':
            resp = act
        else:
            resp = OPTIONS[(i+1)%3]
        score += get_score(act, resp)

    print(score)


if __name__ == '__main__':
    main()
```

La carga de los datos es la misma que en la parte anterior, pero evitando la 
traducción.

```python3
OPTIONS = ['A', 'B', 'C']


def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip()
        inp.append(line.split())
    return inp

```

La función `get_score` no cambia, solo lo hace el `main` para calcular la 'elección'
del jugador.

```python3
def main() -> None:
    data = load_input()
    score = 0

    for (act, resp) in data:
        i = OPTIONS.index(act)
        if resp == 'X':
            resp = OPTIONS[i-1]
        elif resp == 'Y':
            resp = act
        else:
            resp = OPTIONS[(i+1)%3]
        score += get_score(act, resp)

    print(score)
```

