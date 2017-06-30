class Solution(object):
	def singleNumber(self, nums):
		ones = 0
		twos = 0
		for e in nums:
			t1 = ones ^ e
			t2 = (ones & e) ^ twos
			t3 = ~ (t1 & t2)
			ones = t1 & t3
			twos = t2 & t3

		return ones
	def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
	  
		slow = nums[0]
		fast = nums[nums[0]]
		while (slow != fast):
			print slow, fast
			slow = nums[slow]
			fast = nums[nums[fast]]


		fast = 0;
		while (fast != slow):
			fast = nums[fast]
			slow = nums[slow]
			
		return slow

	def minCut(self, s):
		if not s:
			return ''
		length = len(s)
		dps = [True] * length
		cutsno = [length] * (length + 1)
		cutsno[-1] = -1
		for i in range(1, length):
			for j in xrange(i):
				dps[j] = ((s[i] == s[j]) and dps[j + 1])
				if dps[j] and (cutsno[j - 1] < cutsno[i]):
					cutsno[i] = cutsno[j - 1] + 1
			if cutsno[i - 1] < cutsno[i]:
				cutsno[i] = cutsno[i - 1] + 1
		return cutsno[-2]

	def repeatingElements(self, nums):
		if not nums:
			return -1
		for i in xrange(len(nums)):
			if nums[abs(nums[i])] > 0:
				nums[abs(nums[i])] = -1
			else :
				print (asb(nums[i]))

	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		if not s :
			return ''
		length = len(s)
		dps = [True] * length
		result = [[] for _ in range(length + 1)]
		result[0].append([s[0]])
		result[-1].append([])
		for i in range(1, length) :
			for j in range(i) :
				dps[j] = ((s[j] == s[i]) and dps[j + 1])
				if dps[j] :
					tmp = [s[j: i + 1]]
					for ele in result[j - 1] :
						result[i].append(ele + tmp)
			tmp = [s[i]]
			for ele in result[i - 1] :
				result[i].append(ele + tmp)
		return result[-2]

	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums :
			return []
		pivot = len(nums)
		res = []
		for i in range(pivot) :
			idx = abs(nums[i])
			if nums[idx - 1] < 0:
				res.append(idx)
			else :
				nums[idx - 1] = - nums[idx - 1]
		upper = 3 * pivot
		return res

	def findDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums :
			return []
		pivot = len(nums)
		res = []
		for i in range(pivot) :
			idx = abs(nums[i])
			if nums[idx - 1] < 0:
				res.append(idx)
			else :
				nums[idx - 1] = - nums[idx - 1]
		upper = 3 * pivot
		return res
		
def main():
	print (Solution().findDuplicates([4,3,2,7,8,2,3,1]))

if __name__ == '__main__':
	main()