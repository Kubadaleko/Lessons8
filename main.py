# Напишите функцию read_last(lines, file), которая будет открывать определенный
#  файл file и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела


def read_last(lines, file):
    with open(file, 'r', encoding='utf-8') as f:
        if lines > 0:
            info = f.read().splitlines()
            for i in info[len(info) - lines:len(info)]:
                print(i)
        else:
            print('Введите целое положительное число: ')


read_last(int(input('Введите целое положительное число: ')), 'article.txt')

# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file), которая
# записывает в файл result.txt слово, имеющее максимальную длину
# (или список слов, если таковых несколько).


def longest_words(file, file_w):
    with open(file, 'r', encoding='utf-8') as f:
        with open(file_w, 'w', encoding='utf-8') as f_w:
            info = f.read().split()
            maxx = info[0]
            for i in range(len(info)):
                if len(info[i]) > len(maxx):
                    f_w.write(info[i] + '\n')


longest_words('article.txt', 'result.txt')
