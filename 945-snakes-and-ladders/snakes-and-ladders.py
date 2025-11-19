class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def num_to_pos(cell):
            row = (cell-1) // length
            col = (cell-1) % length

            if row % 2 == 1:
                col = length - col - 1

            return [row, col]

        q = collections.deque()
        q.append([1, 0])
        visited = set()
        while q:
            pos, steps = q.popleft()

            for i in range(1, 7):
                next_pos = pos + i
                row, col = num_to_pos(next_pos)

                if board[row][col] != -1:
                    next_pos = board[row][col]
                
                if next_pos == length * length:
                    return steps + 1

                if next_pos not in visited:
                    visited.add(next_pos)
                    q.append([next_pos, steps+1])
        return -1