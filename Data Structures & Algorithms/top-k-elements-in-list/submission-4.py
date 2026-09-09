class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = collections.defaultdict(int)
        # counts = [] { numer: count }
        
        freq = [[] for i in range(len(nums)+ 1)]

        result = []

        for n in nums:
            count[n] += 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        
        
