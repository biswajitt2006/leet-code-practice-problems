class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range (len(matrix) ) :
            for j in range(i+1,n) :
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp

        for i in range(n) :
            for j in range(n//2) :
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][n-1-j]
                matrix[i][n-1-j]=temp

        """
        Do not return anything, modify matrix in-place instead.
        """
        