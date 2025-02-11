# Bubble Sort

def bubble(nums):
    tamanho = len(nums)
    
    for _ in nums:
        is_sorted = True
        print(nums)
        for i in range(tamanho -1):
            if nums[i] > nums[i+1]:
                is_sorted = False
                nums[i+1], nums[i] = nums[i], nums[i+1]
        if is_sorted:
            return

bubble([5,4,3,2,1])
bubble([1,2,3,4,5])