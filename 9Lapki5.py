'''Анаграмма -- это слово, образованное с помощью перестановки букв другого слова.

Напишите функцию is_anagram, которая принимает на вход две строки и возвращает True, если одна строка является анаграммой другой.

Sample Input:

listen silent
Sample Output:

True'''
first_word, second_word = input().split()

def is_anagram(first_word, second_word):
    first_sp = sorted(list(first_word))
    second_sp = sorted(list(second_word))

    if first_sp == second_sp:
        sum_list = True
    else:
        sum_list = False
    return sum_list

result = is_anagram(first_word, second_word)
print(result)
