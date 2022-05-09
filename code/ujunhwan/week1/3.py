import math

def feeCalc(totalTime):
    ret = BASIC_FEE
    totalTime -= BASIC_TIME
    
    if totalTime <= 0:
        return ret
    
    #[div, mod] = divmod(totalTime, UNIT_TIME)
    div = math.ceil(totalTime / UNIT_TIME)
    
    ret += div * UNIT_FEE
    return ret

def timeCalc(a, b):
    if a < b:
        a, b = b, a
    
    return a - b


def convert(time):
    [hour, minute] = time.split(':')
    hour = int(hour)
    minute = int(minute)
    return hour * 60 + minute


def solution(fees, records):
    answer = []
    
    global BASIC_TIME
    global BASIC_FEE
    global UNIT_TIME
    global UNIT_FEE
    
    [BASIC_TIME, BASIC_FEE, UNIT_TIME, UNIT_FEE] = fees
    
    car = [[0 for col in range(2)] for row in range(10000)]
    
    for record in records:
        [time, carId, state] = record.split(" ")
        carId = int(carId)
        time = convert(time) + 1
        
        if car[carId][0] == 0:
            car[carId][0] = time
        else:
            car[carId][1] += timeCalc(car[carId][0], time)
            car[carId][0] = 0
        
    for i in range(10000):
        if car[i][0] != 0:
            car[i][1] += timeCalc(car[i][0], 23*60+59 + 1)
        if car[i][1] != 0:
            answer.append(feeCalc(car[i][1]))
            
    return answer