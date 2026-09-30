class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0,r-1):
            for j in range(i+1,c):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

        for i in range(0,r):
            matrix[i].reverse()

        
   
        