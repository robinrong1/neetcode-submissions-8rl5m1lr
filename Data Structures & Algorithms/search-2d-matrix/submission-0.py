class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        l, r = 0 , len(matrix) * len(matrix[0]) - 1
        rowLength = len(matrix[0])
        while l <= r:
            mid = (l+r)//2
            row = mid // rowLength
            col = mid % rowLength
            midVal = matrix[row][col]
            if midVal < target:
                l = mid + 1
            elif midVal > target:
                r = mid - 1
            else:
                return True
        return False
            