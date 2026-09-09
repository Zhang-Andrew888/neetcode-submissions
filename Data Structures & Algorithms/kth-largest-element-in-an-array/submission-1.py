class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # segment array to store the first k elements into arrray of size k
        # heapify that array into a max_heap: make all elements negative
        # for each remaining element, if the head element is less negative than new element, pop and replace
        # once done iterating, we return first element

        min_heap = nums[:k]

        heapq.heapify(min_heap)
        
        for i in range(k, len(nums)):
            heapq.heappushpop(min_heap, nums[i])

        return min_heap[0] 
        