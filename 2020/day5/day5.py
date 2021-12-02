#!/usr/bin/env python3

def str_to_int(s):
    return int(s.replace('F', '0')
                .replace('B', '1')
                .replace('L', '0')
                .replace('R', '1')
                ,2)

def calculate_seat_id(r,c):
    return r * 8 + c

max_seat_id = -1
seat_dict = {}

with open('day5.txt', 'r') as data_file:
    for line in data_file.readlines():
        line = line.strip()
        row = str_to_int(line[:7])
        column = str_to_int(line[7:])
        seat_id = calculate_seat_id(row, column)
        seat_dict[seat_id] = row, column
        if seat_id > max_seat_id:
            max_seat_id = seat_id
        # print(f'{row},{column},{seat_id}')

print(f'max seat id: {max_seat_id}')
seat_ids = list(seat_dict.keys())
seat_ids.sort()
for i in range(len(seat_ids)-2):
    if seat_ids[i+1] == (seat_ids[i]+2) and seat_ids[i+1] == (seat_ids[i+2]-1):
        print(f'your seat: {seat_ids[i]+1}')
