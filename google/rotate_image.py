from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[0])):
                res[x][y] = matrix[len(matrix) - y - 1][x]

        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[0])):
                matrix[y][x] = res[y][x]

        return matrix

if __name__ == '__main__':
    num = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,4,12,16]]
    s = Solution()
    print (s.rotate(num))