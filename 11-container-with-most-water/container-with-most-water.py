class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxm=0
        while (left <right):

            minm=min(height[left],height[right])
            maxm=max(minm*(right-left),maxm)
            if minm == height[left]:
                left+=1
            else:
                right-=1

        return maxm