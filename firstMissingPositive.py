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

	def reversePairs(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		length = len(nums)
		sortednums = [nums[0]] * length
		def partition(nums, left, right):
			if right <= left:
				return 0
			if (right - left) == 1:
				if nums[left] > nums[right]:
					nums[left], nums[right] = nums[right], nums[left]
					return int(nums[right] > 2 * nums[left])
				return int(nums[left] > 2 * nums[right])
			mid = left + (right - left) / 2
			rightleft = mid + 1
			numReversePairs = partition(nums, left, mid) + partition(nums, rightleft, right)
			doubleidx = rightleft
			lidx = left
			while (lidx <= mid):
				while doubleidx <= right and nums[lidx] > 2 * nums[doubleidx]:
					doubleidx += 1
				numReversePairs += (doubleidx - rightleft)
				lidx += 1
			lidx, ridx = left, rightleft
			sidx = 0
			while (lidx <= mid):
				while ridx <= right and nums[lidx] > nums[ridx]:
					sortednums[sidx] = nums[ridx]
					ridx += 1
					sidx += 1
				sortednums[sidx] = nums[lidx]
				sidx += 1
				lidx += 1
			while ridx <= right:
				sortednums[sidx] = nums[ridx]
				ridx += 1
				sidx += 1
			for i in xrange(sidx):
				nums[left] = sortednums[i]
				left += 1
			return numReversePairs

		return partition(nums, 0, length - 1)

	def groudTruth(self, nums):
		numReversePairs = 0
		for i in xrange(len(nums)):
			for j in xrange(i + 1, len(nums)):
				if nums[i] > 2 * nums[j]:
					numReversePairs += 1
		return numReversePairs

	def generateInts(self, length):
		import random
		return random.sample(range(-(4 * length + 1), 4 * length + 1), length)


	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s :
			return 0
		oddOccurrence = [False] * 256
		longestlength = 1
		for c in s:
			idx = ord(c)
			oddOccurrence[idx] = not oddOccurrence[idx]
		return (len(s) - (max(0, sum(oddOccurrence) - 1)))

	def shortestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if s == '' :
			return ''
		symmetricalRight = 0
		for i in range(len(s) - 1, 0 , -1):
			flag = True
			ridx = i
			for j in range(0, (i + 1) / 2):
				if not s[ridx] == s[j]:
					flag = False
					break
				ridx -= 1
			if flag:
				symmetricalRight = i
				break
		return s[symmetricalRight + 1 :][::-1] + s

	def kmpTable(self, pattern):
		if pattern == '':
			return []
		i, j = 0, -1
		nextPos = [0] * len(pattern)
		while i < len(pattern):
			while j > -1 && x[i] :
				pass


def main():
	print (Solution().shortestPalindrome("a" * 400000))
	# print nums

if __name__ == '__main__':
	main()