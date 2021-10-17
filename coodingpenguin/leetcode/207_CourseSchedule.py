# 문제: 207. Course Schedule
# 링크: https://leetcode.com/problems/course-schedule/

# 시간/공간: 92ms / 15.7MB
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for b, a in prerequisites:
            graph[a].append(b)
            indegrees[b] += 1

        queue = collections.deque()
        for i in range(numCourses):
            if i not in indegrees:
                queue.append(i)

        if not queue:
            return False

        while queue:
            v = queue.popleft()
            for i in graph[v]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)

        return all([True if v == 0 else False for k, v in indegrees.items()])
