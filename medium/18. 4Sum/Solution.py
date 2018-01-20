class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        if not nums or nums[0]*4 > target or nums[-1]*4 < target:
            return result
        for i in range(len(nums)-3):
            threeTarget = target - nums[i]
            if nums[i+1]*3>threeTarget or nums[-1]*3 < threeTarget:
                continue
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                x = self.threeSum(nums[i+1:],threeTarget)
                if x:
                    for item in x:
                        item.append(nums[i])
                        result.append(item)
        return result
                
            
            
    def threeSum(self,nums,target):
        result = []
        if not nums or nums[-1] * 3 < target or nums[0] * 3 > target:
            return result
        else:
            for i in range(len(nums)-2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                low = i +1
                high = len(nums) -1
                twoTarget = target - nums[i]
                while low < high:
                    if nums[low] * 2 > twoTarget or nums[high] * 2 < twoTarget:
                        break
                    sum = nums[low] + nums[high]
                    if sum < twoTarget or (low > i + 1 and nums[low] == nums[low - 1]):
                        low +=1
                    elif sum > twoTarget or (high < len(nums) -1 and nums[high]== nums[high+1]):
                        high -=1
                    else:
                        result.append([nums[i],nums[low],nums[high]])
                        low +=1
                        high -=1
        return result
