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
    //Algorithm
    // first assign newList -> val with ptr1 -> val or ptr2 -> val 
    //      and newList -> next = null
    //      ptr1 = ptr
    //while ptr1 or ptr2
    //  if ptr1 -> val < ptr2 -> val
    //      insert ptr1 at the end of the new node
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* newList = new ListNode();
        ListNode* ptr1 = list1;
        ListNode* ptr2 = list2;
        if (!ptr1)
        return ptr2;
        else if (!ptr2)
        return ptr1;
        if(ptr1 -> val < ptr2 -> val)
        {
            newList -> val = ptr1 -> val;
            ptr1 = ptr1 -> next;
            newList -> next = NULL;
        }
        else
        {
            newList -> val = ptr2 -> val;
            ptr2 = ptr2 -> next;
            newList -> next = NULL;
        }
        ListNode *curr = newList;
        while (ptr1 && ptr2)
        {
            if(ptr2 -> val < ptr1 -> val)
            {
                curr -> next = new ListNode();
                curr -> next -> val = ptr2 -> val;
                curr = curr -> next;
                ptr2 = ptr2 -> next;
            }
            else
            {
                curr -> next = new ListNode();
                curr -> next -> val = ptr1 -> val;
                curr = curr -> next;
                ptr1 = ptr1 -> next;
            }
        }
        if (!ptr1)
        {
            curr -> next = ptr2;
        }
        else
        curr -> next = ptr1;
        return newList;
    }
};
