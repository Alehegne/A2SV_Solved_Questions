# You are given two arrays a[] and b[], 
# return the Union of both the arrays in any order.

# The Union of two arrays is a collection of all distinct elements present in either of the arrays. 
# If an element 
# appears more than once in one or both arrays, it should be included only once in the result.

nums1=[1,2,3]
nums2=[2,3,4]
print(set(nums1) | set(nums2))