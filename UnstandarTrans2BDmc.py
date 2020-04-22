from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog as tkinter_file
from tkinter import ttk
import Batch_read_trans_baidu
import ConstantParameters
import time
class UnstandarTransGUI(Toplevel):

    def __init__(self, master=None):
        super().__init__(master)

        self.grid()
        self.open_filename_load = StringVar()

        self.filename_entry = Entry(self,width=135)
        self.filename_entry.grid(row=0, column=0, sticky=N)
        self.filename_entry["textvariable"] = self.open_filename_load

        self.entry_load = Button(self, text="load", command=self.load)
        self.entry_load.grid(row=0, column=1, sticky=N)

        self.entry_save = Button(self, text='save', command=self.save)
        self.entry_save.grid(row=0, column=2, sticky=N)

        self.contents = ScrolledText(self,width = 60,height=30)
        self.contents.grid(row=2, column=0, sticky=W)
        self.contents_transed = ScrolledText(self, width=60, height=30)
        self.contents_transed.grid(row=2, column=0, sticky=E)

        self.transbutton = Button(self, text="转换", command=self.trans)
        self.transbutton.grid(row=2, column=1, sticky=N)
    def load(self):
        open_filename = tkinter_file.askopenfilename(initialdir="/", title="Select file",
                                     filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        print(open_filename)

        read_path = open_filename.replace('/',"\\\\")
        self.open_filename_load.set(read_path)
        print(read_path)
        # 读取需要转换的数据
        ConstantParameters.model_regulator_data = Batch_read_trans_baidu.read_model_regulator(read_path)

        for a_list in ConstantParameters.model_regulator_data:
            for one in a_list:
                self.contents.insert(END,str(one))
                self.contents.insert(END, ';')

            self.contents.insert('end','\n')

            self.contents.see(END)
            time.sleep(0.01)
            super().update()
    def save(self):
        pass

    def trans(self):
        four_params = ConstantParameters.four_trans_parameters
        wkid = ConstantParameters.trans_wkid
        print(four_params, wkid)
        print(ConstantParameters.model_regulator_data)
        save_regulator_lists = []
        for one in ConstantParameters.model_regulator_data:
            one_reg_list = Batch_read_trans_baidu.trans_regulator_to_baidu_special_coordinate(one, wkid, four_params)
            for one_char in one_reg_list:
                self.contents_transed.insert(END, one_char)
                self.contents_transed.insert(END, ';')

            self.contents_transed.insert(END, '\n')
            self.contents_transed.see(END)
            super().update()
            save_regulator_lists.append(one_reg_list)

        path = self.open_filename_load.get()
        # 保存路径
        Batch_read_trans_baidu.save_transed(save_regulator_lists,path)

if __name__ ==  "__main__":
    new_window_trans = UnstandarTransGUI()

    new_window_trans.title("非标准转墨卡托")
    new_window_trans.geometry('1200x500')

    new_window_trans.mainloop()





