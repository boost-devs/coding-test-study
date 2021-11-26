# ref https://leetcode.com/problems/course-schedule/discuss/58750/Python-easy-to-understand-indegree-solution-with-comments.
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        indegree = [set() for _ in range(numCourses)] # 과목을 수강하기 위한 선수 과목 set
        outdegree = [[] for _ in range(numCourses)] # 과목 별 후 강의 list
        for pre in prerequisites:
            indegree[pre[0]].add(pre[1])
            outdegree[pre[1]].append(pre[0])
        # start = 선수 과목이 필요없는 과목들
        start, count = [i for i in range(numCourses) if not indegree[i]], 0
        while start:
            newStart = []
            for i in start:
                count += 1 # start에 있는 괴목은 선수과목이 충족되었으니 ++
                for j in outdegree[i]: # 강의를 듣고 다음 단계의 강의 for 문
                    indegree[j].remove(i) # 선수 과목 빼기
                    if not indegree[j]:# 뺄 선수 과목이 없다면 해당 강의는 들을 수 있는 강의
                        newStart.append(j)
            start = newStart
        return count == numCourses # 모든 과목들이 선수 과목들을 충족 했는지 판단
numCourses = 4
prerequisites = [[1,0],[2,1],[3,1]]
a = Solution()
a.canFinish(numCourses, prerequisites)