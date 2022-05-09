from itertools import permutations
def solution(n, nums, opers):
    op = []
    for i in range(4):
        for j in range(opers[i]):
            if i == 0:
                op.append('+')
            elif i == 1:
                op.append('-')
            elif i == 2:
                op.append('*')
            elif i == 3:
                op.append('/')
    
    op_list = list(set(permutations(op, n - 1)))
    # print(op_list)
    _max = -1000000001
    _min = 1000000001
    for p in op_list:
        temp = nums[0]
        for i in range(n - 1):
            if p[i] == '+': temp += nums[i + 1]
            elif p[i] == '-': temp -= nums[i + 1]
            elif p[i] == '*': temp *= nums[i + 1]
            elif p[i] == '/':
                if temp < 0:
                    temp *= -1
                    temp = temp // nums[i + 1]
                    temp *= -1
                else:
                    temp = temp //nums[i+1]
        if _max < temp:
            _max = temp
        if _min > temp:
            _min = temp        
            
    print(_max)
    print(_min)


    
n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))

solution(n,nums,opers)