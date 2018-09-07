def main():
    print("Welcome to the game!")
    NUM_DISKS = int(input("Choose number of disks: "))
    tower_one = initial_tower(NUM_DISKS)
    tower_two = []
    tower_three = []
    towers = [tower_one, tower_two, tower_three]

    while (len(tower_three) < NUM_DISKS):
        print_tower(towers)
        from_tower = get_from_tower(towers)
        to_tower = get_to_tower()
        moved = move_tower(towers[from_tower - 1], towers[to_tower - 1])
        if not moved:
            print ('Sorry, this move is not possible.')

    print_tower(towers)
    print("T H E  E N D")


def initial_tower(num):
    tower_one = [0] * num
    for i in range(num):
        tower_one[i] = 2 * (num - i) - 1
    return tower_one


def move_tower(from_tower, to_tower):
    if len(from_tower) > 0:
        from_disk = from_tower[-1]
        if len(to_tower) > 0:
            to_disk = to_tower[-1]
        else:
            from_tower.pop()
            to_tower.append(from_disk)
            return True
        if from_disk < to_disk:
            from_tower.pop()
            to_tower.append(from_disk)
            return True
        return False
    return False


def get_from_tower(towers):
    from_tower = input("Select tower to move disk from(1/2/3): ")
    valid_input = (from_tower == '1' or from_tower == '2' or from_tower == '3') and len(towers[int(from_tower)-1]) > 0

    while not valid_input:
        print("Invalid input, please try again.")
        from_tower = input("Select tower to move disk from(1/2/3): ")
        valid_input = (from_tower == '1' or from_tower == '2' or from_tower == '3') and len(towers[int(from_tower)-1]) > 0
    else:
        return int(from_tower)


def get_to_tower():
    to_tower = input("Select tower to move disk to(1/2/3): ")
    while to_tower != '1' and to_tower != '2' and to_tower != '3':
        print("Invalid input, please try again.")
        to_tower = input("Select tower to move disk to(1/2/3): ")
    else:
        return int(to_tower)


def print_tower(towers):
    num_disks = 0
    for tower in towers:
        num_disks += len(tower)
    SPACE = 24
    print_tower_name(SPACE)
    for level in range(num_disks + 1, 0, -1):
        print_one_level(SPACE, towers, level)


def print_tower_name(SPACE):
    tower_name = ['1', '2', '3']
    for name in tower_name:
        print(' ' * SPACE, end = '')
        print(name, end ='')
    print()


def print_one_level(SPACE, towers, level):
    ''' level counts from 1 at bottom, max_level = NUM_DISKS + 1
    '''
    spaces = space(towers, level)
    for i in range(3):
        print(' ' * (SPACE - spaces[i]), end='')
        print_disk_or_tower(towers[i], level)
    print()


def print_disk_or_tower(tower, level):
    if level > len(tower):
        print('|', end='')
    else:
        print('=' * tower[level - 1], end='')


def space(towers, level):
    space = [0] * 3
    for i in range(3):
        if level > len(towers[i]):
            if i == 0:
                continue
            elif i ==1:
                space[i] = space[i - 1]
            else:
                if level > len(towers[i - 1]):
                    continue
                else:
                    space[i] = towers[i - 1][level - 1] // 2
        else:
            if i == 0:
                space[i] = towers[i][level - 1] // 2
            elif i ==1:
                space[i] = space[i - 1] + towers[i][level - 1] // 2
            else:
                if level > len(towers[i - 1]):
                    space[i] = towers[i][level - 1] // 2
                else:
                    space[i] = towers[i - 1][level - 1] // 2 + towers[i][level - 1] // 2
    return space


if __name__ == '__main__':
    main()
