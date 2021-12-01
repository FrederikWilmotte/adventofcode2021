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


# --------------
# --- Part 1 ---
# --------------
def sonar_sweep_pt1(filename):

    sea_depth_array = create_array(filename)

    depth_increase = 0
    while len(sea_depth_array) > 1:
        if sea_depth_array[1] > sea_depth_array[0]:
            depth_increase += 1
        sea_depth_array.pop(0)

    return depth_increase


# --------------
# --- Part 2 ---
# --------------
def sonar_sweep_pt2(filename):

    sea_depth_array = create_array(filename)

    depth_increase = 0
    while len(sea_depth_array) > 3:
        if sum(sea_depth_array[1:4]) > sum(sea_depth_array[0:3]):
            depth_increase += 1
        sea_depth_array.pop(0)

    return depth_increase


print(sonar_sweep_pt1("sonarSweepReport_input"))

print(sonar_sweep_pt2("sonarSweepReport_input"))
