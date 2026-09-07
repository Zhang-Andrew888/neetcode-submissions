class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points

        max_heap = [0] * k

        for i in range(k):
            x, y = points[i]
            dist = x**2 + y**2
            max_heap[i] = (-dist, i)
        
        heapq.heapify(max_heap)

        for i in range(k, len(points)):
            x, y = points[i]
            dist = x**2 + y**2

            if -(max_heap[0][0]) > dist:
                heapq.heappushpop(max_heap, (-dist, i))

        res = [0] * k

        for i in range(0, len(max_heap)):
            _, j = max_heap[i]

            res[i] = points[j] 
        
        return res

                