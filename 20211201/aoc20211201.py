# Advent of Code 2021
# Author: Frederik Wilmotte
# --- Day 1: Sonar Sweep ---

# ------------------
# --- Read input ---
# ------------------
def read_file(filename):
    return open(filename, "r")


# --------------------
# --- Create array ---
# --------------------
def create_array(filename):
    array = []
    for element in read_file(filename):
        array.append(int(element))
    return array


# -------------------
# --- Sonar Sweep ---
# -------------------
def sonar_sweep(filename, sliding):

    sea_depth_array = create_array(filename)

    depth_increase = 0
    while len(sea_depth_array) > sliding:
        if sum(sea_depth_array[1:sliding+1]) > sum(sea_depth_array[0:sliding]):
            depth_increase += 1
        sea_depth_array.pop(0)

    return depth_increase


print("Part 1: ", sonar_sweep("sonarSweepReport_input", 1))
print("Part 2: ", sonar_sweep("sonarSweepReport_input", 3))
