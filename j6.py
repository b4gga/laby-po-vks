start = int(input("Введите первое число списка: "))
end = int(input("Введите последнее число списка: "))
step = int(input("Введите шаг списка: "))
def process_numbers(start, end, step):
    numbers = list(range(start, end, step))
    multiples_of_6 = list(filter(lambda x: x % 6 == 0, numbers))
    count_multiples = len(multiples_of_6)
    min_number = min(numbers)
    min_cubed = min_number ** 3
    result_diff = count_multiples - min_cubed
    if result_diff < 0:
        final_list = numbers[::-1]
    else:
        final_list = [result_diff] + numbers
    print (final_list)
    return final_list
if start < 0 or end <0 or step <0:
    print("Неверный индекс! Проверьте входные данные")
else:
    end = end+1
    process_numbers (start, end, step)