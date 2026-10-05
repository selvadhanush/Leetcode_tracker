class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap={}
        
        for i , num in enumerate(nums):
            com=target-num 
            if com in hashmap:
                return hashmap[com],i
            hashmap[num]=i