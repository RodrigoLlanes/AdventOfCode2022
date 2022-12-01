
# [Día 1](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
| 1   | 00:02:22 |  655 | 0     | 00:03:26 | 513  | 0     |

## [Parte 1](./Sol1.py)

Primer día, como siempre, de calentamiento. Para el problema de hoy tendremos
que sumar los elementos de cada sublista, para obtener el total de calorías que
carga cada elfo y a partir de esta lista calcular el máximo.

```python3
def load_input() -> list:
    inp = [0]
    for line in open('input', 'r').readlines():
        line = line.strip()
        if len(line) == 0:
            inp.append(0)
        else:
            inp[-1] += int(line)
    return inp


def main() -> None:
    data = load_input()
    print(max(data))


if __name__ == '__main__':
    main()
```

Para la carga de los datos simplemente iteramos en las lineas del fichero de 
entrada, si esta está vacía, añadimos un nuevo elemento a la lista de resultados, 
en caso contrario sumamos el valor de la nueva linea al último elemento de la lista.

```python3
inp = [0]
for line in open('input', 'r').readlines():
    line = line.strip()
    if len(line) == 0:
        inp.append(0)
    else:
        inp[-1] += int(line)
```

A partir de la lista de calorías totales que carga cada elfo (`data`) obtenida
anteriormente, calculamos el número máximo.

```python3
print(max(data))
```

## [Parte 2](./Sol2.py)

Para la segunda parte la carga de datos es identica a la del problema anterior,
solo que ahora necesitamos sumar las calorías de los tres elfos que más calorías
cargan.

Para ello ordenamos la lista y sumamos los 3 últimos (si estás ordenando la lista
de manera ascendente).


```python3
def load_input() -> list:
    inp = [0]
    for line in open('input', 'r').readlines():
        line = line.strip()
        if len(line) == 0:
            inp.append(0)
        else:
            inp[-1] += int(line)
    return inp


def main() -> None:
    data = load_input()
    print(sum(sorted(data)[-3:]))


if __name__ == '__main__':
    main()
```

Como hemos comentado anteriormente la carga de datos es identica a la de la
[Parte 1](#parte-1), así que nos centraremos en el cálculo de la solución.

Simplemente, ordenamos la lista de calorías, cogemos los tres últimos elementos
y los sumamos.

```python3
print(sum(sorted(data)[-3:]))
```

