class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = bin(int(a, 2) + int(b, 2))
        return str(c)[2:]
if __name__ == '__main__':
    a = "101"
    b = "10"
    s = Solution()
    print(s.addBinary(a,b))