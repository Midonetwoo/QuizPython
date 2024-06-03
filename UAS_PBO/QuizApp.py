import tkinter as tk
from tkinter import messagebox
import threading
import time

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.root.title("Quiz App")
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.time_left = 0
        
        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.time_label = tk.Label(root, text="", font=("Arial", 12))
        self.time_label.pack(pady=10)
        
        self.answer_entry = tk.Entry(root, font=("Arial", 12))
        self.answer_entry.pack(pady=10)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=20)
        
        self.show_question()
    
    def show_question(self):
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question]['question'])
            self.time_left = self.questions[self.current_question]['time']
            self.answer_entry.delete(0, tk.END)
            self.update_time()
        else:
            messagebox.showinfo("Kuis selesai", f"Kuis selesai! Skor akhir Anda adalah: {self.score}/{len(self.questions)}")
            self.root.quit()
    
    def update_time(self):
        if self.time_left > 0:
            self.time_label.config(text=f"Waktu tersisa: {self.time_left} detik")
            self.time_left -= 1
            self.root.after(1000, self.update_time)
        else:
            self.check_answer()

    def submit_answer(self):
        if self.time_left > 0:
            self.check_answer()
        else:
            messagebox.showinfo("Waktu habis", "Waktu sudah habis!")

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.questions[self.current_question]['answer'].strip().lower()
        
        if user_answer == correct_answer:
            messagebox.showinfo("Jawaban benar", "Jawaban Anda benar!")
            self.score += 1
        else:
            messagebox.showinfo("Jawaban salah", f"Jawaban salah! Jawaban yang benar adalah: {self.questions[self.current_question]['answer']}")
        
        self.current_question += 1
        self.show_question()

def start():
    root = tk.Tk()
    app = QuizApp(root, questions)
    root.mainloop()

questions = [
    {"question": "Apa ibu kota Indonesia?", "answer": "Jakarta", "time": 10},
    {"question": "Berapa hasil dari 5 + 7?", "answer": "12", "time": 5},
    {"question": "Siapa presiden pertama Indonesia?", "answer": "Soekarno", "time": 10}
]

global root



# # Contoh penggunaan
# if __name__ == "__main__":
#     q1 = SaintekQuestion(
#         "What is the chemical symbol for water?",
#         ["H2O", "O2", "CO2", "NaCl"],
#         "H2O"
#     )
    
#     q2 = SoshumQuestion(
#         "Who wrote 'Pride and Prejudice'?",
#         ["Charlotte Bronte", "Emily Bronte", "Jane Austen", "Mary Shelley"],
#         "Jane Austen"
#     )
    
#     q3 = TPAQuestion(
#         "Solve: 5 + 3 * 2 - 8 / 4",
#         "9"
#     )
    
#     quiz = Quiz()
#     quiz.add_question(q1)
#     quiz.add_question(q2)
#     quiz.add_question(q3)
    
#     participant = Participant("John Doe")
#     quiz.start()
#     participant.update_score(quiz.score)
    
#     print(f"{participant.name}'s final score: {participant.score}")