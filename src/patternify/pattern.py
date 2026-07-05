def square(rows,pattern='*'):
    result = ''
    for i in range(rows):
        result += pattern*rows+'\n'
    return result

def hollow_square(rows,pattern='*',space=' '):
    if not space:return 'The space must be " " or any character not empty.'
    result = ''
    for i in range(1,rows+1):
        if i==1 or i==rows:
            result += pattern*rows+'\n'
        else:
            result += pattern+space*(rows-2)+pattern+'\n'
    return result

def left_triangle(rows,pattern='*'):
    result = ''
    for i in range(1,rows+1):
        result += pattern*i+'\n'
    return result

def hollow_left_triangle(rows,pattern='*',space=' '):
    if not space:return 'The space must be " " or any character not empty.'
    result = ''
    for i in range(1,rows+1):
        if i==1 or i==rows:result += pattern*i+'\n'
        else:result += pattern+space*(i-2)+pattern+'\n'
    return result

def right_triangle(rows,pattern='*'):
    result = ''
    for i in range(rows):
        result += ' '*(rows-i)+pattern*i+'\n'
    return result

def hollow_right_triangle(rows,pattern='*',space=' '):
    result = ''
    for i in range(1,rows+1):
        if i==1 or i==rows:result += ' '*(rows-i)+pattern*i+'\n'
        else:result += ' '*(rows-i)+pattern+space*(i-2)+pattern+'\n'
    return result

def pyramid(rows,pattern='*'):
    result = ''
    for i in range(1,rows+1):
        result += ' '*(rows-i)+(pattern*(2*i-1))+'\n'
    return result

def hollow_pyramid(rows,pattern='*',space=' '):
    if not space:return 'The space must be " " or any character not empty.'
    result = ''
    for i in range(1,rows+1):
        if i==1 or i==rows:result += ' '*(rows-i)+pattern*(2*i-1)+'\n'
        else:result += ' '*(rows-i)+pattern+space*(2*(i-1)-1)+pattern+'\n'
    return result

def inverted_pyramid(rows,pattern='*'):
    result = ''
    for i in range(rows):
        result += ' '*i+pattern*(2*rows-2*i-1)+'\n'
    return result

def hollow_inverted_pyramid(rows,pattern='*',space=' '):
    result = ''
    for i in range(rows):
        base = 2*rows-2*i-1
        if i==0 or i==rows-1:result += ' '*i+pattern*base+'\n'
        else:result += ' '*i+pattern+space*(base-2)+pattern+'\n'
    return result

def diamond(rows,pattern='*'):
    index = reverse = 0
    half = rows//2
    result = ''
    for i in range(rows):
        if i==half:
            reverse = 1
            if rows%2:
                result += pattern*(2*index+1)+'\n';index-=1;continue
            index-=1
        result += ' '*(half-index)+pattern*(2*index+1)+'\n'
        if reverse:index-=1
        else:index+=1
    return result

print(inverted_pyramid(7))
print(hollow_inverted_pyramid(7))
print(diamond(7))