import cProfile
class Solution(object):
	def findLadders(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: List[List[str]]
		"""
#         wordLength = len(beginWord)
		if not wordList or endWord not in wordList:
			return [];
		def oneDistance(lha, rha) : 
			return (1 == sum(1 for x, y in zip(lha, rha) if x != y) )
		if oneDistance(beginWord, endWord) :
			return [[beginWord, endWord]]
		if wordList[-1] != endWord :
			pos = wordList.index(endWord)
			wordList[pos] = wordList[-1]
			wordList[-1] = endWord
		if beginWord in wordList :
			pos = wordList.index(beginWord)
			wordList[pos] = wordList[0]
			wordList[0] = beginWord
		else :
			wordList = [beginWord] + wordList
		length = len(wordList)
		neighbours = [[] for i in range(length)]
		for i in range(length) :
			currentWord = wordList[i]
			for j in range(i + 1, length) :
				if oneDistance(currentWord, wordList[j]) :
					neighbours[i].append(j)
					neighbours[j].append(i)
		visited = [False] * length
		print 'wordList ', wordList, neighbours

		# visited[0] = True
		target = length - 1
		res = []
		path = [0] * length
		maxPathLength = length + 1
		currentPathLength = 0;
		bfsqueue = [0]
		while len(bfsqueue):
			item = bfsqueue.pop()
			if visited[item]:
				continue
			currentPathLength += 1
			if currentPathLength > maxPathLength:
				currentPathLength -= 1
				continue
			
			path[currentPathLength - 1] = item
			if item == target:
				if currentPathLength == maxPathLength:
					res.append(path[:currentPathLength])
				else :
					res = [path[:currentPathLength]]
			visited[item] = True
			for toPos in neighbours[item]:
				if visited[toPos]:
					continue
				bfsqueue.append(toPos)
			currentPathLength -= 1
			visited[item] = False
		# def deepFirstSearch(currentPos, nextIdx, currentPathLength):
		# 	if nextIdx > currentPathLength :
		# 		return currentPathLength
		# 	visited[currentPos] = True
		# 	path[nextIdx] = currentPos;
		# 	if currentPos == target :
		# 		if currentPathLength == nextIdx :
		# 			res.append(path[:nextIdx + 1])
		# 		else :
		# 			currentPathLength = nextIdx
		# 			del res[:]
		# 			res.append(path[:nextIdx + 1])
		# 		visited[currentPos] = False
		# 		return currentPathLength
		# 	for ele in neighbours[currentPos] :
		# 		if visited[ele] :
		# 			continue
		# 		currentPathLength = deepFirstSearch(ele, nextIdx + 1, currentPathLength)
		# 	# visited[currentPos] = False
		# 	return currentPathLength
		# deepFirstSearch(0, 0, length)       
		return [[wordList[i] for i in path]for path in res]
	def findLadders1(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: List[List[str]]
		"""
#         wordLength = len(beginWord)
		if not wordList or endWord not in wordList:
			return [];
		def oneDistance(lha, rha) : 
			return (1 == sum(1 for x, y in zip(lha, rha) if x != y) )
		if oneDistance(beginWord, endWord) :
			return [[beginWord, endWord]]
		if wordList[-1] != endWord :
			pos = wordList.index(endWord)
			wordList[pos] = wordList[-1]
			wordList[-1] = endWord
		if beginWord in wordList :
			pos = wordList.index(beginWord)
			wordList[pos] = wordList[0]
			wordList[0] = beginWord
		else :
			wordList = [beginWord] + wordList
		length = len(wordList)
		neighbours = [[] for i in range(length)]
		for i in range(length) :
			currentWord = wordList[i]
			for j in range(i + 1, length) :
				if oneDistance(currentWord, wordList[j]) :
					neighbours[i].append(j)
					neighbours[j].append(i)
		visited = [False] * length
		visited[0] = True
		target = length - 1
		res = []
		path = [0] * length
		# print ('neighbours = ', neighbours, wordList)
#         currentPathLength = length + 1
		def deepFirstSearch(currentPos, nextIdx, currentPathLength):
			if nextIdx > currentPathLength :
				return currentPathLength
			if currentPos == target :
				if currentPathLength == nextIdx :
					res.append(path[:nextIdx])
				else :
					currentPathLength = nextIdx
					del res[:]
					res.append(path[:nextIdx])
				return currentPathLength
			tmp = neighbours[currentPos]
			for ele in tmp :
				if visited[ele] :
					continue
				visited[ele] = True;
				path[nextIdx] = ele;
				currentPathLength = deepFirstSearch(ele, nextIdx + 1, currentPathLength)
				visited[ele] = False
			return currentPathLength
		deepFirstSearch(0, 1, length + 1)       
		return [[wordList[i] for i in path]for path in res]


def main():
	beginWord = 'hit'
	endWord = 'cog'
	wordList = ["hot","dot","dog","lot","log","cog"]
	# wordList = ["hot","dot","dog","lot","log","cog", 'git', 'gut', 'cut', 'coo', 'poo', 'peg', 'mug', 'pat', 'put', 'fit', 'far', 'lit', 'who', 'pig', 'god', 'pod', 'mud', 'mum', 'inn', 'pad', 'mad', 'set', 'get', 'use', 'pee', 'cat' , 'hat', 'the', 'bad', 'for', 'lid', 'let', 'see', 'but' , 'vet', 'red', 'bar', 'net', 'rod']
	wordList = list(set(wordList))
	print (wordList)
	print (Solution().findLadders(beginWord, endWord, wordList))

def test():
	# To check if strings differ by 
	# exactly one character

	def isadjacent(a, b):
		count = 0
		n = len(a)

		# Iterate through all characters and return false
		# if there are more than one mismatching characters
		for i in range(n):
			if a[i] != b[i]:
				count += 1
			if count > 1:
				break

		return True if count == 1 else False

	# A queue item to store word and minimum chain length
	# to reach the word.
	class QItem():

		def __init__(self, word, len):
			self.word = word
			self.len = len

	# Returns length of shortest chain to reach 
	# 'target' from 'start' using minimum number
	# of adjacent moves. D is dictionary
	def shortestChainLen(start, target, D):

		# Create a queue for BFS and insert 
		# 'start' as source vertex
		Q = []
		item = QItem(start, 1)
		Q.append(item)

		while( len(Q) > 0):

			curr = Q.pop()

			# Go through all words of dictionary
			for it in D:

				# Process a dictionary word if it is 
				# adjacent to current word (or vertex) of BFS
				temp = it
				if isadjacent(curr.word, temp) == True:

					# Add the dictionary word to Q
					item.word = temp
					item.len = curr.len + 1
					Q.append(item)

					# Remove from dictionary so that this 
					# word is not processed again. This is 
					# like marking visited
					D.remove(temp)

					# If we reached target
					if temp == target:
						return item.len

	D = ["hot","dot","dog","lot","log","cog", 'git', 'gut', 'cut', 'coo', 'poo', 'peg', 'mug', 'pat', 'put', 'fit', 'far', 'lit', 'who', 'pig', 'god', 'pod', 'mud', 'mum', 'inn', 'pad', 'mad', 'set', 'get', 'use', 'pee', 'cat' , 'hat', 'the', 'bad', 'for', 'lid', 'let', 'see', 'but' , 'vet', 'red', 'bar', 'net', 'rod']
	start = "hit"
	target = "use"
	print "Length of shortest chain is: {}".format(shortestChainLen(start, target, D))

if __name__ == '__main__':
	# main()
	cProfile.run('main()')
	