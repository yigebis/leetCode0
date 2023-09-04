class Solution:
    def list_returner(self, str: str):
        new_list = [str]
        i = len(str) - 1
        while i >= 0:
            if str[i] == ".":
                new_list.append(str[i+1:])
            i -= 1
        return new_list
    def parameters(self, str: str):
        for i in range(len(str)):
            if str[i] == " ":
                return [str[0: i], str[i+1: ]]
        return []
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        second_param = ""
        first_param = 0
        l = []
        dict = {}
        result = []
        for s in cpdomains:
            second_param = self.parameters(s)[1]
            first_param = int(self.parameters(s)[0])
            l = self.list_returner(second_param)
            for t in l:
                if t not in dict:
                    dict[t] = first_param
                else:
                    dict[t] += first_param
        for t in dict:
            result.append(str(dict[t]) + " " + t)
        return result

