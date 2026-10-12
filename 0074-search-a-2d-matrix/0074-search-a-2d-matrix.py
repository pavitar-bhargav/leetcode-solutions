class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = (rows * cols) - 1

        while left <= right:
            mid = (left + right) // 2

            current_row = mid//cols
            current_col = mid % cols

            mid_value = matrix[current_row][current_col]

            if mid_value == target:
                return True

            elif mid_value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
        