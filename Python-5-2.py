# merge 2 lists with out Zip
f_n = ['a','b','c','d']
l_n = [1,2,3,4]

def merge(lst_1,lst_2):
    return list(map(lambda x,y:(x,y),lst_1,lst_2))
print(merge(f_n,l_n))
