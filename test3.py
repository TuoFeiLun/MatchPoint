from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
import time
import tkinter.messagebox
import tkinter.scrolledtext
class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("this is a variable")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

    def print_contents(self, event):
        print("hi. contents of entry is now ---->",
              self.contents.get())


# root = Tk()
#
# st =scrolledtext.ScrolledText(root)
# st.insert( END , [1,2,3,4])
# st.insert(END ,"11111")
# #st.delete(1.0, END) # 使用 delete
# st.pack()
#
# root.mainloop()
def increment():
    try:
        for i in range(100):
            p1['value'] = i+1
            root.update()
            time.sleep(0.01)
        for i in range(0, 100):
            scrt.insert(END, i)
            #time.sleep(0.01)
            root.update()
            for j in 'okaoskdmaskdmrtmczodmpsa':
                scrt.insert(END, j)
                scrt.insert(END, '\n')
                #
            scrt.see(END)
    except(TclError):
         tkinter.messagebox.showinfo("Stop")
         p1.stop()

if __name__ == "__main__":


    root = Tk()
    root.geometry('1000x800')
    p1 = ttk.Progressbar(root, length=100, mode="determinate", maximum=100, orient=HORIZONTAL)
    p1.grid(row=1, column=1)
    b1 = Button(root, text="start", command=increment)
    b1.grid(row=1, column=0)
    scrt = scrolledtext.ScrolledText(root)
    scrt.grid(row=2,column = 1)
    a = [1,2,3,4]
    b = [2,3,2,[1,[1,1111, '\n'], 2]]
    scrt.insert(END,a)

    scrt.insert(END, b)
    root.mainloop()


