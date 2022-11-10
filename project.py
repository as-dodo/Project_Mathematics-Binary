from gametasks import *
from gameclasses import *

try:
    math_instructions = 'В этой игре вам предлагается решить простую арифметическую задачу.\nЗа каждый правильный ответ вам начисляется одно очко.\nЗа ошибочные ответы очки не вычитаются.'
    binary_instructions = 'В этой игре вы получаете десятичное число.\nВаша задача — преобразовать его в двоичную систему счисления.\nЗа каждый правильный ответ вам начисляется одно очко.\nЗа ошибочные ответы очки не вычитаются.'
    bg = Binary()
    mg = MathGame()
    user_name = input('Enter your name: ')
    score = int(get_user_score(user_name))
    is_new_user = False
    if score == -1:
        is_new_user = True
        score = 0
    print(f'Hello, {user_name}! Your score is {score}')

    user_choice = 0

    while user_choice != '-1':
        game = input('Which game would you like to play: Math Game (enter: 1) or Binary Game (enter: 2)? ')

        while game != '1' and game != '2':
            game = input('Enter a number: 1 (if you want to play Math Game) or 2 (if you want to play Binary game) ')

        num_prompt = input('How many questions do you want per game (1 to 10)? ')

        while True:
            try:
                num = int(num_prompt)
                break
            except:
                num_prompt = input('You didn\'t enter eligible number. Please try again: Enter a number from 1 to 10: ')

        if game == '1':
            mg.no_of_questions = num
            print_instructions(math_instructions)
            current_score = mg.generate_questions()
            score += current_score
        else:
            bg.no_of_questions = num
            print_instructions(binary_instructions)
            current_score = bg.generate_questions()
            score += current_score
        user_choice = input(f'Your new total score is {score}.\nPush Enter button to play more or enter "-1" to exit the game: ')

    update_user_score(is_new_user, user_name, str(score))

except Exception as e:
    print('Unexpected error!')
    print(f'Error: {e}')
