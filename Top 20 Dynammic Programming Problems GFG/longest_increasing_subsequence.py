def ci(A, l, r, k):
    while r-l > 1:
        mid = (l + (r-l))//2
        if A[mid] >= k:
            r=mid
        else:
            l=mid
    return r

def longestSubsequence(a,n):
    t = [0 for _ in range(n+1)]
    l=0
    t[0] = a[0]
    l=1
    for i in range(1, n):
        if a[i] < t[0]:
            t[0] = a[i]
        elif a[i] > t[l-1]:
            t[l] = a[i]
            l+=1
        else:
            x = ci(a, -1, l-1, a[i])
            t[x] = a[i]
    return l
a = list(map(int, input().split(',')))
print(longestSubsequence(a,len(a)))
