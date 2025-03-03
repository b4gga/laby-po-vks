nums1 = [1, 5, 7, 8]
nums2 = [2, 4, 9]
m = 4
n = 3
def merge_arrays(nums1, m, nums2, n):
    index1 = m-1
    index2 = n-1
    index = m + n - 1
    nums = list(range(index+1))
    while index >= 0 and index1 >= 1 and index2 >= 1:
        if index1 >= 0 and nums1[index1] > nums2[index2]:
            nums[index] = nums1[index1]
            index1 -= 1
        else:
            nums[index] = nums2[index2]
            index2 -= 1
        index -= 1
    while index2 >= 0:
        nums[index] = nums2[index2]
        index2 -= 1
        index -= 1
    while index1 >= 0:
        nums[index] = nums1[index1]
        index1 -= 1
        index -= 1
    print(nums)
merge_arrays(
    nums1=nums1,
    nums2=nums2,
    m=m,
    n=n
    )