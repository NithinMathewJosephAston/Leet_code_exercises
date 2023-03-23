class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        board_ = []
        for element in board:
            board_.extend(element)
        for element_ in word:
            if element_ not in board_:
                return False
            else:
                board_.remove(element_)
        return True

gems = Solution()
print(gems.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ADE"))