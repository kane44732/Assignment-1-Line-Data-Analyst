N = int(input())
ai = [int(i) for i in input().split()]

op = -1
for j in set(ai):
    cnt = 0
    for k in ai:
        if j == k:
            cnt += 1
        else:
            cnt
    if cnt > N/2 :
        op = j
        break
print(op)
