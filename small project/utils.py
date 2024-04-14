def find_max(numbers):
    maximum = numbers[0]
    # 0 is for ground zero
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
