class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        a_index = len(A) - 1
        b_index = 0

        while a_index >= 0:
            # print A[a_index:], B[:b_index+1]
            if A[a_index:] == B[:b_index+1]:
                # check other side
                a_beginning = A[:a_index]
                b_end = B[b_index+1:]
                # print'h',  a_beginning, b_end
                if a_beginning == b_end:
                    return True
            a_index -= 1
            b_index += 1
        return False
