# Advent of Code 2021
# Author: Frederik Wilmotte
# --- Day 2: Dive! ---

# ------------------
# --- Read input ---
# ------------------
def read_file(filename):
    return open(filename, "r")


# --------------------------
# --- Create record list ---
# --------------------------
def create_record_list(filename):
    record_list = []
    for row in read_file(filename):
        record_list.append(row)
    return record_list


# ------------------------------
# --- Split Dive instruction ---
# ------------------------------
def split_dive_instruction(dive_instruction):
    dive_instruction_split = dive_instruction.split()
    return dive_instruction_split[0], int(dive_instruction_split[1])


# ------------
# --- Dive ---
# ------------
def dive(filename, complexity):

    horizontal_position = 0
    depth = 0
    aim = 0

    dive_instructions = create_record_list(filename)

    for dive_instruction in dive_instructions:
        command, argument = split_dive_instruction(dive_instruction)
        if command == "forward":
            horizontal_position += argument
            if complexity == "complex":
                depth += aim * argument
        if command == "down":
            if complexity == "complex":
                aim += argument
            else:
                depth += argument
        if command == "up":
            if complexity == "complex":
                aim -= argument
            else:
                depth -= argument

    return horizontal_position * depth


print("Part 1: ", dive("diveInstructions_input", "simple"))
print("Part 2: ", dive("diveInstructions_input", "complex"))
