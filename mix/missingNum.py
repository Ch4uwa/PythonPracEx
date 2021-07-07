nums = [6, 3, 2, 4, 3, 1]


def getDuplicates(nums):
    nums.sort()
    seen = set()
    for i in nums:
        if i in seen:
            dup = i
        else:
            seen.add(i)

    return dup


def getMissing(nums):
    nums.sort()
    for item in range(nums[0], nums[-1]):
        if item not in nums:
            return item


if __name__ == '__main__':
    print(f'Missing number: {getMissing(nums)}')
    print(f'Duplicate number: {getDuplicates(nums)}')
    print(
        f'Sum of missing and duplicate: {getMissing(nums) + getDuplicates(nums)}')
