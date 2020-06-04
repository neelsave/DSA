def bubble(un_list):
    index_length = len(un_list) - 1
    sort = False
    
    while not sort:
        sort = True
        for i in range(0, index_length):
            if un_list[i] > un_list[i+1]:
                sort = False
                un_list[i], un_list[i+1] = un_list[i+1], un_list[i]
    return un_list

print(bubble([5,2,4,2,5,6,7]))
    