def checkInputs(patterns,space):
    result = ''
    if len(patterns)!=len(space):result = 'The Length of both Pattern and the Space should be equal.'
    elif not space:result = 'The space must be " " or any character not empty character.'
    return result

def square(rows,pattern='*'):
    result = ''
    for i in range(rows):result += pattern*rows+'\n'
    return result[:-1]

def hollow_square(rows,pattern='*',space=' '):
    check = checkInputs(pattern,space)
    if check:return check
    result = ''
    for i in range(1,rows+1):
        if i==1 or i==rows:result += pattern*rows+'\n'
        else:result += pattern+space*(rows-2)+pattern+'\n'
    return result[:-1]

def left_triangle(rows,pattern='*'):
    result = ''
    for i in range(1,rows+1):
        result += pattern*i+'\n'
    return result[:-1]

def hollow_left_triangle(rows,pattern='*',space=' '):
    check = checkInputs(pattern,space)
    if check:return check
    result = ''
    for i in range(1,rows+1):
        if i==1 or i==rows:result += pattern*i+'\n'
        else:result += pattern+space*(i-2)+pattern+'\n'
    return result[:-1]

def right_triangle(rows,pattern='*'):
    result = ''
    for i in range(rows):result += ' '*(rows-i)+pattern*i+'\n'
    return result[:-1]

def hollow_right_triangle(rows,pattern='*',space=' '):
    check = checkInputs(pattern,space)
    if check:return check
    result = ''
    for i in range(1,rows+1):
        if i==1 or i==rows:result += ' '*len(pattern)*(rows-i)+pattern*i+'\n'
        else:result += ' '*len(pattern)*(rows-i)+pattern+space*(i-2)+pattern+'\n'
    return result[:-1]

def pyramid(rows,pattern='*'):
    result = ''
    for i in range(1,rows+1):result += ' '*(rows-i)+(pattern*(2*i-1))+'\n'
    return result[:-1]

def hollow_pyramid(rows,pattern='*',space=' '):
    check = checkInputs(pattern,space)
    if check:return check
    result = ''
    for i in range(1,rows+1):
        if i==1 or i==rows:result += ' '*len(pattern)*(rows-i)+pattern*(2*i-1)+'\n'
        else:result += ' '*len(pattern)*(rows-i)+pattern+space*(2*(i-1)-1)+pattern+'\n'
    return result[:-1]

def inverted_pyramid(rows,pattern='*'):
    result = ''
    for i in range(rows):result += ' '*i+pattern*(2*rows-2*i-1)+'\n'
    return result[:-1]

def hollow_inverted_pyramid(rows,pattern='*',space=' '):
    check = checkInputs(pattern,space)
    if check:return check
    result = ''
    for i in range(rows):
        base = 2*rows-2*i-1
        if i==0 or i==rows-1:result += ' '*len(pattern)*i+pattern*base+'\n'
        else:result += ' '*len(pattern)*i+pattern+space*(base-2)+pattern+'\n'
    return result[:-1]

def diamond(rows,pattern='*'):
    index = reverse = 0
    half = rows//2
    result = ''
    for i in range(rows):
        if i==half:
            reverse = 1
            if rows%2:result += pattern*(2*index+1)+'\n';index-=1;continue
            index-=1
        result += ' '*len(pattern)*(half-index)+pattern*(2*index+1)+'\n'
        if reverse:index-=1
        else:index+=1
    return result[:-1]

def hollow_diamond(rows,pattern='*',space=' '):
    check = checkInputs(pattern,space)
    if check:return check
    result = ''
    index = reverse = 0
    half = rows//2
    for i in range(rows):
        if i==half:
            reverse = 1
            if rows%2:
                result += pattern+space*(2*index-1)+pattern+'\n';index-=1;continue
            index-=1
        if i==0 or i==rows-1:result += ' '*len(space)*(half-index)+pattern+'\n'
        else:result += ' '*len(space)*(half-index)+pattern+space*(2*index-1)+pattern+'\n'
        if reverse:index-=1
        else:index+=1
    return result[:-1]

def butterfly(rows,pattern='*'):
    result = ''
    reverse = 0
    index = 1
    half = rows//2
    for i in range(rows):
        if i==half:
            reverse=1;index -= 1
            if rows%2:result += (pattern*rows).strip()+'\n';continue
        result += (pattern*index+' '*len(pattern)*(rows-(2*index))+pattern*index).strip()+'\n'
        index += -1 if reverse else 1
    return result[:-1]

def hollow_butterfly(rows,pattern='*',space=' '):
    check = checkInputs(pattern,space)
    if check:return check
    result = ''
    return result

# print(hollow_square(6,'# ','~ '))
# print(diamond(7,pattern='#  '))
# print(hollow_diamond(7,pattern='*  ',space='~  '))