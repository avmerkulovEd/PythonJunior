'''На вход программы подается текст. Определите, какое слово в нем встречается чаще всего и напечатайте его в нижнем регистре.

Слова "the" и "The" считаются одним словом:) Если таких слов несколько, напечатайте первое в лексикографическом порядке

Sample Input:

The cat sat on the mat
Sample Output:

the'''
slova = input().split()
count = {}
max = 0
for i in range(len(slova)):
    slova[i] = slova[i].lower()
for x in range(len(slova)):
    chet = 0    
    for y in range(len(slova)):
        if slova[x] == slova [y]:
            chet += 1
            if max < chet:
                max = chet
    count.setdefault(slova[x], chet)
    
for k, v in count.items():
    if v == max:
        print(k)
        break
