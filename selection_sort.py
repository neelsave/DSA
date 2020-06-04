#selection sort not optimized

def selection_sort(list_a):
    len_index = range(0, len(list_a)-1)

    for i in len_index:
        min_value = i
        
        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j
                
        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
            
    return list_a

print(selection_sort([6,2,1,4,2,4,3,2]))
    