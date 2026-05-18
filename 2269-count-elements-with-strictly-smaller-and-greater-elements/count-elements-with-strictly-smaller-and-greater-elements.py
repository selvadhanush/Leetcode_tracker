class Solution:
    def countElements(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            max_ele=max(nums)
            min_ele=min(nums)
            if i<max_ele and i>min_ele:
                count+=1
        return count 
        