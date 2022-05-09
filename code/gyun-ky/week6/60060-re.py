from bisect import bisect_left, bisect_right
# 검색키워드는 중복이 될수 있다는 조건을 고려하여 key:잘려진단어 + 키워드길이 / value:일치하는 word 개수
dic_by_s_word = dict()
dic_by_e_word = dict()

# 각 word를 길이 기준
dic_by_len = dict()
dic_by_len_reverse = dict()


# 앞쪽 단어인 경우 개수 찾기
def search_start(keyword, kl, start, end):
    
    cnt = bisect_right(dic_by_len[kl], end) - bisect_left(dic_by_len[kl], start)
    
    dic_by_s_word[keyword] = cnt
    return cnt


# 앞쪽 단어인 경우 개수 찾기
def search_end(keyword, kl, start, end):
    
    cnt = bisect_right(dic_by_len_reverse[kl], end) - bisect_left(dic_by_len_reverse[kl], start)
    
    dic_by_e_word[keyword] = cnt
    return cnt
        

def solution(words, queries):
    global dic_by_len, dic_by_len_reverse
    # 노래 가사의 단어들 중 특정 키워드가 몇개 포함? -> 
    # 100,000 * 100,000 > 1e9  ---> 다 대입하여 비교는 불가다
    
    # 가사단어 길이 : 10,000
    # dictionary로 풀자
    
    answer = []
    
    # 딕셔너리에 key-word길이 : value-word개수 만들기
    for w in words:
        l = len(w)
        if l in dic_by_len:
            dic_by_len[l].append(w)
            dic_by_len_reverse[l].append(w[::-1])
        else:
            dic_by_len[l] = [w]
            dic_by_len_reverse[l] = [w[::-1]]
    
    # 정렬
    for d in dic_by_len.values():
        d.sort()
    for d in dic_by_len_reverse.values():
        d.sort()
    
    for keyword in queries:
        
        # 키워드 길이
        kl = len(keyword)
        
        # 키워드의 길이가 word들의 길이와 동일한 것이 없는 경우 --> 길이가 다르면 아예 매칭 불가능!!
        if kl not in dic_by_len:
            answer.append(0)
            continue
        
        # 키워드가 모두 ?인 경우
        if keyword[0] == '?' and keyword[-1] == '?':
            answer.append(len(dic_by_len[kl]))
            continue
        
        # 처음으로 ?가 나오는 위치 찾기
        wild_start_pos = keyword.find('?')
        
        
        # 물음표가 접두사인 경우 - 물음표가 앞쪽에 몰린 경우
        if wild_start_pos == 0:
            
            # 먼저 dictionary에 있는지 검증
            if keyword in dic_by_e_word:
                answer.append(dic_by_e_word[keyword])
                continue
            # 길이가 같은 것들중에서 찾기
            answer.append(search_end(keyword, kl, keyword[::-1].replace('?', 'a'), keyword[::-1].replace('?', 'z')))
        # 물음표가 접미사인 경우 - 물음표가 뒤쪽에 몰린 경우
        else:

            # 먼저 dictionary에 있는지 검증
            if keyword in dic_by_s_word:
                answer.append(dic_by_s_word[keyword])
                continue
            # 길이가 같은 것들중에서 찾기
            answer.append(search_start(keyword, kl, keyword.replace('?', 'a'), keyword.replace('?', 'z')))
                        
    
    
    return answer