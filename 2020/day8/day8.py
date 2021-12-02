#!/usr/bin/env python3
import re

# Compile regular expression used to parse instructions
instruction_pattern = re.compile(r'(nop|acc|jmp) ([\+-][\d]+)')

# Set global variables
acc = 0
ptr = 0
executed = set([])
instructions_length = 0


def get_data():
    """
    return a list of instruction lines
    """
    global instructions_length
    instructions = []
    with open('day8.txt', 'r') as data_file:
        instructions = [line.strip() for line in data_file.readlines()]
    instructions_length = len(instructions)
    return instructions


def get_example_data():
    """
    return an example list of instruction lines
    """
    global instructions_length
    instructions = ["nop +0",
                    "acc +1",
                    "jmp +4",
                    "acc +3",
                    "jmp -3",
                    "acc -99",
                    "acc +1",
                    "jmp -4",
                    "acc +6"]
    instructions_length = len(instructions)
    return instructions


def parse_instruction(instruction):
    """
    parse an instruction string into a tuple containing 
    the command and the value
    """
    instruction_match = instruction_pattern.match(instruction)
    if instruction_match == None:
        print("ERROR: Failed to parse instruction")
        return None
    return (instruction_match.group(1), int(instruction_match.group(2)))


def execute_instruction(instruction):
    """
    execute the logic for the given parsed instruction tuple
    """
    # This function needs to operate on global variables
    global acc
    global ptr
    global executed

    # Check if current pointer position has already been executed
    if ptr in executed or ptr >= instructions_length:
        return False

    # Add current pointer position to the executed set
    executed.add(ptr)

    # Execute the instruction
    if instruction[0] == 'nop':
        # nop, move pointer, advance ptr
        ptr += 1
        return True
    elif instruction[0] == 'acc':
        # acc, modify global acc variable, advance ptr
        acc += instruction[1]
        ptr += 1
        return True
    elif instruction[0] == 'jmp':
        # jmp, modify global ptr variable
        ptr += instruction[1]
        return True
    else:
        print(f'ERROR: Unknown instruction {instruction}')
        return False


def event_loop(instructions):
    """
    perform the main event loop
    """
    global ptr
    global acc
    global executed

    # Reset global variables
    ptr = 0
    acc = 0
    executed = set([])

    # Set normal exit code and enter main loop
    exit_code = 0
    while True:
        if ptr >= instructions_length:
            # End of program reached. Exit normally
            break

        # Parse instruction and execute it
        instruction = parse_instruction(instructions[ptr])
        if not(execute_instruction(instruction)):
            print('Infinite loop detected. Program terminated.')
            exit_code = 1
            break

    # Final results reporting
    print(f'Final ptr position: {ptr}')
    print(f'Final value of acc: {acc}')
    return exit_code


def self_heal(instructions):
    # Brute force attempt to heal the code
    eval_instruction = 0
    healed = False

    # Loop over instructions flipping nop and jmp instructions
    # until a successful result or all instructions have been tested
    while (not healed) and eval_instruction < instructions_length:
        modded_instructions = flip_instruction(instructions, eval_instruction)
        if modded_instructions:
            # Instructions were modified, test
            if event_loop(modded_instructions) == 0:
                healed = True
            else:
                # Test failed important to flip the instruction back
                flip_instruction(instructions, eval_instruction)
                eval_instruction += 1
        else:
            eval_instruction += 1

    # Program never healed and all options were exhausted
    # Report and exit with generic failure code 1
    if not healed:
        print('WARNING: Program never healed')
        return 1

    # Self-heal successful, report and exit with success code 0
    else:
        print(f'INFO: Program successfully healed by flipping instruction at instruction array index {eval_instruction}')
        # print(instructions)
        return 0


def flip_instruction(instructions, pos):
    """
    return the instructions with a single nop or jmp converted to the other
    """
    # Check if nop, if value is zero just skip jmp +-0 creates infinite loop
    if 'nop' in instructions[pos] and (instructions[pos] != 'nop +0' or instructions[pos] != 'nop -0'):
        instructions[pos] = instructions[pos].replace('nop', 'jmp')
        return instructions
    # If jmp simply flip to nop
    elif 'jmp' in instructions[pos]:
        instructions[pos] = instructions[pos].replace('jmp', 'nop')
        return instructions
    # Else return False to indicate this test should be skipped
    else:
        return False


def test():
    # Part 1
    instructions = get_example_data()
    event_loop(instructions)
    # Part 2
    self_heal(instructions)


def main():
    # Part 1
    instructions = get_data()
    event_loop(instructions)
    # Part 2
    self_heal(instructions)


# test()
main()
