def create_frame(names: list[str]) -> str:
    max_len = max([len(name) for name in names]) + 4

    res = '*'*max_len + "\n"
    for name in names:
        name = '* ' + name
        spaces = ' '*(max_len-1 - len(name)) 
        res += name + spaces + '*\n'

    res += '*'*max_len
    return res