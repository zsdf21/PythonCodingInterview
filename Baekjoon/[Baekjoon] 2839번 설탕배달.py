# 2839 설탕 배달
# (3 ≤ N ≤ 5000)

N = int(input())

## A1. Error in test case 3 -> 3으로만 나눠지는 경우 고려 X

# a = N//5

# if (N-5*a)%3 != 0:
#     print(-1)
# else:
#     b = (N-5*a)//3 
#     print(a+b)

######################################################
## A2. Error in test case 3, 5 -> 5로 나누면 안되는 경우 고려 X

# a = N//5
# if N%3==0 or N%5==0 or (N-5*a)%3==0:
#         b = (N-5*a)//3 
#         print(a+b)    
    
# else:
#     print(-1)


######################################################
## A3. 모든 경우의 수 정리 
# 1) 5로 다 담기는 경우
# 2) 최소의 3과 최대의 5로 담기는 경우
# 3) 3으로 다 담기는 경우
# 4) 예외 -1
    
a = 0

while N >= 0:
    if N % 5 == 0:
        a += N // 5
        print(a)
        break
    
    N -= 3
    a += 1
  
else:
    print(-1)