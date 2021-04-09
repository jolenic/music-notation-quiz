
import random
from Question import Question
from flask import Flask, render_template, request

app = Flask(__name__)


# defines actions for home page
@app.route("/")
def home():
    return render_template('index.html')


# Defines all questions for treble quiz, prompt is file name of .png file
treble_questions = [
  Question("c4-treble", "C"),
  Question("d4", "D"),
  Question("e4", "E"),
  Question("f4", "F"),
  Question("g4", "G"),
  Question("a5", "A"),
  Question("b5", "B"),
  Question("c5", "C"),
  Question("d5", "D"),
  Question("e5", "E"),
  Question("f5", "F"),
  Question("g5", "G"),
  Question("a6", "A"),
  Question("b6", "B"),
  Question("c6", "C")
]


# Defines all questions for bass quiz
bass_questions = [
  Question("c2", "C"),
  Question("d2", "D"),
  Question("e2", "E"),
  Question("f2", "F"),
  Question("g2", "G"),
  Question("a3", "A"),
  Question("b3", "B"),
  Question("c3", "C"),
  Question("d3", "D"),
  Question("e3", "E"),
  Question("f3", "F"),
  Question("g3", "G"),
  Question("a4", "A"),
  Question("b4", "B"),
  Question("c4-bass", "C")
]

# defines all questions for all notes quiz - combines treble and bass questions
all_questions = treble_questions + bass_questions

# creates empty array to store most recent set of questions used
quiz_questions = []


# defines actions for treble-quiz
@app.route("/treble-quiz")
def treble_quiz():
    # shuffles questions and passes first 10 to quiz_questions
    random.shuffle(treble_questions)
    global quiz_questions
    quiz_questions = treble_questions[0:10]
    # passes data and renders html template
    title = "Treble Notes Quiz"
    return render_template('notes-quiz.html', q=quiz_questions, title=title)


# defines actions for bass-quiz
@app.route("/bass-quiz")
def bass_quiz():
    # shuffles questions and passes first 10 to quiz_questions
    random.shuffle(bass_questions)
    global quiz_questions
    quiz_questions = bass_questions[0:10]
    # passes data and renders html template
    title = "Bass Notes Quiz"
    return render_template('notes-quiz.html', q=quiz_questions, title=title)


# defines actions for all-quiz
@app.route("/all-quiz")
def all_quiz():
    # shuffles questions and passes first 10 to quiz_questions
    random.shuffle(all_questions)
    global quiz_questions
    quiz_questions = all_questions[0:10]
    # passes data and renders html template
    title = "All Notes Quiz"
    return render_template('notes-quiz.html', q=quiz_questions, title=title)


# defines actions for results
@app.route('/results', methods=['POST'])
def quiz_answers():
    correct = 0
    total = 0
    # reads user answers and checks against Question object's answer
    for i in quiz_questions:
        answered = request.form[i.prompt]
        i.response = answered
        # adds up total correct answers
        if quiz_questions[total].answer == answered:
            correct = correct+1
        total += 1
    # passes data and renders html template
    return render_template('results.html', q=quiz_questions, correct=correct)


# runs application and turns on debug mode
if __name__ == "__main__":
    app.run(debug=True)
