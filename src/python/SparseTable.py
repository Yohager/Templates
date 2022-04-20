'''
sparse table 稀疏表
st[i][j] 对应的区间为 [i:i+2^j]

'''
import math 

class SparseTable(object):
	"""docstring for SparseTable"""
	def __init__(self, nums):
		super(SparseTable, self).__init__()
		self.nums = nums
		self.n = len(nums)
		self.w = int(math.log(self.n,2)) + 1
		self.st = [[0] * (self.w+1) for _ in range(self.n)] # 设置一个n*w的稀疏表 能够满足n(2^w)长度的数组

	def Preprocessing(self):
		# 稀疏表中每行的第一个元素应该为原数组对应下标的元素
		for i in range(self.n):
			self.st[i][0] = self.nums[i]
		for j in range(1,self.w+1):
			for i in range(self.n):
				if i + (1<<j) - 1 < self.n:
					self.st[i][j] = max(self.st[i][j-1],self.st[i+(1<<(j-1))][j-1])
		# print(self.st)

	def Query(self,l,r):
		k = int(math.log(r-l+1,2))
		return max(self.st[l][k],self.st[r-(1<<k)+1][k])


if __name__ == "__main__":
	m,n = list(map(int,input().split()))
	nums = list(map(int,input().split()))
	queries = []
	for i in range(n):
		queries.append(list(map(int,input().split())))

	st = SparseTable(nums)
	st.Preprocessing()
	for l,r in queries:
		# print('current query is:',l-1,r-1)
		print(st.Query(l-1,r-1))
