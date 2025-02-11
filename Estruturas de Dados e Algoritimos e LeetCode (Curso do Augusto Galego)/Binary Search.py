def binary_search(nuns, n):
    lo = 0
    hi = len(nuns)
    steps = 0

    while lo < hi:
        steps+=1
        mid = int((lo + hi)/2)

        if nuns[mid] == n:
            print("Step: ", steps)
            return mid
        elif nuns[mid] < n:
            lo = mid + 1
        else:
            hi = mid
    return -1


a = [1,2,3,4,5]
b = [1,2,3,4,5,6,7,8,9,10]
c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

binary_search(d, 3)