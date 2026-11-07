class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        i = len(s) 
        length =  0
        while i > 0 :
            if s[i-1] != " ":
                length +=1
                i -=1
            else :
                return length
        return length



