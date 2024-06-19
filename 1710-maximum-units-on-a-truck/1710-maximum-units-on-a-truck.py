class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        summ = 0
        boxTypes.sort(key=lambda x:x[1])
        boxTypes.reverse()
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                summ += box * units
            else:
                summ += truckSize * units
                break
        return summ
        