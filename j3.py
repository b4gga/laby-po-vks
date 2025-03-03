numbers = set(range(10, 24))
result_dict = {
    num: num * 2 if num % 3 == 0 else num + 6
    for num in numbers
}
print(result_dict)
value_list = list(result_dict.values())
print(value_list)
value_list.sort()
print(value_list)