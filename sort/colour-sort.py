#used bubble sort first, because the question talks about space complexity and the space complexity of bubble sort is 1. It is also one pass, so satisfies the requirements of the question, assuming time complexity is not needed. 

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

random_list_of_nums = [0,2,1,2,0,0,0,2,1,2]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
