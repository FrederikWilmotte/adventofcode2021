# Advent of Code 2021
# Author: Frederik Wilmotte
# --- Day 7: The Treachery of Whales ---



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


# -------------------
# --- Fuel Amount ---
# -------------------
def fuel_amount(crab_positions, position):
    total_fuel = 0
    for crab_position in crab_positions:
        fuel = abs(crab_position-position)
        total_fuel += fuel
    return total_fuel


# ---------------------------
# --- Fuel Amount Complex ---
# ---------------------------
def fuel_amount_complex(crab_positions, position):
    total_fuel = 0
    for crab_position in crab_positions:
       total_fuel += sum(range(1, abs(crab_position - position)+1))
    return total_fuel


# ---------------------------
# --- Search Optimal Fuel ---
# ---------------------------
def search_optimal_fuel(crab_positions, median, complex_amount):
    optimal_fuel_found = False
    up = 1
    down = 1
    if complex_amount:
        best_guess = crab_positions[median]
        lowest_fuel = 0
        while not optimal_fuel_found:
            lowest_fuel = fuel_amount_complex(crab_positions, best_guess)
            fuel_min = fuel_amount_complex(crab_positions, best_guess-1)
            fuel_plus = fuel_amount_complex(crab_positions, best_guess+1)
            if fuel_min > lowest_fuel < fuel_plus:
                optimal_fuel_found = True
            else:
                if fuel_min < lowest_fuel:
                    best_guess -= 1
                else:
                    best_guess += 1
    else:
        while not optimal_fuel_found:
            lowest_fuel = fuel_amount(crab_positions, crab_positions[median])
            if fuel_amount(crab_positions, crab_positions[median - down]) > lowest_fuel < fuel_amount(crab_positions, crab_positions[median+up]):
                optimal_fuel_found = True
                new_median = median
            if fuel_amount(crab_positions, crab_positions[median - down]) == lowest_fuel:
                down -= 1
                new_median = median
            if fuel_amount(crab_positions, crab_positions[median + up]) == lowest_fuel:
                up += 1
                new_median = median
            if fuel_amount(crab_positions, crab_positions[median - down]) < lowest_fuel:
                new_median = median-down
                up = 1
                down = 1
            if fuel_amount(crab_positions, crab_positions[median + up]) < lowest_fuel:
                new_median = median + up
                up = 1
                down = 1
            median = new_median

    return lowest_fuel


# ----------------------
# --- Calculate Fuel ---
# ----------------------
def calculate_fuel(filename, complex_amount):
    crab_positions = list(map(int, create_record_list(filename)[0].split(',')))
    crab_positions.sort()
    median = int(len(crab_positions)/2-1)
    fuel = search_optimal_fuel(crab_positions, median, complex_amount)
    return fuel


print("Part 1: ", calculate_fuel("test_input", False))
print("Part 2: ", calculate_fuel("crab_positions_input", True))
