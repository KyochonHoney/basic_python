#분할정복법(Divide & Conquer) : 큰 문제를 작은 문제로 분할해 재귀적으로 해결

import time

#피보나치 ( Fibonacci )
"""
F(n) = F(n-1) + f(n-2)
-> O(K의 n승) n이 클수록 안 좋음
"""
def fibo1(n):
    if(n == 1 or n == 0): 
        return n
    return fibo1(n - 1) + fibo1(n - 2)

# O(logN) -> 정확히 못 들음..
def fibo2(n):
    return 1

# 큰 두 수의 곱셈 : 분할정복 알고리즘(Karatswba's Algorithm)
"""
이진탐색(Binary Search)
    A = [2, 3, 9, 10, 17, 28, 31, 45] => 오름차순 정렬 
    뽑는 수가 K = 31
    가장 간단한 방법은 맨 앞 혹은 맨 뒤에서 비교 시작 --> O(n)
    이진탐색 점화식 =>
    T(n) = T(n/2) + c
    T(n) = 2T(n/2) + cn { BEST CASE }
"""
def bs(A, a, b, k):
    if a > b:
        return -1
    m = (a + b) / 2
    if A[m] == k:
        return m
    elif A[m] > k:
        return bs(A, a, m-1, k)
    else:
        return bs(A, m+1, b, k)