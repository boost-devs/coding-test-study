class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            graph[c].append(p)
        
        def is_cyclic(course):
            if visited[course] == -1:
                return True
            elif visited[course] == 1:
                return False
            
            visited[course] = -1
            for prereq in graph[course]:
                if is_cyclic(prereq):
                    return True
            visited[course] = 1
            return False
            
        for start, _ in prerequisites:
            visited = [0] * numCourses
            if is_cyclic(start):
                return False
        return True
        