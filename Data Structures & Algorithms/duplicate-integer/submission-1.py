class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        all = set()
        for i in nums:
            if i in all:
                return True
            else:
                all.add(i)
        return False