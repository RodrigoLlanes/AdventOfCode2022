
# [Día 5](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
|   5 | 00:21:22 | 3129 |     0 | 00:22:39 | 2427 |     0 |

## [Parte 1](./Sol1.py)

El reto de hoy es el típico problema de mover cajas, no es complicado, pero un
poco laborioso y una confusión tonta puede llevarte a errores, como nos ha pasado
a muchos hoy.

```python3
def load_input() -> tuple:
    crates = [[] for _ in range(9)]
    instructions = []
    inp = open('input', 'r').readlines()
 
    while True:
        line = inp.pop(0)
        if len(line.strip()) == 0:
            break
        for ind, i in enumerate(range(1, len(line), 4)):
            if line[i].isalpha():
                crates[ind].append(line[i])
    
    for line in inp:
        line = line.split()
        instructions.append((int(line[1]), int(line[3])-1, int(line[5])-1))
    
    return crates, instructions


def main() -> None:
    crates, instructions = load_input()
    for a, b, c in instructions:
        crate = crates[b][:a]
        crates[b] = crates[b][a:]
        crates[c] = list(reversed(crate)) + crates[c]

    for crate in crates:
        print(crate[0] if len(crate) else " ", end='')
    print() 


if __name__ == '__main__':
    main()
```

Para la carga de los datos, primero iteramos linea a linea, miramos en la
posición de las cajas y vamos añadiendolas a sus respectivas pilas.

Una vez encontrada una linea vacía, pasamos a la lectura de las instrucciones,
y vamos añadiendolas a la lista `instructions`.

```python3
def load_input() -> tuple:
    crates = [[] for _ in range(9)]
    instructions = []
    inp = open('input', 'r').readlines()
 
    while True:
        line = inp.pop(0)
        if len(line.strip()) == 0:
            break
        for ind, i in enumerate(range(1, len(line), 4)):
            if line[i].isalpha():
                crates[ind].append(line[i])
    
    for line in inp:
        line = line.split()
        instructions.append((int(line[1]), int(line[3])-1, int(line[5])-1))
    
    return crates, instructions
```

Siguiendo las instrucciones extraemos las cajas de su pila, invertimos su orden
para simular que se han cogido de una en una y las añadimos a su pila destino.

```python3
def main() -> None:
    crates, instructions = load_input()
    for a, b, c in instructions:
        crate = crates[b][:a]
        crates[b] = crates[b][a:]
        crates[c] = list(reversed(crate)) + crates[c]

    for crate in crates:
        print(crate[0] if len(crate) else " ", end='')
    print() 
```

## [Parte 2](./Sol2.py)

Para esta segunda parte no es necesario pararse a explicar nada, pues lo unico
que cambia es que he quitado la función `reversed` que invertía el orden de las
cajas transportadas, pues ahora se transportan todas juntas.

```python3
def load_input() -> tuple:
    crates = [[] for _ in range(9)]
    instructions = []
    inp = open('input', 'r').readlines()
    
    while True:
        line = inp.pop(0)
        if len(line.strip()) == 0:
            break
        for ind, i in enumerate(range(1, len(line), 4)):
            if line[i].isalpha():
                crates[ind].append(line[i])
    
    for line in inp:
        line = line.split()
        instructions.append((int(line[1]), int(line[3])-1, int(line[5])-1))
    
    return crates, instructions


def main() -> None:
    crates, instructions = load_input()
    for a, b, c in instructions:
        crate = crates[b][:a]
        crates[b] = crates[b][a:]
        crates[c] = list(crate) + crates[c]

    for crate in crates:
        print(crate[0] if len(crate) else " ", end='')
    print() 


if __name__ == '__main__':
    main()
```

