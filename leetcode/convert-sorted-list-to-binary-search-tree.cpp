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
    TreeNode* sortedListToBST(ListNode* head) {
        if (!head)
        {
            return NULL;
        }
        ListNode* dummy = new ListNode();
        dummy -> next = head;
        TreeNode* treeHead = new TreeNode();
        ListNode *slow = head, *fast = head, *beforeSlow = dummy;
        while (fast && fast -> next)
        {
            beforeSlow = slow;
            slow = slow -> next;
            fast = fast -> next -> next;
        }

        beforeSlow -> next = NULL;

        treeHead -> val = slow -> val;
        treeHead -> left = sortedListToBST(dummy -> next);
        treeHead -> right = sortedListToBST(slow -> next);
        // cout<<treeHead -> val<<" ";
        return treeHead;
    }
};