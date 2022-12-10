
# [Día 10](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
|  10 | 02:14:50 |13828 |     0 | 02:30:53 |11906 |     0 |

## [Parte 1](./Sol1.py)

Como se puede observar, parece que este año mi mayor reto no son los problemas, 
sino conseguir que me suene el despertador. Quejas aparte, pasemos a ver la solución.

El reto de hoy es simple, aunque puede resultar un poco confuso el orden de las
operaciones, primero se calcula la fuerza de la señal y luego se actualiza el valor de x.

```python3
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip().split()
        if len(line) == 2:
            line[1] = int(line[1])
        inp.append(line)
    return inp


def main() -> None:
    data = load_input()
    
    res = 0

    cycle = 0
    x = 1
    for line in data:
        cycle += 1
        if (cycle - 20) % 40 == 0:
            res += cycle * x
        if len(line) == 2:
            cycle += 1
            if (cycle - 20) % 40 == 0:
                res += cycle * x
            x += line[1]
    print(res)


if __name__ == '__main__':
    main()
```

La carga de los datos no varía mucho de lo que ya estamos acostumbrados, dividimos
cada linea por los espacios y si el resultado tiene longitud dos, el segundo elemento
lo pasamos a int.

```python3
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip().split()
        if len(line) == 2:
            line[1] = int(line[1])
        inp.append(line)
    return inp
```

Inicializamos el contador de ciclos y `x`, por defecto incrementamos los ciclos
en uno y comprobamos si es hora de calcular la fuerza de la señal, pues todas
las instrucciones tienen como mínimo un "coste" de un ciclo.

En caso de que la linea tenga longitud 2, sumamos otro ciclo, volvemos a hacer las
comprobaciones pertinentes y por último incrementamos `x`.

```python3
def main() -> None:
    data = load_input()
    
    res = 0

    cycle = 0
    x = 1
    for line in data:
        cycle += 1
        if (cycle - 20) % 40 == 0:
            res += cycle * x
        if len(line) == 2:
            cycle += 1
            if (cycle - 20) % 40 == 0:
                res += cycle * x
            x += line[1]
    print(res)
```

## [Parte 2](./Sol2.py)

Esta segunda parte no varía mucho, solo hay que sustituir el calculo de la fuerza
de la señal, por el dibujo en pantalla.

```python3
def load_input() -> list:
    inp = []
    for line in open('input', 'r').readlines():
        line = line.strip().split()
        if len(line) == 2:
            line[1] = int(line[1])
        inp.append(line)
    return inp


def main() -> None:
    data = load_input()
    
    screen = [['.']*40 for _ in range(6)]

    cycle = -1
    x = 1
    for line in data:
        cycle += 1
        if abs(cycle % 40 - x) < 2:
            screen[cycle // 40][cycle % 40] = '#'
        if len(line) == 2:
            cycle += 1
            if abs((cycle % 40) - x) < 2:
                screen[cycle // 40][cycle % 40] = '#'
            x += line[1]
    for line in screen:
        print(''.join(line))


if __name__ == '__main__':
    main()
```

Inicializamos la pantalla en blanco, y en cada "actualización de pantalla", comprobamos
si el pixel actual hay que dibujarlo (`abs(cycle % 40 - x) < 2`) y en caso afirmativo,
lo sustuimos por el símbolo `#`.

```python3
def main() -> None:
    data = load_input()
    
    screen = [['.']*40 for _ in range(6)]

    cycle = -1
    x = 1
    for line in data:
        cycle += 1
        if abs(cycle % 40 - x) < 2:
            screen[cycle // 40][cycle % 40] = '#'
        if len(line) == 2:
            cycle += 1
            if abs((cycle % 40) - x) < 2:
                screen[cycle // 40][cycle % 40] = '#'
            x += line[1]
    for line in screen:
        print(''.join(line))
```

