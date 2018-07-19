# https://leetcode.com/problems/employee-importance/description/

"""
Solution.
Used: DFS algortihm
Complexity analysis:
Time: O(N * M)
Memory: O(N * M) in worst case
"""

"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        data = {employee.id : employee for employee in employees}
        
        def dfs(id):
            sum = data[id].importance
            for sub_id in data[id].subordinates:
                sum += dfs(sub_id)
                
            return sum
        
        return dfs(id)
            

