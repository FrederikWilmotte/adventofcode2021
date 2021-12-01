# Advent of Code 2021
# Author: Frederik Wilmotte
# --- Day 1: Sonar Sweep ---

sonarSweepReport = open("sonarSweepReport_input", "r")
seaDepthArray = []
address = 1
address2 = 2
depthIncrease = 0
depthIncrease2 = 0

# Load sea floor depth in array
for seaDepth in sonarSweepReport:
    seaDepthArray.append(int(seaDepth))

# Part 1
while address < len(seaDepthArray):
    if seaDepthArray[address] > seaDepthArray[address-1]:
        depthIncrease += 1
    address += 1

# Part 2
seaDepthSum = seaDepthArray[address2] + seaDepthArray[address2-1] + seaDepthArray[address2-2]
address2 += 1
while address2 < len(seaDepthArray):
    if (seaDepthArray[address2] + seaDepthArray[address2-1] + seaDepthArray[address2-2]) > seaDepthSum:
        depthIncrease2 += 1
    seaDepthSum = seaDepthArray[address2] + seaDepthArray[address2 - 1] + seaDepthArray[address2 - 2]
    address2 += 1

print("Number of depth increase - Part 1:", depthIncrease)
print("Number of depth increase - Part 2:", depthIncrease2)