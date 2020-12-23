#!/usr/bin/env python3
import re

line_pattern = re.compile(r'([\w\s]+) bags contain ([^.]+).')
content_pattern = re.compile(r'([\d]+) ([\w\s]+) bags?')

def process_line(line):
    line_match = line_pattern.match(line)
    if line_match == None:
        print(f'ERROR: NO MATCH FOR {line}')
        return None
    key = line_match.group(1).strip()
    contents = line_match.groups()[1:]
    contents = [ content.strip() for content in contents[0].split(',') ]
    line_contents = []
    line_contents.append(key)
    for content in contents:
        content_match = content_pattern.match(content)
        if content_match == None:
            return (key, ())
        line_contents.append((content_match.group(1), content_match.group(2)))
    return (line_contents[0], tuple(line_contents[1:]))

def process_line_data_contents(line_data_contents):
    line_data = {}
    for content in line_data_contents:
        line_data[content[1].strip()] = int(content[0])
    return line_data

def get_data():
    bag_collection = {}
    with open('day7.txt', 'r') as data_file:
        for line in data_file.readlines():
            line = line.strip()
            line_data = process_line(line)
            bag_collection[line_data[0]] = process_line_data_contents(line_data[1])
    return bag_collection

def get_example_data():
    bag_collection = {}
#     example = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# """
    example = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""
    for line in example.splitlines(keepends=False):
        line = line.strip()
        line_data = process_line(line)
        bag_collection[line_data[0]] = process_line_data_contents(line_data[1])
    return bag_collection

def shiny_gold_bag_count(bag_collection, bag_name):
    count = 0
    bag = bag_collection[bag_name]

    if len(bag) == 0:
        return count
    else:
        for sub_bag in bag.keys():
            if sub_bag == "shiny gold":
                count += 1
            count += shiny_gold_bag_count(bag_collection, sub_bag)

    return count

def bags_containing_at_least_one_shiny_gold_bag(bag_collection):
    count = 0
    
    for bag_name in bag_collection.keys():
        if shiny_gold_bag_count(bag_collection, bag_name) > 0:
            # print(f"{bag_name} bags contain at least one shiny gold bag!")
            count += 1

    return count

def bag_count(bag_collection, bag_name):
    count = 0
    top_level_bag = bag_collection[bag_name]
    print(f"Currently counting bags inside {bag_name}.")
    
    if len(top_level_bag) == 0:
        return count
    else:
        for current_bag in top_level_bag.keys():
            # Add the number of bags of the current type
            # to the count.
            current_bag_type_count = top_level_bag[current_bag]
            count += current_bag_type_count
            # Count the bags inside each bag of the current type,
            # multiply it by the number of the current type,
            # then add it to the count.
            bags_inside_current_bag_type_count = bag_count(bag_collection, current_bag)
            count += bags_inside_current_bag_type_count * current_bag_type_count
        
    return count

bag_collection = get_data()
# bag_collection = get_example_data()

# print(bag_collection)
print(bags_containing_at_least_one_shiny_gold_bag(bag_collection))
print(bag_count(bag_collection, 'shiny gold'))
