
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

