numbers = set(range(10, 24))
result_dict = {
    num: num * 2 if num % 3 == 0 else num + 6
    for num in numbers
}
print(result_dict)