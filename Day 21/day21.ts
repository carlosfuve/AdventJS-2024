type TreeNode = {
    left: TreeNode | null;
    right: TreeNode | null;
};

function treeHeight(tree: TreeNode | null): number {
    if (tree === null) {
        return 0;
    }
    
    return 1 + Math.max(treeHeight(tree.left), treeHeight(tree.right));
}