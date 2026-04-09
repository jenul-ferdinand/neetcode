class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurmap = {x: 0 for x in nums}
        for num in nums:
            occurmap[num] += 1
            if occurmap[num] > 1:
                return True
        
        return False
        