
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

