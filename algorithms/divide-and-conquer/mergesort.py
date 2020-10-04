def merge(left_subarray,right_subarray):
	i,j = 0,0
	result = []

	while i<len(left_subarray) and j<len(right_subarray):
		if left_subarray[i] <= right_subarray[j]:
			result.append(left_subarray[i])
			i += 1
		else:
			result.append(right_subarray[j])
			j += 1
	result += left_subarray[i:]
	result += right_subarray[j:]
	return result

def merge_sort(input_list):
	if len(input_list) <= 1:
		return input_list
	else:
		midpoint = int(len(input_list)/2)
		left_subarray = merge_sort(input_list[:midpoint])
		right_subarray = merge_sort(input_list[midpoint:])
		return merge(left_subarray,right_subarray)

number_list = [8, 3, 1, 10, 111, 56, 999, 2]
print merge_sort(number_list)