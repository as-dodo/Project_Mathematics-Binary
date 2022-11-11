from os import remove, rename


# Вывод инструкций
def print_instructions(instruction):
    print(instruction)


# Получение счета пользователя
"""Функция проверяет есть ли, переданный user_name в строках файла,
если есть - то выводит его score, если нет - то, выводит -1.
"""


def get_user_score(user_name):
    user_score = -1
    path = '/Users/anastasia/PycharmProjects/Math_project/user_scores.txt'
    try:
        file = open(path, 'r')

        for line in file:
            user_info = line.strip().replace(' ', '').split(',')
            if user_name in line:
                user_score = user_info[1]
                break
        file.close()

    except IOError:
        print('Файл не найден')
        file = open(path, 'w')
        file.close()

    return user_score


# get_user_score('Ann')

# Обновление счета пользователя
"""Функция проверяет, передается ли информация о новом юзере:
если да, то добавляется строка в файл с его данными, 
если нет,  необходимо перезаписать в файле score этого юзера на переданный в функции.
"""


def update_user_score(is_new_user, user_name, score):
    old_path = '/Users/anastasia/PycharmProjects/Math_project/user_scores.txt'
    temp_path = '/Users/anastasia/PycharmProjects/Math_project/user_scores.tmp'
    if is_new_user:
        file = open(old_path, 'a')
        file.write(f'{user_name}, {score}\n')
        file.close()
    else:
        temp_file = open(temp_path, 'w')
        file = open(old_path, 'r')
        for line in file:
            if user_name in line:
                temp_file.write(f'{user_name}, {score}\n')
            else:
                temp_file.write(line)

        temp_file.close()
        file.close()
        remove(old_path)
        rename(temp_path, old_path)

# update_user_score(True, 'Ilya', 555)
# update_user_score(False, 'Ann', 777)
