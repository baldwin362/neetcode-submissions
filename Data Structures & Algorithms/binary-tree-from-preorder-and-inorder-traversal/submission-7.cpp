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

using namespace std;

class Solution {
public:
    int find_index(const vector<int>& v, int value) {
        for (int i = 0; i < (int)v.size(); i++) {
            if (v[i] == value) {
                return i;
            }
        }
        // Should never happen if inputs are valid:
        // preorder & inorder are guaranteed to match.
        return 0;
    }

    vector<int> slice(const vector<int>& v, int start, int end_exclusive) {
        // Assumes 0 <= start <= end_exclusive <= v.size()
        return vector<int>(v.begin() + start, v.begin() + end_exclusive);
    }

    // Note: pass vectors BY VALUE here (copies) so we can pass temporaries.
    TreeNode* buildTree(vector<int> preorder, vector<int> inorder) {
        if (preorder.empty() || inorder.empty()) {
            return nullptr;
        }

        int rootVal = preorder[0];
        TreeNode* root = new TreeNode(rootVal);

        int mid = find_index(inorder, rootVal);

        // Left subtree
        vector<int> leftPre  = slice(preorder, 1, 1 + mid);   // preorder[1 : mid+1]
        vector<int> leftIn   = slice(inorder, 0, mid);        // inorder[0 : mid]

        // Right subtree
        vector<int> rightPre = slice(preorder, 1 + mid, (int)preorder.size()); // preorder[mid+1 : ]
        vector<int> rightIn  = slice(inorder, mid + 1, (int)inorder.size());   // inorder[mid+1 : ]

        root->left  = buildTree(leftPre, leftIn);
        root->right = buildTree(rightPre, rightIn);

        return root;
    }
};
