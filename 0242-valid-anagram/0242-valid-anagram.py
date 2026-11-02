class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        order={}
        for i in range(len(s)):
            if s[i] in order:
                order[s[i]]=order[s[i]]+1
            else:
                order[s[i]]=1

            if t[i] in order:
                order[t[i]]=order[t[i]]-1    
            else:
                order[t[i]]=-1

        for value in order.values():
            if value != 0:
                return False
        return True



        