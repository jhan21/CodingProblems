def spiralOrder(matrix):
    """
    Spiral Matrix Method

    """
    spiralAnswer = []
    #How to solve this snakelike problem
    #Let's first get the dimensions of the matrix
    height = len(matrix)
    width = len(matrix[0])

    #By keeping track of the dimensions and keeping them in check
    #I can most likely solve this problem
    left, right = 0, width
    top, bottom = 0, height

    #While loop to keep looping through until all numbers are covered
    while left < right and top < bottom:
        #inserting top row
        for i in range(left, right):
            spiralAnswer.append(matrix[top][i])
        top += 1

        #inserting right column
        for i in range(top, bottom):
            spiralAnswer.append(matrix[i][right - 1])
        right -= 1

        #Checks for the middle
        if not (left < right and top < bottom):
            break
        
        #inserting bottom row
        for i in range(right - 1, left - 1, -1):
            spiralAnswer.append(matrix[bottom - 1][i])
        bottom -= 1

        #inserting left column
        for i in range(bottom - 1, top - 1, -1):
            spiralAnswer.append(matrix[i][left])
        left += 1
    print(spiralAnswer)
    return(spiralAnswer)

matrix4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix3 = [[1,2,3],[4,5,6],[7,8,9]]

spiralOrder(matrix4)