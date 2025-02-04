def fix_packages(packages:str) -> str:
  while '(' in packages:
    idx_ini = packages.rfind('(')
    idx_fi = packages[idx_ini+1:].index(')') + 1 + idx_ini

    reversed_word = packages[idx_ini+1:idx_fi][::-1]
    word_parentesis = packages[idx_ini:idx_fi+1]
    packages = packages.replace(word_parentesis,reversed_word)

  return packages