class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a,b = 0, len(numbers) - 1

        while a < b:
            curSum = numbers[a] + numbers[b]

            if curSum > target:
                b -= 1
            elif curSum < target:
                a += 1
            else:
                return [a+1,b+1]
        return[]      