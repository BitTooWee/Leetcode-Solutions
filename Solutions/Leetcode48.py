class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def rotateone(x,y):
            prevvalue = matrix[y][x]
            for i in range(0,3):
                newy = x
                newx = int(-1*(y - (len(matrix)-1)/2) + (len(matrix)-1)/2)
                temp = matrix[newy][newx]
                matrix[newy][newx] = prevvalue
                prevvalue = temp
                x = newx
                y = newy
            newy = x
            newx = int(-1*(y - (len(matrix)-1)/2) + (len(matrix)-1)/2)
            matrix[newy][newx] = prevvalue
        m = int(math.ceil(len(matrix)/2))
        n = int(math.floor(len(matrix)/2))
        for i in range(0,m):
            for j in range(0,n):
                rotateone(i,j)
