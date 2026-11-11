class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length=len(nums)
        notseen=set(nums)
        if len(notseen)!=length:
            return True
        else:
            return False