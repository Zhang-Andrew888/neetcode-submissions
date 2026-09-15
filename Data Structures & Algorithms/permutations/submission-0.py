class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking problem
        # Recursive call function that uses depth first search and our goal is to as soon as we reach terminal of the search return the final list
        # dfs has two parameters: ongoing list, remaining list. 
        # base case, if remaining list is length 1, we return the ongoing list appended with remaining list
        # recursive case, iterate throug remaining numbers, where we pop it from the remaining list and append it to the ongoing list. 
        res = []

        def dfs(ongoing, remaining):
            if len(remaining) == 1:
                res.append(ongoing + [remaining.pop()])
                return
            
            for num in remaining:
                remaining_copy = remaining.copy()
                remaining_copy.remove(num)
                dfs(ongoing + [num], remaining_copy)
        
        dfs([], set(nums))
        return res