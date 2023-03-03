class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # sum = 0
        hashes_ = {'(': ')', '[':']', '{':'}'}
        stack = []
        for element in s:
            if element in hashes_:
                stack.append(hashes_[element])
            elif not stack or stack[-1]!=element:
                return False
            else:
                stack.pop()
        return len(stack)==0


gems = Solution()
print(gems.isValid("()"))