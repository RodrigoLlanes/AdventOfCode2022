from collections import defaultdict
import re

N = 50

ADY = {
        1: {0:(2, 0), 1:(4, 1), 2:(6, 0), 3:(9, 0)},
        2: {0:(7, 2), 1:(4, 2), 2:(1, 2), 3:(9, 3)},
        4: {0:(2, 3), 1:(7, 1), 2:(6, 1), 3:(1, 3)},
        6: {0:(7, 0), 1:(9, 1), 2:(1, 0), 3:(4, 0)},
        7: {0:(2, 2), 1:(9, 2), 2:(6, 2), 3:(4, 3)},
        9: {0:(7, 3), 1:(2, 1), 2:(1, 1), 3:(6, 3)}
        }

def load_input():
    grid = defaultdict(dict)
    data, password = open('input', 'r').read().rstrip().split('\n\n')
    for y, line in enumerate(data.split('\n')):
        for x, char in enumerate(line):
            if char != ' ':
                index = (x // N) + (y // N) * 3
                grid[index][x%N, y%N] = char

    data = password
    password = [data[0]]
    for char in data[1:]:
        if char.isnumeric():
            if password[-1].isnumeric():
                password[-1] += char
            else:
                password.append(char)
        else:
            password.append(char)
    return grid, password

def get_inc(facing):
    if facing == 0:
        return [1, 0]
    elif facing == 1:
        return [0, 1]
    elif facing == 2:
        return [-1, 0]
    elif facing == 3:
        return [0, -1]

def get_wrapping(d, x, y, nd):
    if d==0:
        v = y
    elif d==1:
        v = x
    elif d==2:
        v = y
    elif d==3:
        v = x

    if nd==0:
        if d == 2:
            return 0, N-1-v
        return 0, v
    if nd==1:
        return v, 0
    if nd==2:
        if d == 0:
            return N-1, N-1-v
        return N-1, v
    if nd==3:
        return v, N-1
            

def score(face, x, y, index):
    if index == 1:
        return (y + 1) * 1000 + (N + x + 1) * 4 + face
    if index == 2:
        return (y + 1) * 1000 + (N*2 + x + 1) * 4 + face
    if index == 4:
        return (N + y + 1) * 1000 + (N + x + 1) * 4 + face
    if index == 6:
        return (N*2 + y + 1) * 1000 + (x + 1) * 4 + face
    if index == 7:
        return (N*2 + y + 1) * 1000 + (N + x + 1) * 4 + face
    if index == 9:
        return (N*3 + y + 1) * 1000 + (x + 1) * 4 + face


def main() -> None:
    grid, password = load_input()
    x, y = 0, 0
    facing = 0
    face = 1

    for movement in password:
        if movement.isalpha():
            if movement == 'R':
                facing += 1
            else:
                facing -= 1
            facing %= 4
            continue
        
        movement = int(movement)
        for _ in range(movement):
            dx, dy = get_inc(facing)
            nx, ny = x + dx, y + dy
            nfacing, nface = facing, face
            if (nx, ny) not in grid[face]:
                nface, nfacing = ADY[face][facing]
                nx, ny = get_wrapping(facing, x, y, nfacing)
            if grid[nface][nx, ny] == '#':
                break
            x, y = nx, ny
            facing, face = nfacing, nface
    print(score(facing, x, y, face))


if __name__ == '__main__':
    main()

