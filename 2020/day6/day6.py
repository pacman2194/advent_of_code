#!/usr/bin/env python3

def process_txt(txt):
    txt = txt.strip().split('\n\n')
    return [ line.strip().split('\n') for line in txt ]

def anybody(group):
    group = ''.join(group)
    return set(group)

def everybody(group):
    everybody_declared = 0
    group_str = ''.join(group)
    answers = set(group_str)
    for answer in answers:
        if group_str.count(answer) == len(group):
            everybody_declared += 1
    return everybody_declared

anybody_declarations = 0
every_declarations = 0

with open('day6.txt', 'r') as data_file:
    data = data_file.read()
    data = process_txt(data)
    for group in data:
        # Process questions to which anybody answered yes
        group_anybody = anybody(group)
        anybody_declarations += len(group_anybody)

        # Process questions to which everybody answered yes
        every_declarations += everybody(group)

example = """abc

a
b
c

ab
ac

a
a
a
a

b
"""

# data = process_txt(example)
# for group in data:
#     # Process questions to which anybody answered yes
#     group_anybody = anybody(group)
#     anybody_declarations += len(group_anybody)

#     # Process questions to which everybody answered yes
#     every_declarations += everybody(group)

print(f'anybody: {anybody_declarations}')
print(f'everybody: {every_declarations}')
