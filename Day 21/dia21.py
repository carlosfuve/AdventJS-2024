def tree_height(tree):
  if tree == None:
    return 0
  
  return 1 + max(tree_height(tree['left']),tree_height(tree['right']))



tree = {
  'value': '🎁',
  'left': {
    'value': '🎄',
    'left': {
      'value': '⭐',
      'left': None,
      'right': None
    },
    'right': {
      'value': '🎅',
      'left': None,
      'right': None
    }
  },
  'right': {
    'value': '❄️',
    'left': None,
    'right': {
      'value': '🦌',
      'left': None,
      'right': None
    }
  }
}

print(tree_height(tree))