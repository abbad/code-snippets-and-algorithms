""" 
    Merge sort function.
    I learned and implemented this function during algorithms and data structures course. 
    I wrote this fun fun :)

    Merge sort is a divide and conquer algorithm. It will make this list into a smaller 
    lists by calling itself in recursively.
"""


def merge_sort(merge_list): 

    if len(merge_list) <= 1:
        return merge_list

    middle = len(merge_list) // 2

    # The divide part.
    right_list = merge_sort(merge_list[middle:])
    left_list = merge_sort(merge_list[:middle])

    # The merging part.
    return merge(right_list, left_list)


def merge(right_list, left_list):
    result = []
    r_idx = 0
    l_idx = 0

    while r_idx < len(right_list) and l_idx < len(left_list):

        if left_list[l_idx] < right_list[r_idx]:
            result.append(left_list[l_idx])
            l_idx += 1
        else:
            result.append(right_list[r_idx])
            r_idx += 1

    if len(right_list) > 0:
        result.extend(right_list[r_idx:])

    if len(left_list) > 0:
        result.extend(left_list[l_idx:])

    return result

if __name__ == "__main__":
	print(merge_sort([3,2,1, 7, 6, 5]))
