class Solution(object):
    def spiralOrder(self, matrix):
        m = len(matrix[0]) #x
        n = len(matrix) #y
        result = []
        current = [-1,0]
        while len(result) < len(matrix)*len(matrix[0]):
            for i in range(0,m):
                current[0] += 1
                result.append(matrix[current[1]][current[0]])
                if len(result) >= len(matrix)*len(matrix[0]):
                    break
            if len(result) >= len(matrix)*len(matrix[0]):
                    break
            n -= 1
            for i in range(0,n):
                current[1] += 1
                result.append(matrix[current[1]][current[0]])
                if len(result) >= len(matrix)*len(matrix[0]):
                    break
            if len(result) >= len(matrix)*len(matrix[0]):
                    break
            m -= 1
            for i in range(0,m):
                current[0] -= 1
                result.append(matrix[current[1]][current[0]])
                if len(result) >= len(matrix)*len(matrix[0]):
                    break
            if len(result) >= len(matrix)*len(matrix[0]):
                    break
            n -= 1
            for i in range(0,n):
                current[1] -= 1
                result.append(matrix[current[1]][current[0]])
                if len(result) >= len(matrix)*len(matrix[0]):
                    break
            if len(result) >= len(matrix)*len(matrix[0]):
                    break
            m -= 1
        return result
