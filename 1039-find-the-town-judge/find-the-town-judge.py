class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0] * (n + 1)
        trusted_by = [0] * (n + 1)
        
        for i, j in trust:
            trusts[i] += 1
            trusted_by[j] += 1
            
        for i in range(1, n+1):
            if trusted_by[i] == n - 1 and trusts[i] == 0:
                return i
            
        return -1
        