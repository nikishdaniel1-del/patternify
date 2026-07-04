def left_triangle(rows,pattern='*',space=''):
    result = ''
    for i in range(1,rows+1):
        result += (pattern+space)*i+'\n'
    return result

def hollow_left_triangle(rows,pattern='*',space=''):
    result = ''
    for i in range(rows):
        if i==1 or i==rows:result += pattern*i+'\n'
        else:result += pattern+space*(i-2)+pattern+'\n'
    return result

def right_triangle(rows,pattern='*',space=''):
    result = ''
    for i in range(rows):
        result += space*(rows-i)+pattern*i+'\n'
    return result