def is_trees_synchronized(tree1, tree2):
    if not tree1 and not tree2:
        return [True, ""]
    

    def search_equal_tree(tree1, tree2):
        if not tree1 and not tree2:
            return True
        
        if not 'left' in tree1:
            return tree1['value'] == tree2['value']
        else:
            return tree1['value'] == tree2['value'] and search_equal_tree(tree1['left'],tree2['right']) and search_equal_tree(tree1['right'],tree2['left'])
  

    return [search_equal_tree(tree1, tree2), tree1['value']]

