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
    TreeNode* last = NULL;
    void flatten(TreeNode* root) {
        if (!root)
            return;
        TreeNode* right = root -> right;
        TreeNode* left = root -> left;
        root -> left = NULL;
        if (last)
        {
            last -> right = root;
        }
        last = root;
        flatten(left);
        flatten(right);
    }
};