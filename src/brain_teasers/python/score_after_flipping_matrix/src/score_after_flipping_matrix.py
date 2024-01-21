#helper function
def convToInt(l):
    """l is a list of 0 & 1 that function convert to a decimal number"""
    sNum = ''.join(str(e) for e in l)
    decNum = int(sNum,2)
    return decNum

#helper function
def flipNum(l):
    """l is a list that contains 1 and 0 items oonly. this function
       turn 1 to 0 and vice versa"""
    for i in range(len(l)):
         if l[i] == 0:
              l[i] = 1
         else:
              l[i] = 0
    return l

def scoreAfterFlip(matrix):
    """We are given a matrix that contains only 0s and 1s. Each row
       represents a binary number. We can flip any number of rows and columns.
       We want to maximize the sum of the numbers in the matrix after flipping
    """
    #for maximum of sum, the first item of every row has to be 1
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            l = flipNum(matrix[i])
            matrix[i] = l
    # in every column except the first, if number of 0 is greater than 1, the column be flipped
    for i in range(1,len(matrix[0])):
        #coList: list of every column numbers
        coList = []
        for j in range(len(matrix)):
            coList.append(matrix[j][i])
        if coList.count(0) > len(matrix)/2:
            l = flipNum(coList)
            for k in range(len(l)):
                matrix[k][i] = l[k]
    sumNumb = 0
    for i in matrix:
        sumNumb += convToInt(i)
    return sumNumb
