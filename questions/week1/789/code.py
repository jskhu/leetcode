class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        current_loc = target[0], target[1], abs(target[0]) + abs(target[1])
        for i, ghost in enumerate(ghosts):
            moves = abs(ghost[0] - current_loc[0]) + abs(ghost[1] - current_loc[1])
            if moves <= current_loc[2]:
                return False
        return True
