# 친구
"""
# 문제
지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 
가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다. 
어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, 
A와 친구이고, B와 친구인 C가 존재해야 된다. 
여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 
가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.
A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.

# 입력
첫째 줄에 사람의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다.

# 출력
첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력한다.
"""

import sys
N = int(sys.stdin.readline())
graph = [[map(int, sys.stdin.readline().strip())] for _ in range(N)]

fs = [[0] * N for _ in range(N)]    # 친분 여부 파악 arr(친구 = 1, 친구X = 0)

for k in range(N):                  # i, j간 친구 관계 파악
    for i in range(N):
        for j in range(N):          # k는 제 3자를 통한 i, j 친구 여부 파악 위함(2-hop)
            
            if i == j:              # 동일 인물 제외
                continue
                     
            # 1-hop 친구 or (k와 연결된) 2-hop 친구
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[j][k] =='Y'):
                fs[i][j] = 1        # fs 1로 수정

ans = 0
for i in range(N):
    ans = max(sum(fs[i]), ans)   
print(ans)