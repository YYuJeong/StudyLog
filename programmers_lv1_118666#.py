def solution(survey, choices):
    answer = ''
    type_dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M': 0, 'A':0, 'N':0}
    
    choice_score = {
        1 : 3, # 매우 비동의
        2 : 2, # 동의
        3 : 1, # 약간 동의
        4 : 0, # 모르겠음
        5 : 1, # 약간 동의
        6 : 2, # 동의
        7 : 3  # 매우 동의
    }
    
    for type_, choice in zip(survey, choices):       
        if choice < 4:
            type_dic[type_[0]] += choice_score[choice]       
        elif choice >= 5:
            type_dic[type_[1]] += choice_score[choice]
    
    type_keys = list(type_dic.keys())
    for left, right in zip(type_keys[::2], type_keys[1::2]):
        if type_dic[left] >= type_dic[right]:
            answer += left
        else:
            answer += right

    return answer