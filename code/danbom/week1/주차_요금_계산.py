def hhmm_to_int(s):
    return int(s[:2])*60+int(s[3:])

def cal(time, fees):
    if time <= fees[0]: 
        return fees[1]
      
    over = time - fees[0]
    if not over % fees[2] == 0:
      over += fees[2]
    return fees[1] + over // fees[2] * fees[3]

def solution(fees, records):
    time = [0]*10000
    entered = [-1]*10000
    result = []
    
    for r in records:
        hhmm, car, state = r.split()
        int_hhmm = hhmm_to_int(hhmm)
        car = int(car)
        
        if state == "IN":
            entered[car] = int_hhmm
        else:
            time[car] += int_hhmm - entered[car]
            entered[car] = -1
            
    for i in range(10000):
        if entered[i] != -1:
            time[i] += hhmm_to_int('23:59') - entered[i]
            
    for x in time:
        if x != 0:
            result.append(cal(x, fees))

    return result
  
