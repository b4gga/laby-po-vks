text = input("Введите строку: ")
index = int(input("Введите номер элемента: "))
if index < 0 or index >= len(text):
        print("Неверный индекс!")
removed_char = text[index]
new_text = text[:index] + text[index+1:]
print(f"Удаленный символ: '{removed_char}'")