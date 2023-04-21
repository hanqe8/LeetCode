class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 1:
            return duration
        soln, repeat = 0, 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] >= duration:
                soln += duration
            else:
                repeat += duration - (timeSeries[i+1] - timeSeries[i])
        return len(timeSeries)*duration - repeat
        
