def maxArea(height):
    i,j = 0, len(height)-1
    ans = -99999
    while i < j:
        m = min(height[i], height[j])
        ans = max(ans, m*(j-i))
        if height[i] < height[j]:
            i+=1
        else:
            j-=1
    return ans




height = list(map(int, input().split()))
r = maxArea(height)
print(r)
