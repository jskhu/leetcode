class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """

        win_cases = ["XXX", "OOO"]
        possible_win_cases = board[:]
        x_count = 0
        o_count = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'X':
                    x_count += 1
                elif board[row][col] == 'O':
                    o_count += 1

        for i in range(len(board)):
            possible_win_cases.append("".join([x[i] for x in board]))

        possible_win_cases.append("".join([board[0][0], board[1][1], board[2][2]]))
        possible_win_cases.append("".join([board[0][2], board[1][1], board[2][0]]))

        found_x_win_case = 0
        found_o_win_case = 0
        for i in possible_win_cases:
            if i == 'XXX':
                found_x_win_case += 1
            elif i == 'OOO':
                found_o_win_case += 1
            if found_x_win_case > 1 or found_o_win_case > 1:
                return False

        if (x_count - o_count) not in [1, 0] or ((x_count - o_count) == 0 and found_x_win_case) or ((x_count - o_count) == 1 and found_o_win_case):
            return False

        return True
