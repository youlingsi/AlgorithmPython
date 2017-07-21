#sample of merge-sort algrithm

LIST = [0, 38, 5, 23, 8, 4, 0, 2, 9, 3, 4, 8, 2, 0, 3, 4, 15, 7, 2, 0, 0]
Sorted = LIST[:]
Sorted.sort()
           
def merge(Left, Right):
    merged = []
    i = 0
    j = 0
    while j < len(Right) and i < len(Left):
        if Left[i] < Right[j]:
            merged.append(Left[i])
            i += 1
        elif Left[i] > Right[j]:
            merged.append(Right[j])
            j += 1
        elif Left[i] == Right[j]:
            merged.append(Left[i])
            i += 1                
            merged.append(Right[j])
            j += 1
    if j < len(Right):
        merged += Right[j:]
    elif i < len(Left):
        merged += Left[i:]                  
    return merged
    
def sortLst(L):
    if len(L) == 1:
        return L
    else:
        Left = L[:len(L)/2]
        Right = L[len(L)/2:]
        return merge(sortLst(Left), sortLst(Right))
    
    
print Sorted
print sortLst(LIST)