class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # freqs = [[] for i in range (len(nums) + 1)]

        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        
        # for key, v in count.items():
        #     freqs[v].append(key)
        
        # res = []
        # for i in range(len(freqs) - 1, 0, -1):
        #     for n in freqs[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        


                


            


