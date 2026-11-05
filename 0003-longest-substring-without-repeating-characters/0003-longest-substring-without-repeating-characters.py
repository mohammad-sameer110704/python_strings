class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dummy=""
        longest=""
        c=0
        for i in s:
            if i not in dummy:
                dummy = dummy + i
                c=max(c,len(dummy))
            else :
                dummy = dummy[dummy.index(i)+1:]+i

        return c
        