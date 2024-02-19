

def find_maxindex_in_array(number):
    maxindex = -1
    maxvalue = -1
    for index , num in enumerate(number):
        if num > maxvalue:
            maxindex = index
            maxvalue = num
    return maxindex

print(find_maxindex_in_array([1,2,1,3,5,6,4]))