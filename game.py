import json
import random
from getting_guess import word_guess
from checking_function import check_correct
import sys
from PyQt5.QtWidgets import  QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

#PyQt5 app window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Wordle')
        self.setGeometry(700, 100, 600, 800)
        self.setWindowIcon(QIcon('wordle_emblem.jpg'))

        label = QLabel('Please Guess A Word',self)
        label.setGeometry(10,10,600,200)
        label.setFont(QFont('Arial',40))
        label.setAlignment(Qt.AlignHCenter)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()


#getting files from json & selecting word
with open('words.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
selected_word = random.choice(data)





#first guess
valid:bool = False
guess:str = word_guess(data, valid)

print(selected_word)


#main loop
while True:

    if guess == selected_word:

        print('Correct!')
        break

    else :

        print('try again')
        check_correct(guess,selected_word)
        guess:str = word_guess(data, valid)




