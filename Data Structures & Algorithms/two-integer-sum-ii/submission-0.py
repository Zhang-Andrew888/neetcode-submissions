class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            l = numbers[left]
            r = numbers[right]

            diff = target - l - r

            if diff == 0:
                return [left + 1, right + 1]
            elif diff < 0:
                right -= 1
            else:
                left += 1
        
        return [-1, -1]