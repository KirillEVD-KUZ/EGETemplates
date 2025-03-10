nums = [0] * 500000000

for n in range(len(nums)):
    if n == 0:
        nums[n] = 0
    elif n % 4 < 2 and n > 0:
        nums[n] = nums[n // 4] + n % 4
    elif n % 4 >= 2:
        nums[n] = nums[n // 4] + n % 4 - 1
    if n != 0 and nums[n] == 16 and nums[n - 1] == 27:
        print(n - 1)
        break