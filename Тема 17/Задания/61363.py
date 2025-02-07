nums=list(map(int,open("17.txt").readlines()))
max=0
for num in nums:
    if num>max:
        max=num

count=0
max1=0
for i in range(len(nums)-2):
    if (nums[i] % 3==0 or nums[i +1] % 3==0 or nums[i+2] % 3==0) and (nums[i]+nums[i+1]+nums[i+2] > max) and ((int(len(str(nums[i])) ==4) + int(len(str(nums[i+1])) ==4) + int(len(str(nums[i+2])) ==4)) == 2 ):
        count+=1
        sum=nums[i]+nums[i+1]+nums[i+2]
        if sum>max1:
            max1=sum
print(count, max1)
