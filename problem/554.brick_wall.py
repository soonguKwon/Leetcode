import sys
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        total_cnt={}
        for j in range(len(wall)):
            sum = 0
            for i in range(len(wall[j]) - 1):
                sum += wall[j][i]
                if sum in total_cnt:
                    total_cnt[sum] = total_cnt[sum] + 1
                else:
                    total_cnt[sum] = 1
        res = len(wall)
        for cnt in total_cnt.values():
            res = min(res, len(wall)-cnt)
        return res

if __name__ == '__main__':
    num = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    s = Solution()
    print(s.leastBricks(num))