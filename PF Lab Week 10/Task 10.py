def maximum(lst):

    if len(lst) == 1:
        return lst[0]

    max_value = maximum(lst[1:])

    if lst[0] > max_value:
        return lst[0]
    else:
        return max_value

numbers = [12, 45, 7, 89, 23]

print("Largest Number =", maximum(numbers))