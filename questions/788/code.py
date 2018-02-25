import math

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        not_allowed = {
            1:
        }
        power = int(math.floor(math.log(N, 10)))
        for i in range(power, -1, -1):
            num = int(N / math.pow(10, i))


            N -= num * math.pow(10, i)
            print num
        return power
