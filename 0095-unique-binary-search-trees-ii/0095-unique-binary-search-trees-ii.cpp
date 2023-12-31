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
    vector<TreeNode*> generateTrees(int n) {
        return helper(1,n);
        
    }
    vector<TreeNode*> helper(int start, int end){
        vector<TreeNode*> list;
        
        if(start>end){
            list.push_back(nullptr);
            return list;
        }
        
        if(start==end){
            list.push_back(new TreeNode(start));
            return list;
        }
        for(int i=start;i<=end;i++){
            vector<TreeNode*> leftPossibleTrees = helper(start,i-1);
            vector<TreeNode*> rightPossibleTrees = helper(i+1,end);
            for(TreeNode* &lRoot : leftPossibleTrees){
                for(TreeNode* &rRoot : rightPossibleTrees){
                    TreeNode* root = new TreeNode(i);
                    root->left = lRoot;
                    root->right = rRoot;
                    list.push_back(root);
                }
            }
        }
        return list;
    }
};