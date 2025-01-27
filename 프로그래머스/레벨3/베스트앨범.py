# 베스트앨범

from collections import defaultdict

def solution(genres, plays):
    
    answer = []
    
    p_dict = defaultdict(list)
    s_dict = defaultdict(int)
    
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        t = (i, p, g)
        p_dict[g].append(t)
        s_dict[g] += p
        
    for k, v in sorted(list(s_dict.items()), key=lambda x: x[1], reverse=True):
        for i, _, _ in sorted(p_dict[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer