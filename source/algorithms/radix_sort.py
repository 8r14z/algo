import math
def countingSort(nums: [int], d: int, base: int):
    count = [[]] * base
    n = len(nums)
    for num in nums:
        countIndex = (num // (base ** (d-1))) % base
        if len(count[countIndex]) == 0:
            count[countIndex] = [num]
        else:
            count[countIndex].append(num)

    output = []
    for i in range(base):
        if len(count[i]) > 0:
            output += count[i]

    return output


def radixSort(nums: [int]) -> [int]:
    max = float('-inf')
    base = 10
    for num in nums:
        if num > max:
            max = num
    
    digits = int(math.log10(max)) + 1

    for d in range(1, digits+1):
        nums = countingSort(nums, d, base)
        print(nums)

    return nums


radixSort([329, 457, 657, 839, 436, 720, 355])