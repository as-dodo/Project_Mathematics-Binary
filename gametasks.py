from os import remove, rename


# Вывод инструкций
def print_instructions(instruction):
    print(instruction)


# Получение счета пользователя

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

def update_user_score(is_new_user, user_name, score):
    old_path = '/Users/anastasia/PycharmProjects/Math_project/user_scores.txt'
    temp_path = '/Users/anastasia/PycharmProjects/Math_project/user_scores.tmp'
    if is_new_user:
        file = open(old_path, 'a')
        file.write(f'\n{user_name}, {score}')
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


# def get_user_score(user_name):
#     try:
#         file = open('/Users/anastasia/PycharmProjects/Math_project/user_scores.txt', 'r')
#         user_score = -1
#         for line in file:
#             user_info = line.strip().replace(' ', '').split(',')
#             if user_name in line:
#                 user_score = user_info[1]
#                 break

#
#         file.close()
#         return user_score
#
#     except IOError:
#         print('Файл не найден')
#         file = open('/Users/anastasia/PycharmProjects/Math_project/user_scores.txt', 'w')
#         file.close()
#         return -1


# score = get_user_score('Darren')
# print(score)

# Обновление счета пользователя


# def update_user_score(new_user, user_name, score):
#     if new_user:
#         file = open('/Users/anastasia/PycharmProjects/Math_project/user_scores.txt', 'a')
#         file.write(f'\n{user_name}, {score}')
#         file.close()
#     else:
#         temp_file = open('/Users/anastasia/PycharmProjects/Math_project/user_scores.tmp', 'w')
#         file = open('/Users/anastasia/PycharmProjects/Math_project/user_scores.txt', 'r')
#         for line in file:
#             temp_file.write(line)
#             if get_user_score(user_name) != -1:
#                 temp_file.write(f'{user_name}, {score}')
#                 continue

        # for line in file:
        #     user_info = line.split(',')
        #     user_info[1] = user_info[1].replace('\n', '')
        #     # content.append(user_info)
        #     if user_name in user_info:
        #         user_info[1] = score
        #         temp_file.write(f'\n{user_name}, {user_info[1]}')
        #     else:
        #         temp_file.write(f'\n{user_info[0]}, {user_info[1]}')

        # temp_file.close()
        # file.close()
        # remove('/Users/anastasia/PycharmProjects/Math_project/user_scores.txt')
        # rename('/Users/anastasia/PycharmProjects/Math_project/user_scores.tmp',
        #        '/Users/anastasia/PycharmProjects/Math_project/user_scores.txt')


# update_user_score(False, 'Ann', 555)
