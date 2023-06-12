def change_numbers(x: str) -> int:
    x = int(x)
    if x % 2 == 0:
        return x // 2
    else:
        return x * x

a = map(change_numbers, input().split())

print(*a)