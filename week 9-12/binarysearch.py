def binary_search(L, k):

    begin = 0
    end = len(L) - 1

    while(end - begin > 1):

        mid = (begin + end) // 2

        if mid == k:
            return 1

        if mid > k:
            end = mid-1

        if mid < k:
            begin = mid + 1


    #if the list has less than 2 elements
    if L[begin] == k or L[end]==k: 
        return 1
    else:
        return 0