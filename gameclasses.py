class Game:
    def __init__(self, no_of_questions=0):
        self._no_of_questions = no_of_questions

    @property
    def no_of_questions(self):
        return self._no_of_questions

    @no_of_questions.setter
    def no_of_questions(self, value):
        if value < 1:
            self._no_of_questions = 1
            print("Minimum Number of Questions = 1. \nHence, number of questions will be set to 1")
        elif value > 10:
            self._no_of_questions = 10
            print("Maximum Number of Questions = 10. \nHence, number of questions will be set to 10")
        else:
            self._no_of_questions = value


# first = Game()
# first.no_of_questions = 14
# print(first.no_of_questions)

from random import randint


class Binary(Game):
    def __init__(self, no_of_questions=0):
        super().__init__(no_of_questions)

    def generate_questions(self):
        score = 0
        for i in range(self.no_of_questions):
            base10 = randint(1, 100)
            user_result = input(f'What is {base10} in binary? ')
            print(user_result)
            while True:
                try:
                    answer = int(user_result, base=2)
                    if answer == base10:
                        print('You are right!')
                        score += 1
                        break
                    else:
                        print(f'Wrong answer. The correct answer is {base10}')
                        break
                except:
                    print('There\'s been a mistake. Please enter a binary.')
                    user_result = input(f'Try again. What is {base10} in binary? ')
                    print(user_result)
        print(f'Your score is {score}')
        return score


# firstBinaryGame = Binary()
# firstBinaryGame.no_of_questions = 3
# firstBinaryGame.generate_questions()
#
class MathGame(Game):
    def __init__(self, no_of_questions=0):
        super().__init__(no_of_questions)

    def generate_questions(self):
        score = 0
        number_list = [0, 0, 0, 0, 0]
        symbol_list = ['', '', '', '']
        operator_dic = {
            1: '+',
            2: '-',
            3: '*',
            4: '**',
        }

        for i in range(self.no_of_questions):
            for j in range(len(number_list)):
                number_list[j] = randint(1, 9)
            for k in range(len(symbol_list)):
                symbol_list[k] = operator_dic[randint(1, 4)]
                if symbol_list[k] == '**' and symbol_list[k - 1] == '**':
                    symbol_list[k] = operator_dic[randint(1, 3)]
            question_string = str(number_list[0])
            for l in range(0, 4):
                question_string += symbol_list[l]
                question_string += str(number_list[l])
            # question_string = str(number_list[0]) + symbol_list[0] + str(number_list[1]) + symbol_list[1] + str(
            #     number_list[2]) + symbol_list[2] + str(number_list[3]) + symbol_list[3] + str(number_list[4])
            result = eval(question_string)
            question_string = question_string.replace('**', '^')
            user_result = input(f'Сalculate the value of the expression {question_string} ')

            while True:
                try:
                    answer = int(user_result)
                    if answer == result:
                        print('You are right!')
                        score += 1
                        break
                    else:
                        print(f'Wrong answer. The correct answer is {result}')
                        break
                except:
                    print('There\'s been a mistake. Please enter a number.')
                    user_result = input(f'Try again. What is the value of the expression {question_string}? ')
        print(score)
        return score


# firstMathGame = MathGame()
# firstMathGame.no_of_questions = 3
# firstMathGame.generate_questions()


