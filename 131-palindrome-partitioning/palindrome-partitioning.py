class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        def solve(start,cur):
            if start==len(s):
                result.append(cur[:])
            for end in range(start,len(s)):
                par=s[start:end+1]

                if par==par[::-1]:
                    cur.append(par)

                    solve(end+1,cur)

                    cur.pop()

        solve(0,[])
        return result 