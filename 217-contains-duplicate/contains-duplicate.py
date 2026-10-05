class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        sett=set()
        for i in nums:
            if i in sett:
                return True
            sett.add(i)
        return False