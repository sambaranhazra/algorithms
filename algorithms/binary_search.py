def search(nums: list, target: int):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    nums = [1, 2, 3, 4, 100]
    target = 100
    print(search(nums, target))


if __name__ == "__main__":
    main()
