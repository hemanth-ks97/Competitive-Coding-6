# Time Complexity : O(n!)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : YES

# Any problem you faced while coding this : NO

class Solution:
    def countArrangement(self, n: int) -> int:      
        res = []
        seen = set() 
        cur_perm = []

        def recurse(i):
            if len(cur_perm) == n:
                res.append(cur_perm[::])
                return
            
            # logic
            for x in range(1,n+1):
                if x in seen or (x % i != 0 and i % x != 0):
                    continue
                seen.add(x)
                cur_perm.append(x)
                recurse(i+1)
                seen.remove(x)
                cur_perm.pop()

        recurse(1)
        return len(res)