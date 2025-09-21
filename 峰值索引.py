def find_peak_with_largest_index(nums):
    peak_indices = []

    for i in range(len(nums)):
        # First element is a peak if it's greater than the next element
        if i == 0:
            if len(nums) == 1 or nums[i] > nums[i + 1]:
                peak_indices.append(i)
        # Last element is a peak if it's greater than the previous element
        elif i == len(nums) - 1:
            if nums[i] > nums[i - 1]:
                peak_indices.append(i)
        # Middle element is a peak if it's greater than both adjacent elements
        else:
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                peak_indices.append(i)
    return peak_indices

    # print(peak_indices)
    # max = nums[peak_indices[0]]
    # indice = peak_indices[0]
    # for index, num in enumerate(peak_indices):
    #     if index > 0:
    #         if nums[num] > max:
    #             max = nums[num]
    #             indice = peak_indices[index]
    # return indice


def find_peak_with_largest_index2(nums1):
    max = nums[nums1[0]]
    index = 0
    for num in nums1:
        if nums[num] > max:
            max = nums[num]
            index = num
    return index

# Read input and process
nums = [int(i) for i in input().split()]
new_nums = find_peak_with_largest_index(nums)

print(find_peak_with_largest_index2(new_nums))
