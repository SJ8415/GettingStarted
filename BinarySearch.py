#Sean Johnston 10/19/19
#BubbleSort and BinarySearch

nums_string = input("Please enter a list of numbers separating each by a space: ")
nums = nums_string.split()

target = input("Please enter the number you would like to find: ")

#Convert all input to integers
for h in range(len(nums)):
    nums[h] = int(nums[h])
target = int(target)

def sort(nums): 
    nums = list(set(nums)) #remove dulicates
    for j in range(len(nums)):
        for i in range(len(nums)-j -1):
            if nums[i] > nums[i+1]:
                temp = nums[i+1]
                nums[i+1]= nums[i]
                nums[i] = temp
    return nums
nums = sort(nums)           

def search(nums, target):    
    max = len(nums)
    min = 0
    if len(nums) == 0 or target > nums[max-1] or target < nums[min]:
        return -1
    for j in range(int((len(nums))/2 +1)):
        i = int((min + max)/2)
        if nums[i] == target:
            return i;
        elif nums[i] > target:
            max = i-1
        else:
            min = i+1
    return -1

ans = search(nums, target)
if ans == -1:
    print('This number does not exist in the list you entered.')
else:
    print('The location of this number in your list is', ans)
    
