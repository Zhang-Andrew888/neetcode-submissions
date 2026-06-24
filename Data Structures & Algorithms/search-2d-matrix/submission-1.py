class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_row, right_row = 0, len(matrix) - 1
        row = 0

        # special part of Binary Search
        while left_row <= right_row:
            mid_row = (left_row + right_row) // 2

            if matrix[mid_row][0] <= target and target <= matrix[mid_row][-1]:
                row = mid_row
                break
            elif matrix[mid_row][0] > target:
                right_row = mid_row - 1
            # elif matrix[mid_row][-1] < target:
            #     left_row = mid_row + 1
            # else:
            #     raise ValueError("Violates preconditions")
            else:
                left_row = mid_row + 1
        
        if left_row > right_row:
            return False
        
        # standard binary search
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid -1
            else:
                l = mid + 1
        
        return False





