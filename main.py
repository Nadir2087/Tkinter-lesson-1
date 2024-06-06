from tkinter import *
root = Tk()
# root.iconbitmap("game_gamepad_casino_play_gaming_sport_controller_console_icon_262407.ico")
icon_photo = PhotoImage(file="Nadirbek.png")

root.iconphoto(False, icon_photo)

root.geometry('300x300')
root.resizable(width=False, height=True)
root.title('Nadirbek')

count = IntVar()
count.set(0)

def update_data():
    value = count.get()
    count.set(value+1)

btn = Button(root, text='+', command=update_data)
label = Label(root, textvariable=count)
btn.pack()
label.pack()


root.mainloop()