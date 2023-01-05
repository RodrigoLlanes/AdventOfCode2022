from collections import defaultdict


def load_input():
    grid = defaultdict(dict)
    x_bounds, y_bounds = defaultdict(lambda: [10e5, -1]), defaultdict(lambda: [10e5, -1])
    data, password = open('input', 'r').read().rstrip().split('\n\n')
    for y, line in enumerate(data.split('\n')):
        for x, char in enumerate(line):
            if char != ' ':
                x_bounds[y][0] = min(x_bounds[y][0], x)
                x_bounds[y][1] = max(x_bounds[y][1], x)
                y_bounds[x][0] = min(y_bounds[x][0], y)
                y_bounds[x][1] = max(y_bounds[x][1], y)
                grid[x, y] = char

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
    return grid, password, x_bounds, y_bounds

def get_inc(facing):
    if facing == 0:
        return [1, 0]
    elif facing == 1:
        return [0, 1]
    elif facing == 2:
        return [-1, 0]
    elif facing == 3:
        return [0, -1]

def get_wrapping(facing, x, y, x_bounds, y_bounds):
    if facing == 0:
        return x_bounds[y][0], y
    if facing == 1:
        return x, y_bounds[x][0]
    if facing == 2:
        return x_bounds[y][1], y
    return x, y_bounds[x][1]


def main() -> None:
    grid, password, x_bounds, y_bounds = load_input()
    x, y = x_bounds[0][0], 0
    facing = 0

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
            if (nx, ny) not in grid:
                nx, ny = get_wrapping(facing, x, y, x_bounds, y_bounds)
            if grid[nx, ny] == '#':
                break
            x, y = nx, ny
    print((y+1)*1000 + (x+1)*4 + facing)


if __name__ == '__main__':
    main()

