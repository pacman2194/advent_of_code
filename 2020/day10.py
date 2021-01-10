#!/usr/bin/env python3


def get_data():
    """
    return a list of adapter jolt ratings
    """
    adapters = []
    with open('day10.txt', 'r') as data_file:
        adapters = [int(line.strip()) for line in data_file.readlines()]
        adapters.append(0)
    return adapters


def get_example_data():
    """
    return an example list of adapter jolt ratings
    """
    return [0, 28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
                    38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]


def get_differences(adapters):
    """
    return a tuple containing the count of adapter jolt rating differences
    """
    # start three at 1 since your device is guaranteed a difference of 3
    one, two, three = 0, 0, 0
    for i in range(len(adapters) - 1):
        diff = adapters[i+1] - adapters[i]
        if diff == 1:
            one += 1
        elif diff == 2:
            two += 1
        elif diff == 3:
            three += 1
        else:
            print(f'ERROR: difference of {diff}')
    return (one, two, three)


def get_solutions(adapters):
    """
    """
    solutions = 1
    for i in range(len(adapters)):
        print(f'checking adapters[{i}] ({adapters[i]})')
        paths = 1
        for j in range(2,4):
            if i + j >= len(adapters):
                break
            if adapters[i+j] - adapters[i] > 3:
                break
            paths += 1
        print(f'solutions: {solutions}  paths: {paths}')
        solutions *= paths
    return solutions
# (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (1), 1, 3, 2, 1, 1,  2,  1,  1,  1,  1,  1, ( 1)

def main():
    # Part 1
    adapters = get_example_data()
    # adapters = get_data()
    adapters.append(max(adapters)+3)
    adapters.sort()
    print(adapters)
    one, two, three = get_differences(adapters)
    print(f'{one}, {two}, {three}')
    print(f'{one * three}')
    solutions = get_solutions(adapters)
    print(f'solutions: {solutions}')


if __name__ == "__main__":
    main()
