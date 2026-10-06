class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0]* len(temperatures)
        unresolved_days = []

        for current_day in range(len(temperatures)):
            current_temp = temperatures[current_day]

            while unresolved_days and current_temp > temperatures[unresolved_days[-1]]:
                previous_day = unresolved_days.pop()
                wait_time = current_day - previous_day
                answer[previous_day] = wait_time
            
            unresolved_days.append(current_day)
        return answer
        
        


            