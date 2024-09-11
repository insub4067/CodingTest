# 직각삼각형(기본수학)
while True:
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break
    nums.sort()
    if nums[0]**2 + nums[1]**2 == nums[2]**2:
        print("right")
    else:
        print("wrong")