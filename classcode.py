from abc import ABC, abstractmethod
import random

class Game:
    def __init__(self, story):
        self.story = story
        self.levels = []

    def add_level(self, level):
        self.levels.append(level)

    def start(self):
        print("Игра началась. ", self.story)
        for level in self.levels:
            level.play_level()
        print("Игра завершилась.")

class Level(ABC):
    def __init__(self, questions):
        self.questions = questions

    @abstractmethod
    def play_level(self):
        pass

class MultipleChoiceLevel(Level):
    def play_level(self):
        print("Уровень: выбор ответа из предложенных.")
        for question in self.questions:
            print(question.get_question_text())
            print("Варианты ответа:", question.get_answer_options())
            user_answer = input("Введите ваш ответ: ")
            if user_answer == question.get_correct_answer():
                print("Правильно!")
            else:
                print("Неправильно. Правильный ответ:", question.get_correct_answer())

class TextEntryLevel(Level):
    def play_level(self):
        print("Уровень: введите ответ.")
        for question in self.questions:
            print(question.get_question_text())
            user_answer = input("Введите ваш ответ: ")
            if user_answer == question.get_correct_answer():
                print("Правильно!")
            else:
                print("Неправильно. Правильный ответ:", question.get_correct_answer())

class TimedLevel(Level):
    def play_level(self):
        print("Уровень: дайте ответ за определенное время.")
        for question in self.questions:
            print(question.get_question_text())
            print("Время на ответ:", question.get_time_limit(), "секунд")
            user_answer = input("Введите ваш ответ: ")
            if user_answer == question.get_correct_answer():
                print("Правильно!")
            else:
                print("Неправильно. Правильный ответ:", question.get_correct_answer())

class Question:
    def __init__(self, question_text, correct_answer, answer_options=None, time_limit=None):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.answer_options = answer_options
        self.time_limit = time_limit

    def get_question_text(self):
        return self.question_text

    def get_correct_answer(self):
        return self.correct_answer

    def get_answer_options(self):
        return self.answer_options

    def get_time_limit(self):
        return self.time_limit

# Создание игры и уровней
game = Game("Сюжет игры: математические задачки для малышей")
level1_questions = [
    Question("2 + 2?", "4", answer_options=["3", "4", "5"]),
    Question("5 * 5?", "25", answer_options=["20", "25", "30"])
]
level2_questions = [
    Question("3 + 3", "6"),
    Question("8 - 2", "6")
]
level3_questions = [
    Question("10 - 5?", "5", time_limit=5),
    Question("3 * 3?", "9", time_limit=8)
]

level1 = MultipleChoiceLevel(level1_questions)
level2 = TextEntryLevel(level2_questions)
level3 = TimedLevel(level3_questions)

game.add_level(level1)
game.add_level(level2)
game.add_level(level3)

game.start()
