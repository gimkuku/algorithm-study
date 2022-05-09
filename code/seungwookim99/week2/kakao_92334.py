def solution(id_list, report, k):
    answer = []
    report_dict = {}
    
    # 신고 정보 딕셔너리 초기화
    for i in id_list:
        tmp = dict()
        tmp['count'] = 0  # 누적 신고 횟수
        tmp['report_from'] = [] # 나를 신고한 사람
        tmp['report_to'] = [] # 내가 신고한 사람
        report_dict[i] = tmp
        
    for rep in report:
        r_from, r_to = rep.split(' ')
        # 처음 신고한다면
        if r_to not in report_dict[r_from]['report_to']:
            report_dict[r_from]['report_to'].append(r_to)
            report_dict[r_to]['report_from'].append(r_from)
            report_dict[r_to]['count'] += 1
    
    # 정지당한 계정 추출
    blocked_list = []
    for i, info in report_dict.items():
        if info['count'] >= k:
            blocked_list.append(i)
    
    # 집합으로 만듬
    blocked_set = set(blocked_list)
    
    # 발송할 메일 횟수 계산
    for _, info in report_dict.items():
        report_to = set(info['report_to'])
        answer.append(len(report_to&blocked_set)) # 교집합 원소 개수
    return answer