#somthing more about tuples, list, str
nums = tuple(range(1,11))
print(nums)
print(type(nums))

# nums2 = str(range(1,11))      yaise nahi kar sakte ye simply range(1,11) print karega dikto
# print(nums2)
nums2 = str((1,2,3,4,5,6,7,8,9,10))
print(nums2)
print(type(nums2))

nums3 = list(range(1,11))
print(nums3)
print(type(nums3))

nums4 = str([1,2,3,4,5,6,7,8,9,10])
print(nums4)                 #it will print but it is string[1,2,3,4,5,6,7,8,9,10]
print(type(nums4)) 

