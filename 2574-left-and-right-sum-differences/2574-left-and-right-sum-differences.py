class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lnum = len(nums)
        nums2 = nums[::-1]
        final_list = []
        f_l = 0
        lsum = [0]
        rsum = [0]
        sum = 0
        sum2 = 0

        for num in range(lnum - 1):
            sum = sum + nums[num]
            lsum.append(sum)

        for i in range(lnum - 1):
            sum2 = sum2 + nums2[i]
            rsum.append(sum2)

        reversed_rsum = rsum[::-1]
        for i in range(lnum):
            f_l = abs(lsum[i] - reversed_rsum[i])
            final_list.append(f_l)

        return final_list

        