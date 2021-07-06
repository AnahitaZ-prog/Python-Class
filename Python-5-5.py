# Remove Duplicate items of a list

my_list = ['a','b','d','c','b','c','a']
temp_list = []
for i in my_list:
    if i not in temp_list:
        temp_list.insert(0,i)
        my_list.remove(i)
print(temp_list)
