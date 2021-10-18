// 79. Word Search
// Runtime: 1388 ms, faster than 5.01% of C++ online submissions for Word Search.
// Memory Usage: 7.5 MB, less than 20.31% of C++ online submissions for Word Search.

class Solution {
public:
    int xy[4][2] = {{0, 1},{1, 0},{-1, 0},{0, -1}};
    int w_len, n, m;
    bool dfs(int cur_x, int cur_y, bool visit[10][10], int dep, string word, vector<vector<char>>& board){
        if(dep == w_len) return true;
        for(int i = 0; i < 4; i++){
            int x = cur_x + xy[i][0];
            int y = cur_y + xy[i][1];
            if(x < 0 || n <= x || y < 0 || m <= y || visit[x][y]) continue;
            if(word[dep] == board[x][y]){
                visit[x][y] = true;
                bool copy_v[10][10] = {false,};
                for(int a = 0; a < n; a++)
                    for(int b = 0; b < m; b++)
                        copy_v[a][b] = visit[a][b];
                if(dfs(x, y, copy_v, dep+1, word, board)) return true;   
                visit[x][y] = false;
            }
        }
        return false;
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        w_len = word.size();
        n = board.size();
        m = board[0].size();
        
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                if(board[i][j] == word[0]){
                    bool visit[10][10] = {false,};
                    visit[i][j] = true;
                    if(dfs(i, j, visit, 1, word, board)) return true;
                }
        return false;
    }
};
