#!/usr/bin/python

class GridProblem:
	
	#print function to print the matrix in observable grid
	
        @staticmethod
        def printList(a):
            for i in range(6):
                val = ''
                for j in range(6):
                    val += str(a[i][j])+ " "
                print(val)

	# DFS implementaion of grid search for path

	@staticmethod
        def findPath(arr, currentX, currentY, endX, endY, res, visited):
            if(currentX == (endX - 1)  and currentY == (endY - 1)):
                print("Path Found")
                GridProblem.printList(res)
                return
            
	    if (( currentY + 1 < endY) and (arr[currentX][currentY+1] == 0) and (not visited[currentX][currentY+1])):
                visited[currentX][currentY+1]=True
                res[currentX][currentY+1] = 1
                GridProblem.findPath(arr, currentX, currentY+1, endX, endY, res, visited)


            if ((currentX + 1 < endX ) and (arr[currentX+1][currentY] == 0) and (not visited[currentX+1][currentY])):
                visited[currentX+1][currentY]=True
                res[currentX+1][currentY] = 1
                GridProblem.findPath(arr, currentX+1, currentY, endX,endY, res, visited)



vis =[]
for i in range(6):
    vis.append([])
    for j in range(6):
        vis[i].append(False)

res = []
for i in range(6):
    res.append([])
    for j in range(6):
        res[i].append(0)


Grid = [[ 0 , 1 , 0, 1 , 1, 0],
        [ 0 , 0 , 1, 0 , 1, 0],
        [ 1 , 0 , 1, 0 , 1, 0],
        [ 1 , 0 , 1, 1 , 0, 1],
        [ 0 , 0 , 0, 0 , 1, 0],
        [ 0 , 1 , 0, 0 , 0, 0]
        ]
GridProblem.findPath(Grid, 0, 0, 6, 6, res,vis)
