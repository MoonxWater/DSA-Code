from engine import Engine

'''
Problem Link:
https://leetcode.com/problems/trapping-rain-water/
'''



'''This logic is flawed'''

'''
the constraints say that min len of height is one, so return 0
immediately since there is 0 capacity for elevation with 2 or less
elements

two pointers, l and r starting at 0 and 1
another pointer boundary starting at end

update l till l + 1 is smaller than l. this implies we have 
found a downward slope so there is a chance that water can be 
stored from here

update boundary from right to left till height at boundary - 1 is 
<= height at boundary which implies that there is a downward slope
before boundary

a loop wil go from l till l < boundary and r < boundary.
since r and l will update within the loop at different speeds,
assign the current value of l + 1 to r at start

the plan is to move the pointer r till the height at r is 
>= height at l. this would imply that we
have found a container.

while r is incrementing till we find a container, add each 
invalid height to a rocks list so that we can subtract it from 
the capacity later. we add this to a list and not sum it 
immediately because we don't know what is the height of the
container till me find both ends.

the other end will be either when height at r is >= height
at l or r has reached boundary

in either case calculate: 
    min(height[l], height[r]) -> min_height
    for each rock in rocks list:
        if rock <= min_height
            rocks += rock
        else if rock > min_height this implies that
        we don't need that extra height exceeding 
        min_height
            rocks += min_height

finally update capacity:
    capacity += (min_height * (r - l - 1)) - rocks
    this -1 is important because the width of each
    element is one.

we then update l to the current position of r and 
continue

finally return capacity
'''

class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) <= 2: return 0

        l = 0
        capacity = 0
        r = 1
        boundary = len(height) - 1

        while height[l] <= height[l + 1]:
            l += 1
        
        while height[boundary] <= height[boundary - 1]:
            boundary -= 1

        while l < boundary and r < boundary:        
            r = l + 1
            rocks_list = []
            rocks = 0

            while r < boundary and height[r] < height[l]:
                rocks_list.append(height[r])
                r += 1
            
            min_height = min(height[l], height[r])

            for i, rock in enumerate(rocks_list):
                if rock >= min_height:
                    rocks += min_height
                else:
                    rocks += rock

            capacity += (min_height * (r - l - 1)) - rocks
            l = r
        
        return capacity
    
obj = Solution()
print(obj.trap([0,2,0,3,1,0,1,3,2,1]))