def generateMatrix(n):
    matrix = []
    insertMatrix = []
    counter = 0
    for i in range(n*n):
        if counter < n - 1:
            insertMatrix.append(i+1)
            counter += 1
        else:
            counter = 0
            insertMatrix.append(i+1)
            matrix.append(insertMatrix.copy())
            insertMatrix.clear()

    top, bottom = 0, n
    left, right = 0, n
    num = 1
    while left < right and top < bottom:
        print(num)
        for i in range(left, right):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom):
            matrix[i][right-1] = num
            print(num)
            num += 1
        right -= 1

        if not left < right and top < bottom:
            break

        for i in range(right -1, left-1, -1):
            matrix[bottom - 1][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom - 1, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    
    print(matrix)
    return matrix

generateMatrix(3)