from tkinter import *

canvas_height = 400
canvas_width = 600
canvas_color = "black"

window = Tk()
window.title("마음대로 그려 보세요")
# canvas = Canvas(bg=canvas_color, height=canvas_height, width=canvas_width, highlightthickness=0)
# canvas.pack()

Label(window,text="이름머고?").grid(row=0,column=0,sticky=W)
entry = Entry(window,width=20,bg="light green")
entry.grid(row=1,column=0,sticky=W)
output = Text(window, width=75,height=6,wrap=WORD,background="light green")
output.grid(row=4,column=0,columnspan=2,sticky=W)

def click():
    a = entry.get()
    output.insert(END,a+"\n")
    entry.delete(0,END)


Button(window,text="확인",width=5,command=click).grid(row=2,column=0,sticky=W)

window.mainloop()

# 문제
# 컴퓨터가 생각하고 있는 1~100까지의 숫자를 알아 맞추는 프로그램을 GUI로 작성해 봅니다.










