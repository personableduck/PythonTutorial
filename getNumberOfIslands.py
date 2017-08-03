function getNumberOfIslands(binaryMatrix):
    islands = 0
    rows = binaryMatrix.length # number of rows
    cols = binaryMatrix[0].length # number of columns

    for i from 0 to rows-1:
        for j from 0 to cols-1:
            if (binaryMatrix[i][j] == 1):
                markIsland(binaryMatrix, rows, cols, i, j)
                islands++
                
    return islands


function markIsland(binaryMatrix, rows, cols, i, j):
    q = new Queue()
    q.push([i,j])
    while (!q.isEmpty()):
        item = q.pop()
        x = item[0]
        y = item[1]
        if (binaryMatrix[x][y] == 1):
            binaryMatrix[x][y] = -1
            pushIfValid(q, rows, cols, x-1, y)
            pushIfValid(q, rows, cols, x, y-1)
            pushIfValid(q, rows, cols, x+1, y)
            pushIfValid(q, rows, cols, x, y+1)


function pushIfValid(q, rows, cols, x, y):
    if (x >= 0 AND x < rows AND y >= 0 AND y < cols):
        q.push([x,y])
