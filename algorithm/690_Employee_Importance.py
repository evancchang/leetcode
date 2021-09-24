"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(id):
            imp = emap[id]
            for sub_id in sub_map[id]:
                imp += dfs(sub_id)
            return imp
        
        emap = {}
        sub_map = {}
        for employee in employees:
            emap[employee.id] = employee.importance
            sub_map[employee.id] = employee.subordinates
            
        return dfs(id)
            
