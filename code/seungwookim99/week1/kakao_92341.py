def calc_fee(table, fees):
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    
    answer = []
    for info in table:
        time = info[1]['time']
        if time <= default_time:
            answer.append(default_fee)
        else:
            if (time - default_time) % unit_time != 0:
                time = (time - default_time) // unit_time + 1
            else:
                time = (time - default_time) // unit_time
            answer.append(default_fee + time * unit_fee)
    return answer

def convert_to_minute(hhmm):
    splited_hhmm = hhmm.split(":")
    hour = splited_hhmm[0]
    minute = splited_hhmm[1]
    return int(hour)*60 + int(minute)

def solution(fees, records):
    answer = []
    table = dict()
    end_time = convert_to_minute("23:59")
    for record in records:
        # 데이터 추출
        data = record.split(" ")
        time = convert_to_minute(data[0])
        car_number = data[1]
        is_in = True if data[2] == "IN" else False
        
        # 입차 / 출차 여부 확인
        if is_in:
            # 처음 입차한 경우
            if car_number not in table:
                info = dict()
                info['in_time'] = time # 입차 시각(분)
                info['is_in'] = is_in # 현재 입차 여부
                info['time'] = 0 # 누적 시간
                table[car_number] = info
            # 두 번 이상 입차한 경우
            else:
                table[car_number]['in_time'] = time
                table[car_number]['is_in'] = is_in
        else:
            table[car_number]['is_in'] = is_in
            table[car_number]['time'] += time - table[car_number]['in_time']
            pass
        
    # 23:59까지 입차한 차량 확인 후 시간 계산
    for car_number in table:
        if table[car_number]['is_in']:
            table[car_number]['time'] += end_time - table[car_number]['in_time']
    
    # 차량 번호대로 정렬된 튜플 배열 생성
    sorted_tuple_table = sorted(table.items())
    
    # 주차 요금 계산
    answer = calc_fee(sorted_tuple_table, fees)
        
    return answer