from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QPushButton, QGroupBox, QButtonGroup

class Questions():
    def __init__(self, questions, right_answer, wrong_1, wrong_2, wrong_3):
        self.questions = questions
        self. right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    text1.setText(q.questions)
    text3.setText(q.right_answer)
    show_quest()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.answers += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно')

def next_question():
    main_win.counter += 1
    print('Статистика всех вопросов:', main_win.counter)
    print('Правильных ответов:', main_win.answers)
    print('Рейтинг:', int(main_win.answers/main_win.counter*100))

    result = 'Статистика всех вопросов: ' + str(main_win.counter) + '\n'
    result += 'Правильных ответов: ' + str(main_win.answers) + '\n'
    result += 'Рейтинг: ' + str(round(main_win.answers/main_win.counter*100, 2)) + '%'

    if main_win.counter < len(questions_list):
        ask(questions_list[main_win.counter])
    else:
        dop_w = QMessageBox()
        dop_w.setWindowTitle('Результаты:')
        dop_w.setText(result)
        dop_w.exec_()
    

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def show_correct(res):
    text2.setText(res)
    show_result()
    

def show_quest():
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    AnswerGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')

def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    button.setText('Следующий вопрос')


def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_quest()

app = QApplication([])
main_win = QWidget()
main_win.counter = 0
main_win.answers = 0
main_win.setWindowTitle('Memory Card')
main_win.resize(400,200)
text1 = QLabel('Какой национальности не существует?')


button = QPushButton('Ответить')
button.clicked.connect(click_ok)

RadioGroupBox = QGroupBox('Варианты ответов')
AnswerGroupBox = QGroupBox('Результата теста')
RadioGroup = QButtonGroup()

text2 = QLabel('Правильно/Неправильно')
text3 = QLabel('Правильный ответ')
layoutAnsBox = QVBoxLayout()

layoutAnsBox.addWidget(text2, alignment=(Qt.AlignLeft | Qt.AlignTop))
layoutAnsBox.addWidget(text3, alignment=Qt.AlignCenter)

AnswerGroupBox.setLayout(layoutAnsBox)
AnswerGroupBox.hide()

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
answers = [rbtn_1, rbtn_2, rbtn_3 ,rbtn_4]

q1 = Questions('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Бразильский','Итальянский')

questions_list = []
q2 = Questions('Какого цвета нет на флаге России?','Зелёный','Красный','Белый','Синий')
q3 = Questions('Национальная хижина якутов','Ураса','Юрта','Иглу','Хата')
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
shuffle(questions_list)
ask(questions_list[0])

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(rbtn_1)
layout2.addWidget(rbtn_2)
layout3.addWidget(rbtn_3)
layout3.addWidget(rbtn_4)
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout1.addLayout(layout2)
layout1.addLayout(layout3)

RadioGroupBox.setLayout(layout1)

layout4 = QHBoxLayout()
layout5 = QHBoxLayout()
layout6 = QHBoxLayout()

layout4.addWidget(text1, alignment = Qt.AlignHCenter)
layout5.addWidget(RadioGroupBox)
layout5.addWidget(AnswerGroupBox)
layout6.addStretch(10)
layout6.addWidget(button, stretch=20) 
layout6.addStretch(10)
layout7 = QVBoxLayout()
layout7.addLayout(layout4)
layout7.addLayout(layout5)
layout7.addLayout(layout6)
main_win.setLayout(layout7)

main_win.show()
app.exec_()
