'''

Course Schedule
Solved 
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.

Example 1:

Input: numCourses = 2, prerequisites = [[0,1]]

Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:

Input: numCourses = 2, prerequisites = [[0,1],[1,0]]

Output: false

'''


class Solution:
    
    def mycanFinish(self, numCourses,prerequisites ):
        preMap = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        visit = set()
        def dfs(crs):
            if crs in visit: 
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in numCourses:
            if not dfs(crs): return False
        
            return True

    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()
        def dfs(crs): 
            if (crs in visit):
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(crs): return False

            visit.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses): 
            if not dfs(crs): 
                return False
            return True
        