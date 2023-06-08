from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel,QButtonGroup)

from random import shuffle,randint

class Question() :
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Kad je bio prvi svjetski rat?','1914','1918','1900','2000'))
questions_list.append(Question('Kad je bio drugi svjetski rat?','1939','1940','1220','2270'))
questions_list.append(Question('Kad je bio boj na Kosovu?','1389','1100','1990','2311'))
questions_list.append(Question('Koje godine je bio zadnj krstaski rat?','1270','1222','1567','990'))
questions_list.append(Question('Kako se zvao osnivac Islama','Muhamed','Petar','Igor','Dragan'))
questions_list.append(Question('Gdje su zivjeli Arabljani?','Arablansko poluostrvu','Bijeljini','Carigradu','Vizantiji'))
questions_list.append(Question('Kad su se Huni uselili u Evropu?','375','444','666','989'))
questions_list.append(Question('Kad je palo  rimsko carstvo?','476','234','143','1298'))
questions_list.append(Question('Kad je rodjen Muhamed?','570' ,'578' ,'666','2005'))
questions_list.append(Question('Kad se desio prvo srpski ustanak?','1804','1456','1677','2056'))

app =   QApplication([])
window = QWidget()
btn_answer = QPushButton('Answer')
lb_Question = QLabel('Kako se zove nas nastavnik?')

RadioGroupBox = QGroupBox ('Answer options')
rbtn_1 = QRadioButton('Pero')
rbtn_2 = QRadioButton('Milijan')
rbtn_3 = QRadioButton('Obrad')
rbtn_4 = QRadioButton('Andjela')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Test result')
lb_result = QLabel('True/Folse')
lb_Correct = QLabel('Correct answer')

layout_result = QVBoxLayout()
layout_result.addWidget (lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget (lb_Correct, alignment=Qt.AlignHCenter ,  stretch=2 )
AnsGroupBox.setLayout(layout_result)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter ))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_answer, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

AnsGroupBox.hide()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_answer.setText('Next question')

def show_question():
    window.total +=1
    print('Statistic \n - total options:',window.total,'\n -Right answers:',window.score)
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_answer.setText('Answer')
    RadioGroup.setExclusive (False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_3.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q : Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(result):
    lb_result.setText(result)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct('Correct!')
        window.score +=1
        print('Statistic \n - total options:',window.total,'\n -Right answers:',window.score)
        print('Rating:',(window.score / window.total)*100)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                show_correct('Inccorect!')
def next_question():
    cur_question = randint(0,len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)


def click_OK(): 
    if btn_answer.text() == 'Answer':
        check_answer()
    else: 
        next_question()

btn_answer.clicked.connect(click_OK)
window.cur_question =-1

window.total = 0
window.score  = 0
next_question()



window.setLayout(layout_card)
window.show()
app.exec()