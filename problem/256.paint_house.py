from typing import List
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0: return 0
        costs = costs[::-1]
        for i in range(len(costs) - 1):
            costs[i+1][0] += min(costs[i][1], costs[i][2])
            costs[i+1][1] += min(costs[i][0], costs[i][2])
            costs[i+1][2] += min(costs[i][0], costs[i][1])

        return min(costs[len(costs)-1])
if __name__ == '__main__':
    num = [[17,2,17],[16,16,5],[14,3,19]]
    s = Solution()
    print (s.minCost(num))