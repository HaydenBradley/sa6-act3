def find_intersection(list1, list2):
    intersection = list(filter(lambda x: x in list2, list1))
    return intersection

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

intersection_result = find_intersection(list1, list2)

print("Intersection two lists:", intersection_result)
