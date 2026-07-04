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


# print(square(5))
# print(hollow_square(8,space='#'))
# print(left_triangle(6))
# print(hollow_left_triangle(8))
# print(right_triangle(7))
# print(hollow_right_triangle(8,space='#'))
# print(pyramid(8,'#'))
# print(hollow_pyramid(8,space='#'))