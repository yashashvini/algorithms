/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSymmetric(struct TreeNode* root) {
    if(root){
        struct TreeNode* head1 = root->left;
        struct TreeNode* head2 = root->right;
        bool func(struct TreeNode* head1,struct TreeNode* head2){
            if(head1 == NULL && head2 == NULL){
                return true;
            }
            else if(head1 == NULL || head2 == NULL){
                return false;
            }
            else{
                if(head1->val == head2->val){
                    bool a1 = func(head1->left,head2->right);
                    bool a2 = func(head1->right,head2->left);
                    if(a1==false||a2==false){
                        return false;
                    }
                    else{
                        return true;
                    }
                }
                else{
                    return false;
                }
            }
        }
        return func(head1,head2);
    }
    return true;

}