class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # store all stone into a max heap
        # from there, pop the two largest elements
        # if equal weights, do nothing
        # if first stone is more heavier than second stone, we put the difference back into heap
        # loop until the len of the heap is ≤ 1

        max_heap = [-x for x in stones]
        
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = heapq.heappop(max_heap)
            x = heapq.heappop(max_heap)

            diff = -(y-x)

            if diff > 0:
                heapq.heappush(max_heap, -diff)
        
        if len(max_heap) == 1:
            return heapq.heappop(max_heap) * -1
        
        return 0
