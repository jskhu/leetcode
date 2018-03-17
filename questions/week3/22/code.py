class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def makeParenthesis(is_left, left_b, right_b):
            if left_b == 0 and right_b == 0:
                return [")"]
            left_permutations = []
            right_permutations = []
            if left_b > 0:
                left_permutations = makeParenthesis(1, left_b-1, right_b)
            if right_b > 0 and right_b > left_b:
                right_permutations = makeParenthesis(0, left_b, right_b-1)

            permutations = left_permutations + right_permutations
            if is_left:
                final_permutations = ["(" + p for p in permutations]
            else:
                final_permutations = [")" + p for p in permutations]

            return final_permutations

        return makeParenthesis(1, n-1, n)
