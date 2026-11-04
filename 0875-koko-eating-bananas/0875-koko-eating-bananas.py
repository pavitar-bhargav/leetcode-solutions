class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        slowest_speed = 1
        fastest_speed = max(piles)
        best_speed = fastest_speed

        while slowest_speed <= fastest_speed:
            test_speed = (fastest_speed + slowest_speed) // 2
            hours_spent = 0

            for pile in piles:
                hours_spent += (pile + test_speed - 1) // test_speed
            
            if hours_spent <= h:
                best_speed = test_speed
                fastest_speed = test_speed - 1
            else:
                slowest_speed = test_speed + 1
        
        return best_speed 
        