# GCD ( 최대공약수 구하는 알고리즘 )
import time

def gcd(a,b):
    while(a != 0 and b != 0):
        if(a > b):
            a %= b
        else:
            b %= a
    return a+b

start_time = time.time()
print(gcd(2,100000))
end_time = time.time()
print(f"걸린 시간 : { end_time - start_time}")