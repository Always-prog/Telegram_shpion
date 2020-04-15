import telebot as TL
from PyQt5.QtWidgets import QMessageBox
import PyQt5
import sys
from tkinter import *
from pyautogui import screenshot


token = input("введите токен бота: ")



def vopros(mess,msg):
    def ok_btn(entr,msg,root):
        msg = msg
        root = root
        msg("ответ: "+entr.get())
        root.destroy()
    root = Tk()
    root.geometry("200x200")
    root.attributes("-fullscreen",True)
    root.lift()
    lab = Label(root,text=mess)
    entr = Entry(root)
    btn_ok = Button(text="Ответить",command=lambda: ok_btn(entr,msg,root))
    lab.pack()
    entr.pack()
    btn_ok.pack()
    root.mainloop()


def msg_mean(mess):
    newApp = PyQt5.QtWidgets.QApplication(sys.argv)
    msg = QMessageBox()
    msg.setWindowTitle("сообщение")
    msg.setText(mess)
    msg.setIcon(QMessageBox.Critical)
    x = msg.exec_()

bot = TL.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, началось :)')

@bot.message_handler(content_types=['text'])
def send_text(message):
    def msg(message_text):
        bot.send_message(message.chat.id, str(message_text))
    def snd_doc(name_doc):
        bot.send_document(message.chat.id, open(name_doc,"rb"))
    if message.text[:6] == "вопрос":
        vopros(message.text,msg)
    else:
        if message.text == "s":
            screen = screenshot('muzik.jpg')
            snd_doc("muzik.jpg")
        else:
            msg_mean(message.text)


while True:
    try:
        bot.polling()
    except(BaseException):
        pass
