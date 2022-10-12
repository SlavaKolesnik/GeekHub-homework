# 2. Write a script to remove empty elements from a list.
# Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

test_list  = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

res = list(map(list, test_list))
list_1 = [x for x in res if x]
list_2 = [x for x in list_1 if x != ['']]


print(list_2)
