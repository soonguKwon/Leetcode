class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = list(map(int, str(n)))
        i=len(n)-1

        while True:
            if n[i] > n[i-1] or i-1 < 0: break
            i -= 1
        if i==0: return -1

        cur = n[i-1]
        min_index = i
        for j in range(i, len(n)):
            if cur < n[j] and n[j] <= n[min_index]:
                min_index = j

        n[i - 1], n[min_index] = n[min_index], n[i - 1]
        tmp_n = n[i:]
        tmp_n.sort()
        n[i:] = tmp_n
        res = int(''.join(map(str, n)))
        return res if res <= 1<<31 else -1
if __name__ == '__main__':
    num = 230241
    s = Solution()
    print (s.nextGreaterElement(num))