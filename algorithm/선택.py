# 선택(Selection) 알고리즘 8강부터
"""
Quick Select
Median of medians

입력 : n 개의 값과 K값 ( 1 <= k <= n)
출력: k번째로 작은 입력값
목표 : 비교횟수 최소화
"""

#최댓값 찾기 O(n) -> O(1/2n)
import time

a = [1,2,3,4,5,6,7,8,9,10]
K = 6
def select_maximum():
    max = -1000
    for i in range(1, len(a)):
        if max < i:
            max = i
    return max

start_time = time.time()
print(select_maximum())
end_time = time.time()
print(f"걸린 시간 : { end_time - start_time}")


#Quick Select
"""
1. p를 고른다 : pivot
2. O(n-1) 
    A = {p보다 작은 값}
    B = {P보다 큰 값}
    M = {P와 같은 값}
3.  if |A| > K :
        A에서 K번째 작은 값 => M U B에는 없음 -> 재귀
    elif |A| + |M| < k :
        B에서 찾아야 함
    else:
        return P
"""

def quick_select(L, K):
    P = L[0]
    A,B,M = [],[],[]
    # 방법 1
    for x in L :
        if P > x :
            A.append(x)
        elif P < x : 
            B.append(x)
        else: 
            M.append(x)
    #방법2
    """
    if len(A) > K : 
        quick_select(A, K)
    elif len(A) + len(M) < K :
        quick_select(B, K)
    else:
        return P
    

start_time = time.time()
print(quick_select(a, K))
end_time = time.time()
print(f"걸린 시간 : { end_time - start_time}")
"""

# MoM ( Median of Medians ) 알고리즘
"""
L : 배열
mom(L,K):
    1. 5개씩 group
    2. 각 그룹의 중앙값 (median)
"""