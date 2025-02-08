import copy


set1 = {1,2}
set2 = {2,1}

set3 = copy.deepcopy(set1)

print(set1==set3)

set3.add(6)

print(set1==set3)
print(set1)

