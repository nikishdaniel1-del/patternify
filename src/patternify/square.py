def square(rows,pattern='*',space=''):
    result = ''
    for i in range(rows):
        result += pattern*rows+'\n'
    return result

def hollow_square(rows,pattern='*',space=''):
    result = ''
    for i in range(1,rows+1):
        if i==1 or i==rows:
            result += pattern*rows+'\n'
        else:
            result += pattern+space*(rows-2)+pattern+'\n'
    return result