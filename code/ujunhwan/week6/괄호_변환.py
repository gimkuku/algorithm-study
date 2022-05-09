def solution(w):
    length = len(w)
    
    def check(s):
        length = len(s)
        is_right = True
        left, right = 0, 0
        for i in range(length):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left < right:
                is_right = False
                
        return is_right
    
    def divide(s):
        length = len(s)
        left, right = 0, 0
        for i in range(length):
            if w[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                u = w[:i+1]
                v = w[i+1:]
                return u, v
   	
    # check right string
    #if check(w):
    #    return w
    
    # level 1
    if w == '':
        return ''
    
    # level 2
    left, right = 0, 0
    u, v = divide(w)
    
    # level 3
    if check(u):
        return u + solution(v)
    
    # level 4
    else:
        u = u[1:-1]
        new_u = ''
        for i in range(len(u)):
            if u[i] == '(':
                new_u += ')'
            else:
                new_u += '('
                
        return '(' + solution(v) + ')' + new_u
    
    return w