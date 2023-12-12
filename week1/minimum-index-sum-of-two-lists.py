class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index_sum = len(list1) + len(list2)
        index_of = {}
        common = []

        for index in range(len(list1)):
            index_of[list1[index]] = index
        
        for i in range(len(list2)):
            if list2[i] in index_of:
                if i + index_of[list2[i]] < min_index_sum:
                    min_index_sum = i + index_of[list2[i]]
                    # common = [list2[i]]
                # elif i + index_of[]
        for i in range(len(list2)):
            if list2[i] in index_of and i + index_of[list2[i]] == min_index_sum:
                common.append(list2[i])
        
        return common