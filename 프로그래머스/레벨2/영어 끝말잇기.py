# 프로그래머스 레벨2: 영어 끝말잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981

from collections import defaultdict

def solution(n, words):
    word_dict = defaultdict(int) 
    for i, word in enumerate(words):
        player = (i % n) + 1  
        turn = (i // n) + 1  
        
        if i > 0 and words[i - 1][-1] != word[0]:
            return [player, turn]
        
        if word_dict[word] > 0:
            return [player, turn]
        
        word_dict[word] += 1 

    return [0, 0] 

inputA = 3
inputB = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# expect: [3,3]
print(solution(inputA, inputB))
