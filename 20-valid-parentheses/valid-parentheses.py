class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pair={"}":"{",
                "]":"[",
                ")":"("}
        for i in s:
            if i in pair.values():
                stack.append(i)
            elif i in pair.keys():
                if not stack or pair[i]!=stack.pop():
                    return False
        return not stack