// 242. Valid Anagram
// Runtime: 10 ms, faster than 59.04 % of C++ online submissions for Valid Anagram.
// Memory Usage : 7.4 MB, less than 7.00 % of C++ online submissions for Valid Anagram.

class Solution {
public:
    bool isAnagram(string s, string t) {
        int alpha[26] = { 0, };
        int s_len = s.size();
        int t_len = t.size();
        for (int i = 0; i < s_len; i++) alpha[s[i] - 'a']++;
        for (int i = 0; i < t_len; i++) alpha[t[i] - 'a']--;
        for (int i = 0; i < 26; i++)
            if (alpha[i] != 0) return false;
        return true;
    }
};