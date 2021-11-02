/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        // cout << "-------\n";
        vector<int> result;
        ListNode* cur = head;
        ListNode* nex = head->next;
        
        int bef_val = -1;
        int nex_val = nex->val;
        int cur_val = cur->val;
        
        int ind = 0;
        while(nex != nullptr){
            // 이전이 없음
            if(bef_val == -1){
                 bef_val = cur->val;
                if(cur->next == nullptr) break;
                cur = cur->next;
                nex = cur->next;
                ind++;
                continue;
            }
            // 다음이 없음
            if(nex == nullptr)
                break;
            
            cur_val = cur->val;
            nex_val = nex->val;
            
            
            // check max
            if(bef_val < cur_val && cur_val > nex_val)
                result.push_back(ind);

            // check min
            if(bef_val > cur_val && cur_val < nex_val)
                result.push_back(ind);
                
            bef_val = cur->val;
            if(cur->next == nullptr) break;
            cur = cur->next;
            nex = cur->next;
            
            ind++;
        }
        
        // make return values
        vector<int> ret;
        if(result.size() < 2){
            ret.push_back(-1);
            ret.push_back(-1);
        }
        else{
            int res_len = result.size();
            int min_val = 200000;
            for(int i = 0; i < res_len-1; i++)
                min_val = min(min_val, result[i+1] - result[i]);
            ret.push_back(min_val);
            ret.push_back(result[res_len - 1] - result[0]); // max
        }
        
        return ret;
    }
};