class Solution:
    def maxScore(self, s: str) -> int:
        divide = 1
        maxx = 0
        while divide<len(s):
            score = s.count("0",0,divide) + s.count("1",divide)
            maxx = max(maxx, score)
            divide +=1
        return maxx

        
