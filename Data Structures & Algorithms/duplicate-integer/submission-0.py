class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list=[]
        length=len(nums)
        for i in range(0,len(nums)):
            if nums[i] not in list:
                list.append(nums[i])
        if length!=len(list):
            return True
        else:
            return False