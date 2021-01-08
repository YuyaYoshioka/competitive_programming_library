left=0
right=N-1
while right > left + 1:
    half = (right + left) // 2
    if numbers[half] <= number:
        right = half
    else:
        left = half
