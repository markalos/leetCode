class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums :
            return -1
        left = 0
        right = len(nums) - 1
        while left < right :
            if ((right - left) == 1) :
                return nums[left] if nums[left] < nums[right] else nums[right]
            mid = left + ( right - left) / 2
            if (nums[mid] > nums[left]) :
                if nums[right] > nums[mid] :
                    return nums[left]
                else :
                    left = mid + 1
            else :
                right = mid
        return nums[left]

def main():
    sol = Solution()
    print sol.findMin([0,1,2,4])

if __name__ == '__main__':
    main()