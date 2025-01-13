nums = list(map(int, open("373721.txt").readlines()))
m = 0
count = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if ((nums[i] - nums[j]) % 45 == 0) and (nums[i] % 18 == 0 or nums[j] % 18 == 0):
            count += 1
            m = max(m, abs(nums[i] - nums[j]))
print(count, m)
