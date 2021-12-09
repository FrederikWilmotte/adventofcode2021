# Advent of Code 2021
# Author: Frederik Wilmotte
# --- Day 6: Lanternfish ---


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


# ----------------------------
# --- Simulate Lanternfish ---
# ----------------------------
def simulate_lanternfish(lanternfish_ages, days):
    ages = [lanternfish_ages.count(0), lanternfish_ages.count(1), lanternfish_ages.count(2), lanternfish_ages.count(3),
            lanternfish_ages.count(4), lanternfish_ages.count(5), lanternfish_ages.count(6), lanternfish_ages.count(7),
            lanternfish_ages.count(8)]
    for day in range(days):
        new_ages = ages.copy()
        for age in range(8, -1, -1):
            if age > 0:
                new_ages[age-1] = ages[age]
            else:
                new_ages[8] = ages[0]
                new_ages[6] = new_ages[6] + ages[0]
        ages = new_ages.copy()
    lanternfish_count = sum(ages)

    return lanternfish_count


# -------------------------
# --- Count Lanternfish ---
# -------------------------
def count_lanternfish(filename, days):
    lanternfish_ages = list(map(int, create_record_list(filename)[0].split(',')))
    lanternfish_count = simulate_lanternfish(lanternfish_ages, days)

    return lanternfish_count


print("Part 1: ", count_lanternfish("lanternfish_input", 80))
print("Part 2: ", count_lanternfish("lanternfish_input", 256))
