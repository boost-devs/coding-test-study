// 1143. Longest Common Subsequence
// Runtime: 16 ms, faster than 65.32% of C++ online submissions for Longest Common Subsequence.
// Memory Usage: 10.7 MB, less than 54.96% of C++ online submissions for Longest Common Subsequence.

class Solution {
public:
    
    int longestCommonSubsequence(string text1, string text2) {
        // variables
        text1 = ' ' + text1;
        text2 = ' ' + text2;
        int arr[1002][1002] = {0,};
        int len1 = text1.size();
        int len2 = text2.size();
        
        for(int i = 1; i < len1; i++)
            for(int j = 1; j < len2; j++){
                if(text1[i] == text2[j]) arr[i][j] = arr[i-1][j-1] + 1;
                else arr[i][j] = max(arr[i-1][j], arr[i][j-1]);
            }
        
        return arr[len1-1][len2-1];
    }
};