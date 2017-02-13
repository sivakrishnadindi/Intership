def index_power(array,n):
    if (len(array)-1)>=n:
        return (array[n])**n
    else:
        return -1
print index_power([1, 2], 3)