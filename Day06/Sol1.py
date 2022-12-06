
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

