strings_list = ["mcdonalds", "wendys", "poplar", "yates", "chicfila", "central"]

sorted_list = sorted(strings_list, key=lambda x: (len(x), x))

print(sorted_list)
