class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # mandarin = []
        # if strs[0]:
        #     for index in range(len(strs[0])+1):
        #         if index:
        #             mandarin.append(strs[0][0:index])
        #         else:
        #             mandarin.append(strs[0][index])
        #     for element in mandarin[::-1]:
        #         flag = [checker for checker in strs[1:len(strs)] if checker.startswith(element)]
        #         if len(flag) == len(strs[1:len(strs)]):
        #             return element
        # return ""
        if len(strs) == 0:
            return ''

        w1, w2 = min(strs), max(strs)
        i = 0
        debug = len(min(strs, key=len))
        _debug = min(strs, key=len)
        while i < len(min(strs, key=len)) and w1[i] == w2[i]:
            i += 1

        return w1[:i]

gems = Solution()
print(gems.longestCommonPrefix(["c","zcc","ccc"]))