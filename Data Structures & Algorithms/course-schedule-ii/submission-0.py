class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        res = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()
        def dfs(crs):
            
            if crs in visit:
                return False
            
            if preMap[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True
            
            visit.add(crs)
            for pres in preMap[crs]:
                if not dfs(pres):
                    return False
            
            #we good
            visit.remove(crs)
            preMap[crs] = []
            res.append(crs)
            return True
        for r in range(numCourses):
            if not dfs(r):
                return []
        return res
            