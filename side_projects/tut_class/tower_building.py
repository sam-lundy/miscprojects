

# def tower_builder(n):
#     return [('*' * i).center(n * 2 - 1) for i in range(1, 2 * n + 1, 2)]

# print(tower_builder(2))


def tower_builder(n_floors):

    tower = []

    for i in range(1, n_floors + 1):
        blocks = '*' * (2 * i - 1)
        space = ' ' * (n_floors - i)
        tower.append(space + blocks + space)
    print(tower)

tower_builder(6)