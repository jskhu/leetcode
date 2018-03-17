class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        tower = [[0] * k for k in xrange(1, 102)]
        tower[0][0] = poured

        for row in range(query_row + 1):
            for col in range(row + 1):
                q = (tower[row][col] - 1.0) / 2.0
                if q > 0:
                    tower[row+1][col] += q
                    tower[row+1][col + 1] += q
        if tower[query_row][query_glass] > 1:
            return 1
        return tower[query_row][query_glass]
