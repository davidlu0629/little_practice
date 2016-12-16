def twosum(nums, target):
    if len(nums)<=1:
        return False
    buf_dict={}
    for i in range(len(nums)):
        if nums[i] in buf_dict:
            return [nums[buf_dict[nums[i]]], nums[i]]
        else:
            buf_dict[target-nums[i]]=i

r=twosum([1,3,7,8,10],10)
print(r)
