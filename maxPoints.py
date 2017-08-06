class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		

class Solution(object):
	def maxPoints(self, points):
		"""
		:type points: List[Point]
		:rtype: int
		"""
		if not points :
			return 0;
		def euclidgcd(a, b) :
			if b == 0 :
				return a
			return euclidgcd(b, a % b)
		res = 0;
		for i in range(len(points)) :
			maps = dict()
			maximum = 0
			duplicate = 1

			for j in range(i + 1, len(points)) :
				x = points[j].x - points[i].x
				y = points[j].y - points[i].y
				if x == 0 and y == 0 :
					duplicate += 1
					continue
				gcd = euclidgcd(x, y)
				if (gcd != 0) :
					x /= gcd
					y /= gcd
				if x in maps :
					if y in maps[x] :
						maps[x][y] += 1
					else :
						maps[x][y] = 1
				else :
					maps[x] = {y : 1}
				maximum = max(maximum, maps[x][y])
			res = max(res, maximum + duplicate)
		return res

def main():
	points = [Point(i % 10, i * i % 10) for i in range(100)]
	print Solution().maxPoints(points)

if __name__ == '__main__':
	main()