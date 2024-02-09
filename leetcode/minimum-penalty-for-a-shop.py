class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N= len(customers)
        yes = [0 for _ in range(N+1)]
        no = [0 for _ in range(N+1)]
        for i in range(N):
            if customers[N-i-1]=='Y':
                yes[N-i-1]= yes[N-i]+1
            else:
                yes[N-i-1]=yes[N-i]
            if  customers[i]=="N":
                no[i+1] = no[i]+1
            else:
                no[i+1] = no[i]
        min_value =yes[0]+no[0] 
        min_index = 0

        for i in range(N+1):
            curr_sum = yes[i]+no[i]
            if curr_sum<min_value:
                min_index = i
                min_value = curr_sum
        return min_index

# NNNN
# 01234