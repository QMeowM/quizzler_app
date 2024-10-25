from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz):
        self.quiz = QuizBrain(quiz)
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        #we are using the following somewhere else, so assign it a name
        self.question_text = self.canvas.create_text(150, 125, text="QuestionQuestionQuestionQuestionQuestion",
                                                     width=250, fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_image = PhotoImage(file="images/true.png")
        incorrect_image = PhotoImage(file="images/false.png")
        self.correct_button = Button(image=correct_image, command=self.true_pressed, highlightbackground=THEME_COLOR)
        self.correct_button.grid(row=2, column=0)
        self.incorrect_button = Button(image=incorrect_image, command=self.false_pressed, highlightbackground=THEME_COLOR)
        self.incorrect_button.grid(row=2, column=1)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def disable_buttons(self):
        self.correct_button.config(state="disabled")
        self.incorrect_button.config(state="disabled")

    def get_next_question(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        self.correct_button.config(state="active")
        self.incorrect_button.config(state="active")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz. Hooray!")
            self.disable_buttons()

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        # self.scoring()

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.disable_buttons()
        self.window.after(1000, self.get_next_question)

