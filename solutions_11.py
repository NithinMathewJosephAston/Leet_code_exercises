class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip(' ')
        last_word = s.split()[-1]
        # last_word = s.split(' ')[-1]
        length = len(last_word)
        return "The last word is \"{}\" with length {}".format(last_word, length)

gems = Solution()
print(gems.lengthOfLastWord("   fly me   to   the moon  "))