def insertion_asc(unsorted): #234 5196
    sort1 = [unsorted[0]]
    unsort = unsorted[1:]
    for j in unsort:
        i = 0
        for k in sort1:
            if k > j:
                break
            i += 1
        sort1.insert(i, j)
    return sort1