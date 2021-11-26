// 207. Course Schedule
// Runtime: 60 ms, faster than 8.89 % of C++ online submissions for Course Schedule.
// Memory Usage : 16.8 MB, less than 8.35 % of C++ online submissions for Course Schedule.
// ref: https://leetcode.com/problems/course-schedule/discuss/1519258/Easy-C%2B%2B-Solution-using-cycle-detection-in-a-directed-graph

class Solution {
public:
#define MAX 100001

    int N;
    vector<int> v[MAX];
    bool visit[MAX];
    bool visit_all[MAX];

    bool dfs(int cur) {
        visit_all[cur] = visit[cur] = true;
        for (auto i : v[cur]) {
            if (visit[i]) return false;
            else if (!visit_all[i]) {
                if (!dfs(i)) return false;
            }
        }
        visit[cur] = false;
        return true;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // init
        N = numCourses;
        for (auto i : prerequisites)
            v[i[0]].push_back(i[1]);

        // check cycle
        for (int i = 0; i < N; i++)
            if (!visit_all[i] && !dfs(i)) return false;

        return true;
    }
};