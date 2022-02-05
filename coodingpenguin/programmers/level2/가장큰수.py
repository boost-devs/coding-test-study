def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key=lambda x: x * 3, reverse=True)
    result = "".join(nums)
    if result.count("0") == len(result):
        return "0"
    return "".join(nums)
