import tkinter as tk
from tkinter import messagebox
import random

import UAS_PBO.LoginApp as app_login
####################### class #######################
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    
    def check_answer(self, given_answer):
        return given_answer.lower() == self.answer.lower()
    
    def display(self):
        raise NotImplementedError("This method should be overridden in subclasses")

class SaintekQuestion(Question):
    def __init__(self, prompt, choices, answer):
        super().__init__(prompt, answer)
        self.choices = choices
    
    def display(self):
        print(f"Saintek: {self.prompt}")
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")

class SoshumQuestion(Question):
    def __init__(self, prompt, choices, answer):
        super().__init__(prompt, answer)
        self.choices = choices
    
    def display(self):
        print(f"Soshum: {self.prompt}")
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")

class TPAQuestion(Question):
    def __init__(self, prompt, choices, answer):
        super().__init__(prompt, answer)
        self.choices = choices
    
    def display(self):
        print(f"TPA: {self.prompt}")
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
    
    def add_question(self, question):
        self.questions.append(question)
    
    def start(self):
        random.shuffle(self.questions)
        for question in self.questions:
            question.display()
            answer = input("Your answer: ")
            if question.check_answer(answer):
                print("Correct!")
                self.score += 1
            else:
                print("Wrong!")
        print(f"Your final score is: {self.score} out of {len(self.questions)}")

class Participant:
    def __init__(self, username, password, name, prodi, score, ):
        self.name = name
        self.score = score
    
    def update_score(self, score):
        self.score = score

###################### method ######################
def open_loginapp():
    app_login.start()

def makeQuiz(quiz):
    Quiz

####################### main #######################

open_loginapp()





