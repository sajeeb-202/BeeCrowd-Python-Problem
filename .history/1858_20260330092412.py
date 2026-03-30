N = int(input())
arr = list(map(int, input().split()))
minimum_arr = min(arr)

for i in range(N):
    if arr[i] == minimum_arr:
        print(i +1)
        break