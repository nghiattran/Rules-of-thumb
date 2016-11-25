# Given an 2D board, count how many different battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# Invalid Example:
# ...X
# XXXX
# ...X
# This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
 
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        cols = len(board)
        rows = len(board[0])
        ct = 0
        for c in xrange(cols):
            for r in xrange(rows):
                # We count a battleship only first time we see it. If a battleship piece 'X'
                # is encountered, it is only new if neither the upper or left components are not also
                # pieces of the same battleship. These prior indices are guarenteed to already be explored by 
                # the time we get to the current board index.
                if board[c][r] != 'X':
                    continue
                if r > 0 and board[c][r - 1] == 'X':
                    continue
                if c > 0 and board[c - 1][r] == 'X':
                    continue
                ct += 1
        return ct