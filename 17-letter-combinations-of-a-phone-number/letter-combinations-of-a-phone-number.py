class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result=[]
        
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if not digits:
            return result 
        def solve(index,curr):
            if index==len(digits):
                result.append(curr)
                return
            for letter in letters[digits[index]]:
                curr+=letter
                solve(index+1,curr)
                curr=curr[:-1]

        solve(0,'')
        return result 