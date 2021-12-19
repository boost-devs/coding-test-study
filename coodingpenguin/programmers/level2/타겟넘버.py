def solution(numbers, target):
    n = len(numbers)
    count = 0
    for i in range(1 << n):
        total = 0
        for j in range(n):
            # 비트가 1이면
            if i & 1 << j:
                total += numbers[j]  # 더해준다
            # 비트가 0이면
            else:
                total -= numbers[j]  # 빼준다
        # 결과가 타겟과 일치하면
        if total == target:
            count += 1  # 카운트를 +1 해준다
    return count
