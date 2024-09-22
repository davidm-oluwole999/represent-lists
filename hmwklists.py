#Get 20 random marks for 20 students (between 0 to 100). Create 3 separate lists . The first list should contain the marks <=30.
#  The second list between 31 to 69. The third list >= 70.Display the output lists
matrix= [[5,8,12,18,23,27,30],[34,38,41,47,52,55,68],[74,78,80,84,91,95,99]]

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        print(matrix[i][j], end=" ")
    print("\n")

