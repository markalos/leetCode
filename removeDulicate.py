import collections

class Solution(object):
	def removeDuplicateLetters(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if not s :
			return ""
		cnt = collections.Counter(list(s))
		pos = 0
		for i, x in enumerate(s) :
			if x < s[pos] :
				pos = i
			cnt[x] -= 1;
			if (cnt[x] == 0) :
				break
		return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ""))

	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		def foldPeak(peakIdx):
			print peakIdx, height
			while len(peakIdx) > 2:
				print peakIdx[-1], peakIdx[-2], peakIdx[-3]
				if height[peakIdx[-1]] > height[peakIdx[-2]] and height[peakIdx[-3]] >= height[peakIdx[-2]]:
					peakIdx[-2] = peakIdx[-1]
					peakIdx.pop()
				else :
					break
		length =  len(height)
		if length < 3:
			return 0
		peakIdx = []
		left = 0
		res = 0
		while left < length - 1:
			if height[left + 1] < height[left]:
				peakIdx.append(left)
				break
			left += 1
		if left == (length - 1):
			return 0
		for i in xrange(1, length - 1):
			if height[i - 1] < height[i]:
				if height[i] >= height[i + 1]:
					peakIdx.append(i)
					foldPeak(peakIdx)
		print peakIdx
		if height[-1] > height[-2]:
			peakIdx.append(length - 1)
			foldPeak(peakIdx)
		if 0 == len(peakIdx):
			return 0
		lidx = peakIdx[0]
		for j in xrange(1, len(peakIdx)):
			ridx = peakIdx[j]
			peak = min(height[lidx], height[ridx])
			for i in xrange(lidx + 1, ridx):
				res += max(0, peak - height[i])
			lidx = ridx
		return res

def main():
	solution = Solution()
	solution.removeDuplicateLetters('cabkdeackfkm')
	print solution.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]) == 83
	print solution.trap([8,8,1,5,6,2,5,3,3,9]) == 31

if __name__ == '__main__':
	# main()
	alphabet = ['z']
	for i in xrange(25):
		alphabet.append(chr(i + ord('a')))
	print alphabet