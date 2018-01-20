class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #sort
        #target = -num[i]
        #from num[low] = num[i+1] ~ num[hi] = num[len-1]
        #if num[low] + num[high] < -num[i], low+
        #else >, high -
        result = []
        nums.sort()
        if not nums or nums[-1]< 0 or nums[0] > 0:
            return result
        else:
            for i in range(len(nums)-2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                low = i +1
                high = len(nums) -1
                target = -1 * nums[i]
                while low < high:
                    sum = nums[low] + nums[high]
                    if sum < target or (low > i + 1 and nums[low] == nums[low - 1]):
                        low +=1
                    elif sum > target or (high < len(nums) -1 and nums[high]== nums[high+1]):
                        high -=1
                    else:
                        result.append([nums[i],nums[low],nums[high]])
                        low +=1
                        high -=1
        return result
