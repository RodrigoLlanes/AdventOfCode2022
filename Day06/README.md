
# [Día ](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
|   6 | 02:37:00 | 30472|     0 | 02:38:09 | 29427|     0 |

## [Parte 1](./Sol1.py)

El reto de hoy ha sido ridíulamente facil (y como podeis observar, alguien ha 
vuelto a quedarse dormido), simplemente hay que buscar en un string las primeras
cuatro letras distintas.

```python3
def load_input() -> str:
    return open('input', 'r').readlines()[0]


def main() -> None:
    data = load_input()
    for i in range(3, len(data)):
        if len(set(data[i-3:i+1])) == 4:
            print(i+1)
            return


if __name__ == '__main__':
    main()
```

Para la carga de los dato, simplemente leemos la primera linea del fichero.

```python3
def load_input() -> str:
    return open('input', 'r').readlines()[0]
```

Y para resolverlo, iteramos desde el cuarto elemento en adelante, comprobando si
el y los 3 anteriores son distintos entre ellos, en caso positivo devolvemos el
resultado paramos.

```python3
def main() -> None:
    data = load_input()
    for i in range(3, len(data)):
        if len(set(data[i-3:i+1])) == 4:
            print(i+1)
            return
```

## [Parte 2](./Sol2.py)

Para la segunda parte no voy ni a molestarme en explicar nada, es simplemente
comprobar 14 en lugar de solo 4.

```python3
def load_input() -> str:
    return open('input', 'r').readlines()[0]


def main() -> None:
    data = load_input()
    for i in range(13, len(data)):
        if len(set(data[i-13:i+1])) == 14:
            print(i+1)
            return


if __name__ == '__main__':
    main()
```

