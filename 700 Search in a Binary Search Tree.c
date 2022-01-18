/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* searchBST(struct TreeNode* root, int val){
    if(!root) return NULL;
    if(val>root->val) return searchBST(root->right,val);
    else if(val<root->val) return searchBST(root->left,val);
    else return root;
}

Success
Details 
Runtime: 49 ms, faster than 11.70% of C online submissions for Search in a Binary Search Tree.
Memory Usage: 15.4 MB, less than 7.38% of C online submissions for Search in a Binary Search Tree.
