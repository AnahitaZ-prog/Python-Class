#Add members of a list with a recursive function

#list = [1,2,3,4,5,6,7,8,9,10]
def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])
        
print sum([1,3,5,7,9])
