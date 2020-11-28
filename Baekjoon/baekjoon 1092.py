import sys
N = int(input())
limits = map(int, sys.stdin.readline().split()) # 크레인 별 무게 제한
M = int(input())
packages = map(int, sys.stdin.readline().split()) # 화물 별 무게

# 무게 제한과 화물 무게 전부 내림차순으로 정렬
limits = sorted(limits, reverse=True)
packages = sorted(packages, reverse=True)

# 무게 제한이 제일 높은 크레인도 제일 무거운 화물을 들 수 없는 경우
if packages[0] > limits[0] :
    print(-1)
    exit()

answer = 0
# 화물이 전부 옮겨질 때까지
while len(packages) > 0:
    answer += 1
    # 무게제한을 돌면서 옮길 수 있는 화물을 옮김
    for l in limits:
        for j in range(len(packages)):
            if l >= packages[j]: # 화물을 옮길 수 있으면
                del packages[j]
                break
print(answer)