def rotate(nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    res = []
    res.append(nums[k:])
    res.append(nums[:k])
    return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 4

    print(rotate(nums,k))