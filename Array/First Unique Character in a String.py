class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for i in range(len(s)):
            if s[i] in dict:
                del dict[s[i]]
            else:
                dict[s[i]] = i
        r = dict.values()
        if len(r) > 0:
            return r[0]
        else:
            return -1
            