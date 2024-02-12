t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    arr = []
    for j in range(n):
        arr.append(int(s[j]))
    # print(arr)
    prev_count = {0 : 1}
    running = 0
    count = 0
    for j in range(n):
        running += arr[j]
        count += prev_count.get(running - (j + 1), 0)
        prev_count[running - (j + 1)] = 1 + prev_count.get(running - (j + 1), 0)
    print(count)
        
        