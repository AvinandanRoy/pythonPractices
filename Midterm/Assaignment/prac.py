def swap_elements_by_index(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Swapping elements at index 1 and 3
my_list = swap_elements_by_index(my_list, 1, 3)
print("List after swapping elements at index 1 and 3:", my_list)
