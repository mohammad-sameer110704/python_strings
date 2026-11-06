class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest = ""

        if not strs:
            return longest

        for i in range(len(strs[0])):
            for j in range(len(strs)-1):

                if i >= len(strs[j]) or i >= len(strs[j+1]):
                    return longest

                if strs[j][i] != strs[j+1][i]:
                    return longest

            longest = longest + strs[0][i]

        return longest