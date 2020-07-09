class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]

        if x[-1] == "-": x = '-' + x[:-1]

        res = int(x)
        if res >= -2 ** 31 and res < 2 ** 31 - 1:
            return res
        else:
            return 0
if __name__ == '__main__':
    num = 1534236469
    s = Solution()
    print (s.reverse(num))