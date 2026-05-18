class Solution:
    def countElements(self, nums: List[int]) -> int:
        count=0
        max_ele=max(nums)
        min_ele=min(nums)
        for i in nums:
            if i<max_ele and i>min_ele:
                count+=1
        return count 
        