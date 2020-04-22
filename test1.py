import tkinter as tk
from tkinter import filedialog
import os

application_window = tk.Tk()

application_window.title('My Window')

application_window.geometry('500x300')  # 这里的乘是小x

# 第4步，在图形界面上创建一个标签label用以显示并放置
var = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
l = tk.Label(application_window, bg='yellow', width=200, text='模型的坐标系')
l.pack()


# 第6步，定义选项触发函数功能
def print_selection():
    l.config(text='你选择的是 ' + var.get())


# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r1 = tk.Radiobutton(application_window, text='国际标准系', variable=var, value='国际标准系', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(application_window, text='非标准偏移系', variable=var, value='非标准偏移系', command=print_selection)
r2.pack()

var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.pack()

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')


# 第5步，在窗口界面设置放置Button按键
b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()

my_filetypes = [('all files', '.*'), ('Excel files', '.xlsx')]
'''

answer = filedialog.askopenfilename(parent=application_window,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:",
                                    filetypes=my_filetypes)
                                    
                                    '''
application_window.mainloop()