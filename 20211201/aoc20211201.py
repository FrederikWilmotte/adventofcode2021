# Advent of Code 2021
# Author: Frederik Wilmotte
# --- Day 1: Sonar Sweep ---


seaDepthArray = []
depthIncrease = 0
depthIncrease2 = 0


def read_file():
    return open("sonarSweepReport_input", "r")

# Part 1

# Load sea floor depth in array
seaDepthArray.clear()
for seaDepth in read_file():
    seaDepthArray.append(int(seaDepth))

while len(seaDepthArray) > 1:
    if seaDepthArray[1] > seaDepthArray[0]:
        depthIncrease += 1
    seaDepthArray.pop(0)

# Part 2

# Load sea floor depth in array
seaDepthArray.clear()
for seaDepth in read_file():
    seaDepthArray.append(int(seaDepth))

while len(seaDepthArray) > 3:
    if sum(seaDepthArray[1:4]) > sum(seaDepthArray[0:3]):
        depthIncrease2 += 1
    seaDepthArray.pop(0)

print("Number of depth increase - Part 1:", depthIncrease)
print("Number of depth increase - Part 2:", depthIncrease2)
