class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        output = []
        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            if target-nums[i] in map and map[target - nums[i]] != i:
                
                first = map.get(nums[i])
                second = map.get(target-nums[i])
                output.append(first)
                output.append(second)

                return output
           
        