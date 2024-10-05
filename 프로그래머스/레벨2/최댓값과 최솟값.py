# 프로그래머스: 레벨2 최댓값과 최솟값
# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
	l = list(map(int, s.split()))
	mi = min(l)
	ma = max(l)
	return str(mi) + " " + str(ma)