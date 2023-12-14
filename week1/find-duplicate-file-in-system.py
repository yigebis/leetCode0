class Solution:
    def in_brackets(self, s: str) -> str:
        return s.split('(')[1][:-1]
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_root = {}
        for i in paths:
            parent = i.split(' ')[0]
            for f in i.split(' ')[1:]:
                content = self.in_brackets(f)
                path = parent + '/' + f.split('(')[0]
                if content in content_to_root:
                    content_to_root[content].append(path)
                else:
                    content_to_root[content] = [path] 
        list = []
        for i in content_to_root:
            if len(content_to_root[i]) > 1:
                list.append(content_to_root[i])
        return list       