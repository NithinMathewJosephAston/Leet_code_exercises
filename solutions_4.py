class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        palindrome = []
        for element in str(x):
            palindrome.append(element)
        palindrome.reverse()
        palindrome = ('').join(palindrome)
        if palindrome == str(x):
            return True
        else:
            return False

gems = Solution()
print(gems.isPalindrome(-121))