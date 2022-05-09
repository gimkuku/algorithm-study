# p를 문자열 2개로 분리
def split(p):
    cnt = 0
    index =0
    for index in range(len(p)):
        if p[index] == ')':
            cnt = cnt +1
        else : 
            cnt = cnt -1
        if cnt == 0:
            break
    return p[:index+1],p[index+1:]

# u가 올바른 괄호 문자열인지 확인
def check(u):
    stack = []
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            # 스택이 비어있으면               
            if stack == []:
                return False
            stack.pop()
    return True   

        
def solution(p):
    if len(p) == 0:
        return ""

    # u, v 로 분리
    u,v = split(p)
    
    if (check(u)):
        return u + solution(v)
    else : 
        ans = '('
        ans = ans + solution(v)
        ans = ans + ')'
        # 앞뒤 자르고 괄호 바꾸기        
        u = u[1:len(u)-1]
        ans = ans + u[:: -1]
           
    return ans