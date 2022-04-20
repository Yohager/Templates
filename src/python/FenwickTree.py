'''
Fenwick Tree 树状数组
对于一个已知数组存在两种操作：
1. 将某个数加上x
2. 求出某个区间的和
'''
import sys
import os
from io import BytesIO, IOBase
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

def I():
    return input()
def II():
    return int(input())
def MI():
    return map(int, input().split())
def LI():
    return list(input().split())
def LII():
    return list(map(int, input().split()))
def GMI():
    return map(lambda x: int(x) - 1, input().split())


class FenwickTree(object):
	"""docstring for FenwickTree"""
	def __init__(self, n):
		# super(FenwickTree, self).__init__()
		# self.nums = [0] + nums 
		self.n = n + 1
		self.t = [0] * (self.n)

	def low_bit(self,x):
		return x & (-x)

	def UpdateValue(self,i,x):
		while i < self.n:
			self.t[i] += x 
			i += self.low_bit(i)

	def Query(self,i):
		res = 0
		while i > 0:
			res += self.t[i]
			i -= self.low_bit(i)
		return res 

	def QueryRange(self,l,r):
		return self.Query(r) - self.Query(l-1)


if __name__ == "__main__":
	m,n = LII()
	nums = [0] + LII()

	ft = FenwickTree(m)
	for i,v in enumerate(nums):
		if i != 0:
			ft.UpdateValue(i,v)
	# print(ft.Query(m))
	for _ in range(n):
		t,x,y = LII()
		if t == 1:
			# update 
			ft.UpdateValue(x,y)
		elif t == 2:
			print(ft.QueryRange(x,y))