matrix = [
   #c0 c1 c2
    [1,2,3],  #r0
    [4,5,6],  #r1
    [7,8,9]   #r2

]
            #r*c
print(matrix[1][2])

#modification
matrix[1][2] = 20
print(matrix[1][2])

#for loop for list out

for row in matrix:
    for column in row:
        print(column)