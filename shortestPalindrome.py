# coding : utf-8
import random
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Parrot:
	def __init__(self):
		self._voltage = 100000

	@property
	def voltage(self):
		"""Get the current voltage."""
		return self._voltage

def argmin(values):
	ivs = [(i, v) for i, v in enumerate(values)]
	return min(ivs, key = lambda iv : iv[1])[0]

class Solution(object):
	def nextGreaterElements(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if len(nums) == 0 :
			return []
		cache = [(0, nums[0])]
		res = [-1] * len(nums)
		for i in range(1, len(nums)):
			if cache[-1][1] >= nums[i]:
				cache.append((i, nums[i]))
			else :
				while len(cache) > 0 and cache[-1][1] < nums[i]:
					res[cache[-1][0]] = nums[i]
					cache.pop()
				cache.append((i, nums[i]))
		idx = 0
		for i in range(len(nums) ):
			while len(cache) > 0 and cache[-1][1] < nums[i]:
				res[cache[-1][0]] = nums[i]
				cache.pop()
			if len(cache) == 0:
				break
		return res
		
	def nextGreaterElement(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n < 1 :
			return -1
		maxint = 1 << 31 - 1
		nstr = [int(i) for i in str(n)][::-1]
		for i in range(1, len(nstr)) :
			candidates = [(j, nstr[j]) for j in range(i) if nstr[i] < nstr[j] ]

			if len(candidates) > 0:
				pivot = min(candidates, key = lambda c : c[1])[0]
				nstr[pivot], nstr[i] = nstr[i], nstr[pivot]
				nstr = sorted(nstr[:i], reverse = True) + nstr[i : ]
				factor = 1
				res = 0
				for ele in nstr:
					res += factor * ele
					factor *= 10
				return res
		return -1

	def createNode(self, v):
		return TreeNode(v)

	def addOneRow(self, root, v, d):
		"""
		:type root: TreeNode
		:type v: int
		:type d: int
		:rtype: TreeNode
		"""
		pass
		if d == 1:
			nroot = self.createNode(v)
			nroot.left = root
			return nroot
		pstack = [root]
		nstack = []
		for i in range(2, d):
			for node in pstack:
				if node.left is not None:
					nstack.append(node.left)
				if node.right is not None:
					nstack.append(node.right)
			pstack , nstack = nstack, pstack
			nstack.clear()
		for node in pstack:
			leftNode = self.createNode(v)
			leftNode.left = node.left
			node.left = leftNode
			rightNode = self.createNode(v)
			rightNode.right = node.right
			node.right = rightNode
		return root
				

	def shortestPalindrome(self, string):
		"""
		Computes length of the longest palindromic substring centered on each char 
		in the given string. The idea behind this algorithm is to reuse previously 
		computed values whenever possible (palindromes are symmetric).
		
		Example (interleaved string):
		i    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 
		s    #  a  #  b  #  c  #  q  #  q  #  q  #  q  #  q  #  q  #  x  #  y  #
		P    0  1  0  1  0  1  0  1  2  3  4  5  6  5  4  ?
										^        ^        ^        ^
									  mirror   center   current  right
		
		We're at index 15 wondering shall we compute (costly) or reuse. The mirror
		value for 15 is 9 (center is in 12). P[mirror] = 3 which means a palindrome
		of length 3 is centered at this index. A palindrome of same length would be
		placed in index 15, if 15 + 3 <= 18 (right border of large parlindrome 
		centered in 12). This condition is satisfied, so we can reuse value from
		index 9 and avoid costly computation.
		"""
		if not string:
			return ''
		right = 0
		center = 0
		dataString = string
		string = self.interleave(string)
		dps = [0] * len(string)
		
		for i in range(1, len(string)):
			mirror = 2*center - i
			if i + dps[mirror] < right:
				dps[i] = dps[mirror]
			else:
				center = i
				mirror = 2 * center - right - 1
				ridx = right + 1
				# print (i, center, right, mirror)
				while ridx < len(string):
					if mirror >= 0 and string[mirror] == string[ridx]:
						mirror -= 1
						ridx += 1
					else :
						break
				# print (i, center, ridx, mirror)
				right = ridx - 1
				dps[i] = right - i

		# print (string)
		idx = len(dps) - 1
		while idx > 0:
			if idx == dps[idx]:
				break
			idx -= 1
		# print (idx, 'idx')
		return  dataString[:idx - 1 - len(dataString): -1] + dataString

	def interleave(self, string):
		"""
		Returns a interleaved version of a given string. 'aaa' --> '#a#a#a#'.
		Thanks to thin function we don't have to deal with even/odd palindrome 
		length problem.
		"""
		ret = []
		for s in string:
			ret.extend(['#', s])
		ret.append('#')
		
		return ''.join(ret)




def manacher(string):
	"""
	Computes length of the longest palindromic substring centered on each char 
	in the given string. The idea behind this algorithm is to reuse previously 
	computed values whenever possible (palindromes are symmetric).
	
	Example (interleaved string):
	i    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 
	s    #  a  #  b  #  c  #  q  #  q  #  q  #  q  #  q  #  q  #  x  #  y  #
	P    0  1  0  1  0  1  0  1  2  3  4  5  6  5  4  ?
									^        ^        ^        ^
								  mirror   center   current  right
	
	We're at index 15 wondering shall we compute (costly) or reuse. The mirror
	value for 15 is 9 (center is in 12). P[mirror] = 3 which means a palindrome
	of length 3 is centered at this index. A palindrome of same length would be
	placed in index 15, if 15 + 3 <= 18 (right border of large parlindrome 
	centered in 12). This condition is satisfied, so we can reuse value from
	index 9 and avoid costly computation.
	"""
	if not string:
		return []
	right = 0
	center = 0
	string = interleave(string)
	dps = [0] * len(string)
	
	for i in range(1, len(string)):
		mirror = 2*center - i
		if i + dps[mirror] < right:
			dps[i] = dps[mirror]
		else:
			center = i
			mirror = 2 * center - right - 1
			ridx = right + 1
			# print (i, center, right, mirror)
			while ridx < len(string):
				if mirror >= 0 and string[mirror] == string[ridx]:
					mirror -= 1
					ridx += 1
				else :
					break
			# print (i, center, ridx, mirror)
			right = ridx - 1
			dps[i] = right - i

	# print (string)
	return  dps

def main():
	sol = Solution()
	print sol.nextGreaterElements([1,2,1])


if __name__ == '__main__':
	main()