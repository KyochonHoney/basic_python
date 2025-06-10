# 재귀알고리즘 Recursion
"""
시간복잡도 = T(n) = cn = O(n)
"""
import time

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

start_time = time.time()
print(sum(100))
end_time = time.time()
print(f"걸린 시간 : { end_time - start_time}")


