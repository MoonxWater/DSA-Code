from engine import Engine

test_cases = [
    ([[
  [0,1],
  [1,0]
]], {'mod':[
  [0,0],
  [0,0]
]}),
([[
  [1,2,3],
  [4,0,5],
  [6,7,8]
]], {'mod':[
  [1,0,3],
  [0,0,0],
  [6,0,8]
]})
]
run = Engine(test_cases)

'''
About this problem:

'''


#----Solution-----------------------------------------------------------------


'''
keep a weight array equal to column of the matrix
1. run a loop over each row and check if the element is zero
2. if the current element is zero, make the corresponding
    weight zero
3. after inner loop, make the entire row zero

4.run another loop and multiply each element with the 
    corresponding weight
Note: In place, return None
'''

def set_matrix_zero(matrix: list[list[int]]) -> None:
    weights = [1] * len(matrix[0])

    for i in range(len(matrix)):
        found = False

        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                weights[j] = 0
                found = True
        if found:
            matrix[i] = [0] * len(matrix[i])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= weights[j]
    

run.v8(set_matrix_zero)