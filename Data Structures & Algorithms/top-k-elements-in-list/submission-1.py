class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arr = [[] for i in range(len(nums)+ 1)]

        for n, c in count.items():
            arr[c].append(n)

        res = []

        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res
        




