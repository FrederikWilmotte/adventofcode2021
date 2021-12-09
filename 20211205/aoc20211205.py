# Advent of Code 2021
# Author: Frederik Wilmotte
# --- Day 5: Hydrothermal Venture ---

import numpy as np


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


# ---------------------------------
# --- Create coordinates matrix ---
# ---------------------------------
def create_coordinates_matrix(coordinates_list):
    floor_dimension = 0
    matrix_count = len(coordinates_list)
    matrix_nr = 0
    coordinates_matrix = np.empty((matrix_count, 2, 2)).astype(int)
    for coordinates in coordinates_list:
        row = 0
        line_segment = coordinates.split(' -> ')
        for pair in line_segment:
            column = 0
            coordinate = pair.split(',')
            for element in coordinate:
                coordinates_matrix[matrix_nr, row, column] = int(element)
                if int(element) > floor_dimension:
                    floor_dimension = int(element)
                column += 1
            row += 1
        matrix_nr += 1

    floor_dimension += 1

    return coordinates_matrix, floor_dimension


# -----------------------
# --- Draw Horizontal ---
# -----------------------
def draw_horizontal(floor, row, first, last):
    if first > last:
        temp = first
        first = last
        last = temp
    for x in range(first, last+1):
        floor[row, x] += 1

    return floor


# ---------------------
# --- Draw Vertical ---
# ---------------------
def draw_vertical(floor, column, first, last):
    if first > last:
        temp = first
        first = last
        last = temp
    for x in range(first, last+1):
        floor[x, column] += 1

    return floor


# ---------------------
# --- Draw Diagonal ---
# ---------------------
def draw_diagonal(floor, coordinates):
    if coordinates[0, 0] < coordinates[1, 0]:
        x1 = coordinates[0, 0]
        y1 = coordinates[0, 1]
        x2 = coordinates[1, 0]
        y2 = coordinates[1, 1]
    else:
        x1 = coordinates[1, 0]
        y1 = coordinates[1, 1]
        x2 = coordinates[0, 0]
        y2 = coordinates[0, 1]

    row = y1

    for column in range(x1, x2+1):
        floor[row, column] += 1
        if y2 > y1:
            row += 1
        else:
            row -= 1

    return floor


# -----------------
# --- Map Floor ---
# -----------------
def map_floor(coordinates_matrix, floor, diagonal):
    for coordinates in coordinates_matrix:
        if coordinates[0, 1] == coordinates[1, 1]:
            # Draw Horizontal
            floor = draw_horizontal(floor, coordinates[0, 1], coordinates[0, 0], coordinates[1, 0])
        else:
            if coordinates[0, 0] == coordinates[1, 0]:
                # Draw Vertical
                floor = draw_vertical(floor, coordinates[0, 0], coordinates[0, 1], coordinates[1, 1])
            else:
                if diagonal:
                    # Draw Diagonal
                    floor = draw_diagonal(floor, coordinates)
    return floor


# ----------------------------
# --- Count Overlap points ---
# ----------------------------
def count_overlap_points(floor):
    overlap_points = 0
    for rows in floor:
        for columns in rows:
            if columns > 1:
                overlap_points += 1
    return overlap_points


# --------------------------------
# --- Calculate overlap points ---
# --------------------------------
def calculate_overlap_points(filename, diagonal):
    coordinates_list = create_record_list(filename)
    coordinates_matrix, floor_dimension = create_coordinates_matrix(coordinates_list)
    floor = np.zeros((floor_dimension, floor_dimension)).astype(int)
    floor = map_floor(coordinates_matrix, floor, diagonal)
    overlap_points = count_overlap_points(floor)
    print(floor)

    return overlap_points


print("Part 1: ", calculate_overlap_points("test_input", False))
print("Part 2: ", calculate_overlap_points("vent_lines_input", True))
