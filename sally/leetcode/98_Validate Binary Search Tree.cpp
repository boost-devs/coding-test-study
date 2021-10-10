// 98. Validate Binary Search Tree
// Runtime: 8 ms, faster than 90.29% of C++ online submissions for Validate Binary Search Tree.
// Memory Usage: 21.6 MB, less than 69.86% of C++ online submissions for Validate Binary Search Tree.


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        stack<pair<TreeNode*, pair<long long int, long long int>>> st;
        TreeNode* cur;
        st.push({root, {-pow(2, 31)-1, pow(2, 31)}});
        long long int max_num, min_num;
        
        while(!st.empty()){
            cur = st.top().first;
            min_num = st.top().second.first;
            max_num = st.top().second.second;
            
            if(cur->val <= min_num || cur->val >= max_num) return false;
            
            st.pop();
            if(cur->left != nullptr){
                if(cur->left->val >= cur->val) return false;
                st.push({cur->left, {min_num, cur->val}});
            }
            if(cur->right != nullptr){
                if(cur->right->val <= cur->val) return false;
                st.push({cur->right, {cur->val, max_num}});  
            }
        }
        return true;
    }
};
