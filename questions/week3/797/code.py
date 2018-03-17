class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        all_paths = []
        paths = []
        for _ in graph:
            paths.append([])

        for i, node in reversed(list(enumerate(graph))):
            if len(node) == 0:
                paths[i].append([i])
                continue
            for connection in node:
                for old_connection in paths[connection]:
                    paths[i].append([i] + old_connection)
        return paths[0]
