class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        rows, cols = len(board), len(board[0])
        board.reverse()
        def num_to_pos(square):
            r = (square-1)//rows
            c = (square-1)% cols
            if r % 2:
                c = cols - 1 - c
            return [r,c]

                
        q = collections.deque()
        q.append([1, 0])

        visited = set()

        while q:
            pos, moves = q.popleft()
            
            for i in range(1, 7):
                next_pos = pos + i
                row, col = num_to_pos(next_pos)

                if (board[row][col] != -1):
                    next_pos = board[row][col]

                if next_pos == rows * cols:
                    return moves + 1

                if next_pos not in visited:
                    visited.add(next_pos)
                    q.append([next_pos, moves+1])
        return -1
                    


            
            


"""
[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]
]

alernating: from n-1R, n-1Col to n-2R, n-1Col - column index remain constant

6 possible next cells for non snake or ladder

you start at square 1 (n-1, 0)
return the minimum possible ways to get to the end position (0,0)

we need to kind of see where we move for each step like in range [curr+1, min(curr+6, n**2)]


                1
        2   3   4   5   6   7
    15                     8 9 10 11 12     13 
    21                                    14      15 16 17 18 19
    27                                 35         
    33                                36
    36
"""