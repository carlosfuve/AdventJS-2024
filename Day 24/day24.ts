type TreeNode2 = {
    value: number;
    left?: TreeNode2;
    right?: TreeNode2;
} | null;

function isTreesSynchronized(tree1: TreeNode2, tree2: TreeNode2): [boolean, string] {
    if (!tree1 && !tree2) {
        return [true, ""];
    }

    function searchEqualTree(t1: TreeNode2, t2: TreeNode2): boolean {
        if (!t1 && !t2) {
            return true;
        }
        
        if (!t1 || !t2 || t1.value !== t2.value) {
            return false;
        }

        return searchEqualTree(t1.left ?? null, t2.right ?? null) &&
               searchEqualTree(t1.right ?? null, t2.left ?? null);
    }
    
    return [searchEqualTree(tree1, tree2), tree1 ? String(tree1.value) : ""];
}