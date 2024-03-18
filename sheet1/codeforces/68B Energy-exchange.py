n, k = map(int, input().split())
k /= 100
# k = 1 - k
arr = list(map(int, input().split()))
arr.sort(reverse=True)

def possible(mid, k):
    sur = 0.0
    for i in range(len(arr)):
        val = arr[i] + 0.0
        # if val == mid:
        #     continue
        if val >= mid:
            sur += (val - mid) * (1 - k)
        elif val < mid:
            if sur + val < mid:
                return False
            sur -= (mid - val)
    return True
l, r = arr[n-1] + 0.0 , sum(arr)/n + 0.0
# print(r)
ans = l
if n == 1:
    print(arr[0] + 0.0)
else:
    while l <= r:
        mid = l + (r - l) / 2
        # print(l, r, mid)
        if possible(mid, k):
            # print(mid)
            ans = mid
            l = mid + 0.0000001
        else:
            r = mid - 0.0000001
    print(ans)