

# 2단계 : 문자열 w를 u,v로 분리하는 메소드
def phase2(p):
    
    open_cnt = 0
    close_cnt = 0
    result = []
    q = []
    for i in range(len(p)):
        print(p[i])
        if p[i] == '(':
            open_cnt += 1
            q.append('(')
        else:
            close_cnt += 1
            q.append(')')
        # 균현잡혔다 : 여는 괄호와 닫는 괄호수가 같다
        if open_cnt == close_cnt:
            result.append(''.join(q))
            result.append(p[i+1:])
            return result
    
    # for문을 다 돌 때까지 return 안했다? 그건 균형잡힌 문자열이 없는거다!
    result = ['', p]
            
    return result


# 올바른 문자열인지 판단
def check_right(u):
    stack = []
    # stack 사용하여 괄호 짝 찾기
    for i in range(len(u)):
        if u[i] == '(':
            stack.append('(')
        else:
            if stack:
                pop = stack.pop()
                if pop != '(':
                    stack.append(pop)
                    stack.append(u[i])
            # ')'가 나왔는데 stack에 아무것도 없다면 어차피 짝 안 맞는 것!
            else:
                return False
    # 문자열 다 살펴 봤는데 stack이 비었으면 괄호 짝 다 찾은 것!
    if len(stack) == 0:
        return True
    else:
        return False
            
    
# 절차 진행
def process(p):
    
    # 만약 빈칸이 들어오면 그냥 빈칸을 뱉어주어야 result에 ''이 붙는다
    if p == '':
        return p
    # u, v 뱉어냄
    u, v = phase2(p)
    # u가 올바른 괄호문자열인지 체크
    ## 올바른 문자열이면
    if check_right(u):
        result = u + process(v)
        ## u 뒤에 이어 붙일 재귀의 return 값
        return result
    
    # 올바른 문자열이 아니라면 
    else:
        ## v에 대해서 process 처리 (1단계부터 다시 처리)
        new_v = process(v)
        # u의 양쪽 괄호 지워주기
        sliced_u = u[1:-1]
        # 결과 양쪽에 괄호, 가공된 v값 가운데에 넣어주기
        result = '(' + new_v + ')'
        # u값들 괄호 반전 처리해주기
        for i in range(len(sliced_u)):
            if sliced_u[i] == '(':
                result+= ')'
            else:
                result+= '('
        return result
            

def solution(p):
    
    # 균형잡힌 괄호 문자열 - ( 개수와 ) 의 개수가 같음 / 올바른 괄호 문자열 - ()의 짝이 맞아야 함
    
    answer = process(p)

    return answer