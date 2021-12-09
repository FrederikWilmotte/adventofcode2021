# Advent of Code 2021
# Author: Frederik Wilmotte
# --- Day 4: Giant Squid ---

import numpy as np


# --------------------------
# --- Read Drawn Numbers ---
# --------------------------
def read_drawn_numbers(line):
    return list(map(int, line.split(',')))


# ------------------
# --- Read input ---
# ------------------
def read_bingo_input(filename):
    bingo_input = open(filename, "r").read().split("\n")
    matrix_nr = 0
    start_matrix = False
    bingo_list = []
    for line in bingo_input:
        if line == "":
            start_matrix = True
            matrix_nr += 1
        else:
            if start_matrix:
                number_list = line.split(" ")
                for number in number_list:
                    if number != "":
                        bingo_list.append(int(number))
            else:
                drawn_numbers = read_drawn_numbers(line)

    return bingo_list, matrix_nr, drawn_numbers


# -------------------------
# --- Make bingo boards ---
# -------------------------
def make_bingo_boards(bingo_list, matrix_nr):
    bingo_boards = np.empty((matrix_nr, 5, 5)).astype(int)
    score_boards = np.zeros((matrix_nr, 5, 5)).astype(int)
    i = 0
    for x in range(matrix_nr):
        for y in range(5):
            for z in range(5):
                bingo_boards[x, y, z] = bingo_list[i]
                i += 1
    return bingo_boards, score_boards


# --------------------------
# --- Check bingo boards ---
# --------------------------
def check_bingo_number(bingo_boards, score_boards, random_number):
    x = 0
    for matrix in bingo_boards:
        y = 0
        for row in matrix:
            z = 0
            for element in row:
                if element == random_number:
                    score_boards[x, y, z] = 1
                z += 1
            y += 1
        x += 1
    return score_boards


# -------------------
# --- Check bingo ---
# -------------------
def check_bingo(score_boards):
    bingo = False
    x = 0
    for _ in score_boards:
        for row in range(5):
            for column in range(5):
                bingo = True
                if score_boards[x, row, column] == 0:
                    bingo = False
                    break
            if bingo:
                break
        if bingo:
            break
        x += 1

    if not bingo:
        x = 0
        for _ in score_boards:
            for column in range(5):
                for row in range(5):
                    bingo = True
                    if score_boards[x, row, column] == 0:
                        bingo = False
                        break
                if bingo:
                    break
            if bingo:
                break
            x += 1

    return bingo, x


# --------------------------
# --- Check bingo boards ---
# --------------------------
def check_bingo_boards(score_boards, boards):
    latest_board = -1
    for board_nr in range(len(boards)):
        if not boards[board_nr]:
            # check rows
            for row in range(5):
                for column in range(5):
                    bingo = True
                    if score_boards[board_nr, row, column] == 0:
                        bingo = False
                        break
                if bingo:
                    boards[board_nr] = True
                    latest_board = board_nr
                    break
        if not boards[board_nr]:
            # check columns
            for column in range(5):
                for row in range(5):
                    bingo = True
                    if score_boards[board_nr, row, column] == 0:
                        bingo = False
                        break
                if bingo:
                    boards[board_nr] = True
                    latest_board = board_nr
                    break

    for board in boards:
        bingo_all = True
        if not board:
            bingo_all = False
            break

    return bingo_all, latest_board, boards


# -----------------------------
# --- Calculate Final Score ---
# -----------------------------
def calculate_final_score(board, random_number, bingo_boards, score_boards):
    board_sum = 0
    for row in range(5):
        for column in range(5):
            if score_boards[board, row, column] == 0:
                board_sum += bingo_boards[board, row, column]

    return board_sum * random_number


# ---------------------------
# --- Score winning board ---
# ---------------------------
def score_winning_board(filename):
    bingo_list, matrix_nr, drawn_numbers = read_bingo_input(filename)
    bingo_boards, score_boards = make_bingo_boards(bingo_list, matrix_nr)

    for random_number in drawn_numbers:
        score_boards = check_bingo_number(bingo_boards, score_boards, random_number)
        bingo, board = check_bingo(score_boards)
        if bingo:
            final_score = calculate_final_score(board, random_number, bingo_boards, score_boards)
            break

    return final_score


# ---------------------------
# --- Last winning board ---
# ---------------------------
def last_winning_board(filename):
    boards = []
    bingo_list, matrix_nr, drawn_numbers = read_bingo_input(filename)
    bingo_boards, score_boards = make_bingo_boards(bingo_list, matrix_nr)
    for board_nr in range(matrix_nr):
        boards.append(False)

    for random_number in drawn_numbers:
        score_boards = check_bingo_number(bingo_boards, score_boards, random_number)
        bingo_all, board, boards = check_bingo_boards(score_boards, boards)
        if bingo_all:
            final_score = calculate_final_score(board, random_number, bingo_boards, score_boards)
            break

    return final_score


print("Part 1: ", score_winning_board("bingo_input"))
print("Part 2: ", last_winning_board("bingo_input"))
