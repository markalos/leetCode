class Solution() :
	def minimalEditStepToParlindrome(self, s):
		if len(s) == 0:
			return 0
		length = len(s)
		dps = [[0 for _ in range(length)] for _ in range(length)]
		print s
		for j in range(1, len(s)):
			for i in range(j - 1, -1, -1):

				tmp = dps[i + 1][j - 1]
				if s[i] != s[j]:
					tmp += 1
				tmp = min(tmp, dps[i + 1][j] + 1, dps[i][j - 1] + 1)
				dps[i][j] = tmp
		return dps[0][-1]

def main():
	pattern = raw_input()
	sol = Solution()
	print sol.minimalEditStepToParlindrome(pattern)

if __name__ == '__main__':
	main()
