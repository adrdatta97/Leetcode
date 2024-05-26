class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        l = len(batteryPercentages)
        c = 0
        for i in range(l):
            if batteryPercentages[i]-c > 0:
                c += 1
        return c
        