nums = list(map(int, open("58484.txt").readlines()))
min_num=0
for num in nums:
    if len(str(num)) == 4 and num % 10 == 5:
        min_num=min(min_num, num)

count = 0
m = 0
for i in range(0,  len(nums) - 1):
    if ((len(str(nums[i]))) == 4) and (len(str(nums[i+1])) == 4) and (nums[i] ** 2 + nums[i +1] ** 2) % min_num == 0 :
        count +=1
        m = max(m, nums[i] ** 2 + nums[i+1] **2)
print(count , m)