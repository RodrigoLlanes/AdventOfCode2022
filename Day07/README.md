
# [Día 7](./)

| Day | Time     | Rank | Score | Time     | Rank | Score |
|-----|----------|------|-------|----------|------|-------|
|   7 | 00:25:49 | 1458 |     0 | 00:37:47 | 2002 |     0 |

## [Parte 1](./Sol1.py)

Empezamos ya con problemas ligeramente más complejos, en este tendremos que
montar un arbol de carpetas, para luego sumar el tamaño de todas las carpetas 
menores de 100000.

```python3
class Dir:
    def __init__(self, parent) -> None:
        self.parent: Dir = parent
        self.childs = {}
        self.files = {}

    def size(self):
        return sum(self.files.values()) + sum(child.size() for child in self.childs.values())

    def sol1(self):
        res = sum(child.sol1() for child in self.childs.values())
        if self.size() < 100000:
            return res + self.size()
        return res


def load_input() -> Dir:
    root = Dir(None)
    curdir = root
    for line in open('input', 'r').readlines()[1:]:
        line = line.strip().split()
        match line:
            case ['$', 'cd', '..']:
                curdir = curdir.parent
            case ['$', 'cd', directory]:
                if directory not in curdir.childs:
                    curdir.childs[directory] = Dir(curdir)
                curdir = curdir.childs[directory]
            case ['$', 'ls']:
                pass
            case ['dir', name]:
                if name not in curdir.childs:
                    curdir.childs[name] = Dir(curdir)
            case [size, name]:
                curdir.files[name] = int(size)
    return root


def main() -> None:
    root = load_input()
    print(root.sol1())


if __name__ == '__main__':
    main()
```

Para la carga de datos, definimos una clase `Dir` que define un directorio, tiene
un directorio padre, una serie de directorios hijos y contiene una serie de
ficheros con sus respectivos tamaños.

```python3
class Dir:
    def __init__(self, parent) -> None:
        self.parent: Dir = parent
        self.childs = {}
        self.files = {}

    ...
```

Haciendo uso de esta clase `Dir`, vamos construyendo el arbol de ficheros,
en función del comando ejecutado, cambiamos el directorio actual o añadimos ficheros
o subcarpetas a dicho directorio.

```python3
def load_input() -> Dir:
    root = Dir(None)
    curdir = root
    for line in open('input', 'r').readlines()[1:]:
        line = line.strip().split()
        match line:
            case ['$', 'cd', '..']:
                curdir = curdir.parent
            case ['$', 'cd', directory]:
                if directory not in curdir.childs:
                    curdir.childs[directory] = Dir(curdir)
                curdir = curdir.childs[directory]
            case ['$', 'ls']:
                pass
            case ['dir', name]:
                if name not in curdir.childs:
                    curdir.childs[name] = Dir(curdir)
            case [size, name]:
                curdir.files[name] = int(size)
    return root
```

Una vez montado todo el arbol, hacemos uso de la función `sol1` de la clase `Dir`
que de manera recursiva devuelve la suma de todas las carpetas cuyo tamaño es menor
a 100000.

```python3
class Dir:
    ...

    def size(self):
        return sum(self.files.values()) + sum(child.size() for child in self.childs.values())

    def sol1(self):
        res = sum(child.sol1() for child in self.childs.values())
        if self.size() < 100000:
            return res + self.size()
        return res
```

## [Parte 2](./Sol2.py)

Para la parte 2, tenemos que encontrar la carpeta cuyo peso se acerca más al
espacio necesario, pero sin quedarse corto.

```python3
class Dir:
    def __init__(self, parent) -> None:
        self.parent: Dir = parent
        self.childs = {}
        self.files = {}

    def size(self):
        return sum(self.files.values()) + sum(child.size() for child in self.childs.values())
  
    def sol2(self, n):
        if self.size() < n:
            return 30000000 * 100
        return min(self.size(), min(child.sol2(n) for child in self.childs.values()))


def load_input() -> Dir:
    root = Dir(None)
    curdir = root
    for line in open('input', 'r').readlines()[1:]:
        line = line.strip().split()
        match line:
            case ['$', 'cd', '..']:
                curdir = curdir.parent
            case ['$', 'cd', directory]:
                if directory not in curdir.childs:
                    curdir.childs[directory] = Dir(curdir)
                curdir = curdir.childs[directory]
            case ['$', 'ls']:
                pass
            case ['dir', name]:
                if name not in curdir.childs:
                    curdir.childs[name] = Dir(curdir)
            case [size, name]:
                curdir.files[name] = int(size)
    return root


def main() -> None:
    root = load_input()
    print(root.sol2(30000000 - (70000000 - root.size())))


if __name__ == '__main__':
    main()
```

Lo único que cambia con respecto a la parte 1 es la función sol2, que dado un tamaño
de memoria `n`, si la carpeta actual es más pequeña devuelve un número muy grande,
para que al calcular el mínimo, nunca sea escogido. En caso contrario, devuelve 
el mínimo entre su tamaño y la sol2 de todos sus hijos.

```python3
class Dir:
    ...

    def sol2(self, n):
        if self.size() < n:
            return 30000000 * 100
        return min(self.size(), min(child.sol2(n) for child in self.childs.values()))
```

