print("hello")


def largest_range(input_list):
    output = []
    longest_range_length = 0

    number_tracker = {}
    for number in input_list:
        number_tracker[number] = True

    for number in input_list:
        if not number_tracker[number]:
            continue
        number_tracker[number] = False
        currentLength = 1
        left = number - 1
        right = number + 1
        while left in number_tracker:
            number_tracker[left] = False
            currentLength += 1
            left -= 1
        while right in number_tracker:
            number_tracker[right] = False
            currentLength += 1
            right += 1
        if currentLength > longest_range_length:
            longest_range_length = currentLength
            output = [left + 1, right - 1]
    return output


x = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

print(largest_range(x))
print(largest_range([1, 2, 3, 4]))
print(largest_range([0, 0]))
print(largest_range([]))
print(largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
