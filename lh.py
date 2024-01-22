import random

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

list3 = list1 + list2
print(list3)
list4 = list(set(list1 + list2))
print(list4)
list5 = list(set(list1) & set(list2))
print(list5)
list6 = list(set(list1) ^ set(list2))
print(list6)
list7 = [min(list1), max(list1), min(list2), max(list2)]
print(list7)

