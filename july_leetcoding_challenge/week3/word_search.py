from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for y in range(len(board)):
            for x in range(len(board[y])):
                if self.dfs(board, x, y, word):
                    return True
        return False

    def dfs(self, board, x, y, word):
        if len(word) == 0: return True
        if x<0 or x>=len(board[0]) or y<0 or y>=len(board) or board[y][x] != word[0]:
            return False
        tmp, board[y][x] = board[y][x], '-'
        res = self.dfs(board, x+1,y,word[1:]) or self.dfs(board, x-1,y,word[1:]) \
              or self.dfs(board, x,y+1,word[1:]) or self.dfs(board, x,y-1,word[1:])
        board[y][x] = tmp
        return res
if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "SEE"
    s = Solution()
    print(s.exist(board, word))