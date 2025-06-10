# 최댓값 찾기
import time 

A = [1, 2, 3, 4, 50, 6, 7, 8, 9, 10]

def algorithm_array_max(A):
    currentMax = A[0]

    for i in range(1, len(A)):
        if currentMax < A[i]:
            currentMax = A[i]
    return currentMax

start_time = time.time()
print(algorithm_array_max(A))
end_time = time.time()
print(f"걸린 시간 : { end_time - start_time}")