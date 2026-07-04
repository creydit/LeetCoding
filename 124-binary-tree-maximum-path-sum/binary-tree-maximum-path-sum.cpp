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
    int dfs(TreeNode* node, int &ans){
        if (node == NULL) return 0;
        int leftsum = max(0, dfs(node->left,ans)); //max (0,leftsum) to ignore negatives
        int rightsum = max(0, dfs(node->right, ans)); //max (0,rightsum) to ignore negatives
        ans = max(ans, node->val+leftsum+rightsum);
        return node->val + max(leftsum,rightsum);
    }
    int maxPathSum(TreeNode* root) {
        int ans = INT_MIN;
        dfs(root, ans);
        return ans;
    }
};