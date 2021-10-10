// 143. Reorder List
// Runtime: 932 ms, faster than 5.09% of C++ online submissions for Reorder List.
// Memory Usage: 17.8 MB, less than 76.07% of C++ online submissions for Reorder List.

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
    void reorderList(ListNode* head) {
        ListNode* cur = head;
        
        while(cur->next != nullptr){
            if(cur->next == nullptr) break;
            if(cur->next->next == nullptr) break;
            
            ListNode* LastNode = cur;
            ListNode* BeforeLastNode;
            
            while(LastNode->next != nullptr){
                BeforeLastNode = LastNode;
                LastNode = LastNode->next;
            }
            
            LastNode->next = cur->next;
            cur->next = LastNode;
            cur = LastNode->next;
            BeforeLastNode->next = nullptr;
            
            if(cur->next == nullptr) break;
            if(cur->next->next == nullptr) break;
        }
    }
};