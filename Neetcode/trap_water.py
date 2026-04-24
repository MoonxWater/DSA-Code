def trap(height: list[int]) -> int:
    '''
    one pointer at start
    update pointer till l + 1 is smaller than l 
    after that a new pointer will go till r + 1 is smaller then r
        (this implies that the water will fall beyond this point)
    update capacity at every increment of r with height[l] - height[r]

    calc min(height[l], height[r])
    if height[l] is smaller move on
    else subtract from capacity (height[l] - height[r]) * (r - l)

    update l to be r and repeat the process
    
    there is a variable to store capacity

    remember to subtract width from all the calculations
    
    max water to trap = min(height[l], height[r]) * (r - l - 1) 
                        - (all heights between l and r)

    '''

    l = 0
    capacity = 0
    r = 1

    while l < len(height) - 1 and r < len(height):
        print(l)
        if height[l] <= height[l + 1]: 
            l += 1
            continue
    
        r = l + 1
        rocks = height[r]
        backup_capacity = capacity

        while r < len(height) - 1 and height[r] >= height[r + 1]:
            r += 1
            rocks += height[r]

        while r < len(height) - 1 and height[r] <= height[r + 1]:
            r += 1 
            rocks += height[r]

        capacity += (min(height[l], height[r]) * (r - l - 1)) - rocks
        l = r - 1

        if r == len(height) - 1:
            break

    return capacity

print("Capacity:", trap([0,2,0,3,1,0,1,3,2,1]))
