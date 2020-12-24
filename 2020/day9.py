#!/usr/bin/env python3


def get_next_datum(data_file):
    """
    read next line and return the integer or False if end of file
    """
    datum = data_file.readline()
    if datum == '':
        return False
    return int(datum.strip())


def get_preamble(data_file, length):
    """
    return the preamble list
    """
    preamble = []
    for i in range(length):
        datum = get_next_datum(data_file)
        if datum == False:
            return False
        preamble.append(datum)
    return preamble


def validate(preamble, datum):
    """
    validate the next datum
    """
    for i in range(len(preamble) - 1):
        for j in range(i+1, len(preamble)):
            if datum == preamble[i] + preamble[j]:
                return True
    return False


def find_weakness_list(data, invalid):
    """
    find the contiguous list of numbers that sum up to the invalid datum
    """
    for i in range(len(data) - 1):
        for j in range(i+1, len(data)):
            summation = sum(data[i:j+1])
            if summation == invalid:
                return data[i:j+1]


def main():
    # Part 1
    with open('day9.txt', 'r') as data_file:
        preamble = get_preamble(data_file, 25)
        data = preamble[:]
        invalid = False
        while True:
            datum = get_next_datum(data_file)
            if not datum:
                break
            if not validate(preamble, datum):
                print(f'datum {datum} is not valid')
                invalid = datum
                break
            else:
                preamble = preamble[1:]
                preamble.append(datum)
                data.append(datum)

        # Part 2
        weakness_list = find_weakness_list(data, invalid)
        weakness = min(weakness_list) + max(weakness_list)
        print(f'weakness list: {weakness_list}')
        print(f'weakness min: {min(weakness_list)}')
        print(f'weakness max: {max(weakness_list)}')
        print(f'weakness: {weakness}')

if __name__ == "__main__":
    main()
