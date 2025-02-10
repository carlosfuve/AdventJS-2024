def remove_snow(s: str) -> str:
    stack = []
    for char in s:
      if stack and stack[-1] == char:
          stack.pop()
      else:
          stack.append(char)
    
    return ''.join(stack)

#Con indices daba 4 estrellas
def remove_snow2(s: str) -> str:
  i = 0
  n = len(s) - 1
  while True:
    if i >= n:
      break
    
    if s[i] == s[i+1]:
        s = s[:i]+s[i+2:]
        i = 0
        n = len(s) - 1
    else:
      i+=1

  return s

print(remove_snow('zxxzoz'))
print(remove_snow('zzz'))
print(remove_snow('aaabbaacc'))