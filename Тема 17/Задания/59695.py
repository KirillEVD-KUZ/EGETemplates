nums = list(map(int, open("59695.txt").readlines()))
max_num = 0
for num in nums:
    if num % 100 == 15:
        max_num = max(max_num, num)
count = 0
m = 0
for i in range(len(nums) - 2):
    if (int(len(str(nums[i])) == 4) + int(len(str(nums[i + 1])) == 4) + int(len(str(nums[i + 2])) == 4)) == 1 and (
            nums[i] + nums[i + 1] + nums[i + 2]) >= max_num:
        count += 1
        m = max(m, nums[i] + nums[i + 1] + nums[i + 2])
print(count, m)
