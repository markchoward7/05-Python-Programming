import random

# initialize the 2d list for the matrix
matrix = [[],[],[],[]]
# initalize lists for the highest rows and columns
highestRow = [0]
highestCol = []
# for loop enumerating over the rows of matrix
for index, row in enumerate(matrix):
    # initialize accumulator
    total = 0
    # for loop for 4 entries into each matrix row
    for _ in range(4):
        # generate a random number and add it to the matrix and to the accumulator
        randNum = random.randint(0,1)
        row.append(randNum)
        total += randNum
    # print the matrices
    print(row)
    # if not the first row
    if index != 0:
        # check if this row is bigger and replace the list if so
        if total > matrix[highestRow[0]].count(1):
            highestRow = [index]
        # otherwise, check if row is the same size and add it to list
        elif total == matrix[highestRow[0]].count(1):
            highestRow.append(index)
# print highest row results
print("Highest row(s):", highestRow)
# initialize a list of accumulators for columns
total = [0,0,0,0]
# double range loop to get the matching indices for rows and columns
for index in range(4):
    for index2 in range(4):
        # reverse the usage of indices to check columns instead of rows
        # and add to appropriate accumulator
        total[index] += matrix[index2][index]
# for loop for the accumulators to check which ones are the highest
for i in range(total.count(max(total))):
    highestCol.append(total.index(max(total)) + i)
    total.remove(max(total))
# print results of highest column check
print("Highest column(s):", highestCol)