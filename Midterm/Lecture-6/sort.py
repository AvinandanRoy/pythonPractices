sample_dict = {'kouser': 6, 'atia': 1, 'shaida': 3, 'kona': 8}

sorted_asc = {}
for key in sorted(sample_dict, key=sample_dict.get):
    sorted_asc[key] = sample_dict[key]

print("Sorted Dictionary (Ascending):", sorted_asc)

sorted_desc = {}
for key in sorted(sample_dict, key=sample_dict.get, reverse=True):
    sorted_desc[key] = sample_dict[key]


print("Sorted Dictionary (Descending):", sorted_desc)

