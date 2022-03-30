def heap_sort(a):
    def down_heap(a,left,right):
        temp = a[left]
        parent = left
        while parent < (right+1)//2:
            cl = parent*2+1
            cr = cl+1
            child = cr if cr<= right and a[cr]> a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp
    
    n= len(a)
    for i in range((n-1)//2,-1,-1):
        down_heap(a,i,n-1)