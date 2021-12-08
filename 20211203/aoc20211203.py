# Advent of Code 2021
# Author: Frederik Wilmotte
# --- Day 3: Binary Diagnostic ---

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
        row = row.rstrip("\n")
        record_list.append(row)
    return record_list


# ------------------
# --- Pivot list ---
# ------------------
def pivot_list(listname):
    listpivot = []
    for column in range(len(listname[0])):
        line = ""
        for row in range(len(listname)):
            line = line + listname[row][column]
        listpivot.append(line)
    return listpivot


# -----------------------------------
# --- Calculate power consumption ---
# -----------------------------------
def calculate_power_consumption(filename):
    binary_list = create_record_list(filename)
    pivot_binary_list = pivot_list(binary_list)

    gamma_rate = ""
    epsilon_rate = ""
    gamma_rate_dec = 0
    epsilon_rate_dec = 0

    for row in pivot_binary_list:
        if row.count("1") > row.count("0"):
            gamma_rate = gamma_rate + "1"
            epsilon_rate = epsilon_rate + "0"
        else:
            gamma_rate = gamma_rate + "0"
            epsilon_rate = epsilon_rate + "1"
        gamma_rate_dec = int(gamma_rate, 2)
        epsilon_rate_dec = int(epsilon_rate, 2)

    return gamma_rate_dec * epsilon_rate_dec


# -----------------------------------------------------
# --- Calculate Oxygen generator rating consumption ---
# -----------------------------------------------------
def calculate_oxygen_generator_rating(binary_list):
    old_binary_list = binary_list.copy()
    new_binary_list = []
    pivot_binary_list = []
    char = 0
    while len(old_binary_list) != 1:
        pivot_binary_list.clear()
        pivot_binary_list = pivot_list(old_binary_list)
        if pivot_binary_list[char].count("1") >= pivot_binary_list[char].count("0"):
            for i in range(len(old_binary_list)):
                if old_binary_list[i][char] == "1":
                    new_binary_list.append(old_binary_list[i])
        else:
            for i in range(len(old_binary_list)):
                if old_binary_list[i][char] == "0":
                    new_binary_list.append(old_binary_list[i])
        char += 1
        old_binary_list.clear()
        old_binary_list = new_binary_list.copy()
        new_binary_list.clear()

    oxygen_generator_rating = int(old_binary_list[0], 2)

    return oxygen_generator_rating


# -------------------------------------------------
# --- Calculate CO2 scrubber rating consumption ---
# -------------------------------------------------
def calculate_co2_scrubber_rating(binary_list):
    old_binary_list = binary_list.copy()
    new_binary_list = []
    pivot_binary_list = []
    char = 0
    while len(old_binary_list) != 1:
        pivot_binary_list.clear()
        pivot_binary_list = pivot_list(old_binary_list)
        if pivot_binary_list[char].count("0") <= pivot_binary_list[char].count("1"):
            for i in range(len(old_binary_list)):
                if old_binary_list[i][char] == "0":
                    new_binary_list.append(old_binary_list[i])
        else:
            for i in range(len(old_binary_list)):
                if old_binary_list[i][char] == "1":
                    new_binary_list.append(old_binary_list[i])
        char += 1
        old_binary_list.clear()
        old_binary_list = new_binary_list.copy()
        new_binary_list.clear()

    co2_scrubber_rating = int(old_binary_list[0], 2)

    return co2_scrubber_rating


# -----------------------------------
# --- Calculate power consumption ---
# -----------------------------------
def calculate_life_support_rating(filename):
    binary_list = create_record_list(filename)
    oxygen_generator_rating = calculate_oxygen_generator_rating(binary_list)
    co2_scrubber_rating = calculate_co2_scrubber_rating(binary_list)

    return oxygen_generator_rating * co2_scrubber_rating


print("Part 1: ", calculate_power_consumption("test_input"))
print("Part 2: ", calculate_life_support_rating("diagnosticReport_input"))
