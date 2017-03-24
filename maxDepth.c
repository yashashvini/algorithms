/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    if(root){
        int left = maxDepth(root->left) + 1;
        int right = maxDepth(root->right) + 1;
        if(left > right){
            return left;
        }
        else{
            return right;
        }
    }
    return 0;
}