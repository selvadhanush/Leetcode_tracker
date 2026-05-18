class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        hash={}
        for num in nums:
            if num in hash:
                hash[num]+=1
            else:
                hash[num]=1
        max_feq=max(hash.values())
        ans=0
        for feq in hash.values():
            if feq==max_feq:
                ans+=feq
        return ans