str = "Лабораторная номер Один пункт Пять"
def filter_and_sort_words(stroka2):
    words = stroka2.split()
    filtered_words = list(
        filter(lambda word: word[0].islower(), words)
        )
    sorted_words = sorted(filtered_words, reverse=True)
    print (sorted_words)
    return sorted_words
filter_and_sort_words (str)