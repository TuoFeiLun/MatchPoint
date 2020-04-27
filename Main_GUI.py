from tkinter import *
from tkinter import ttk
from TransToBaidu import *
import tkinter.messagebox
from SolveEquation import *
from UnstandarTrans2BDmc import *
from StandarTrans2BDmc import *
import ConstantParameters
'''
2 各主界面，一个是 测试模型单个 点转换为百度地图, 输入模型中的点，
 转换为百度坐标，（也是2 种标准，非国标标准，国际标准）

498000.272 ,3988538.836 qd 4549

5ef7DaH5hSFwNDNMGyVbzUCC8bBGjGGT

------
顺德
 a1 = SolveEquation.A_factor(719441.34,2517856.7, 721163.5,2543599.32)
    b1 = SolveEquation.L_factor(416677.38,2518133.12, 418589.54,2543872.7)

726043.85,2526174.92	荣华酒楼
4547 

'''


def one_point_convert():
    try:
        baidu_ak = e_ak.get()
        ConstantParameters.global_ak_code = e_ak.get()
        model_wkid = e_wkid.get()
        ConstantParameters.standard_trans_wkid = model_wkid
        transtobaidu= TransToBaiduC(baidu_ak, model_wkid)

        model_x = e1.get()
        model_y = e2.get()
        model_x_float = float(model_x)
        model_y_float = float(model_y)
        transtowgs = transtobaidu.ModelXY_2_WGS(model_x_float, model_y_float)
        baidu_lng_lat = transtobaidu.wgs84_to_bd09(transtowgs[0], transtowgs[1])
        Baidu_Lat.set(baidu_lng_lat[1])
        Baidu_Lng.set(baidu_lng_lat[0])

    except:
        tkinter.messagebox.showerror(title='Error', message='Error!')


def one_point_convert_unstd():
    try:
        modelxy_1 = str.split(e1_tab2.get(), ',')
        corresp_xy_1 = str.split(e2_tab2.get(), ',')
        modelxy_2 = str.split(e3_tab2.get(), ',')
        corresp_xy_2 = str.split(e4_tab2.get(), ',')

        modelxy_3 = str.split(e5_tab2.get(), ',')

        standard_wkid = e10_tab2.get()

        model_x_1 =float(modelxy_1[0])
        model_y_1 =float( modelxy_1[1])
        model_x_2 =float(modelxy_2[0])
        model_y_2 =float(modelxy_2[1])
        model_x_3 =float(modelxy_3[0])
        model_y_3 =float(modelxy_3[1])

        new_coor_x_1 =float(corresp_xy_1[0])
        new_coor_y_1 =float(corresp_xy_1[1])
        new_coor_x_2 =float(corresp_xy_2[0])
        new_coor_y_2 =float(corresp_xy_2[1])

        model_points = A_factor(model_x_1, model_y_1, model_x_2, model_y_2)
        correspond_points = L_factor(new_coor_x_1, new_coor_y_1,new_coor_x_2,new_coor_y_2  )
        four_parameters = solver_equation(model_points, correspond_points)
        the_third_point = CalTransformedPoint(four_parameters, model_x_3, model_y_3)
        after_deviation_std_xy.set("{0},{1}".format(round(the_third_point[0],2),round(the_third_point[1]),2))
        # 开始转
        baidu_ak = e_ak.get()
        ConstantParameters.global_ak_code = e_ak.get()

        transtobaidu = TransToBaiduC(baidu_ak, int(standard_wkid))
        transtowgs = transtobaidu.ModelXY_2_WGS(the_third_point[0], the_third_point[1])
        baidu_lng_lat = transtobaidu.wgs84_to_bd09(transtowgs[0], transtowgs[1])
        after_deviation_baidu.set("{0},{1}".format(baidu_lng_lat[0] ,baidu_lng_lat[1]) )

        ConstantParameters.four_trans_parameters = four_parameters
        ConstantParameters.trans_wkid = int(standard_wkid)
        print(ConstantParameters.four_trans_parameters,ConstantParameters.trans_wkid )
    except:

        tkinter.messagebox.showerror(title='Error', message='Error!')


def unstand_batch_trans_to_baidumc():
    new_window_trans = UnstandarTransGUI()

    new_window_trans.title("非标准转墨卡托系")
    new_window_trans.geometry('1200x500')

    new_window_trans.mainloop()
def stand_batch_trans_to_baidumc():
    standard_tans_window = StandarTransGUI()

    standard_tans_window.title("标准系转墨卡托系")
    standard_tans_window.geometry('1200x500')
    standard_tans_window.mainloop()

def tab3_Load_user_baidu():
    open_filename = tkinter_file.askopenfilename(initialdir="/", title="Select file",
                                                 filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
    print(open_filename)

    read_path = open_filename.replace('/', "\\\\")
    user_baidu_path_tab3.set(read_path)
    print(read_path)



def tab3_userbaidu_trans_baidumc():
    read_path = user_baidu_path_tab3.get()
    ConstantParameters.global_ak_code = e_ak.get()
    ConstantParameters.user_baidu_data_transed = Batch_read_trans_baidu.trans_user_to_baidu(read_path)


def tab3_load_trandsed_regulator():
    open_filename = tkinter_file.askopenfilename(initialdir="/", title="Select file",
                                                 filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
    print(open_filename)

    read_path = open_filename.replace('/', "\\\\")
    model_data_path_tab3.set(read_path)
    model_path = model_data_path_tab3.get()
    ConstantParameters.read_transed_data = Batch_read_trans_baidu.read_transed_model_data(model_path)

def tab3_Load_user_baidu_mc():
    open_filename = tkinter_file.askopenfilename(initialdir="/", title="Select file",
                                                 filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
    print(open_filename)
    read_path = open_filename.replace('/', "\\\\")
    user_baidu_path_mc_tab3.set(read_path)
    print(read_path)
    baidumc_path = user_baidu_path_mc_tab3.get()
    ConstantParameters.user_baidu_data_transed = Batch_read_trans_baidu.read_user_baidu_mc_data(baidumc_path)
    print(ConstantParameters.user_baidu_data_transed)


def match_user_regulator():
    userlistdata = ConstantParameters.user_baidu_data_transed
    reglistdata = ConstantParameters.read_transed_data
    user_list_len = len(userlistdata)
    all_reg_list_len = len(reglistdata)
    # which point is closest
    for i in range(0, user_list_len):
        temp_distance = 1000000.0
        temp_point_num = 0

        # check user list , whether it fit calculate condition.

        for j in range(0, all_reg_list_len):
            regtup = (reglistdata[j][4], reglistdata[j][5])  #  x y value
            usertup = (userlistdata[i][2], userlistdata[i][3])  #  user x y value

            caldis = Batch_read_trans_baidu.calculate_distance(regtup, usertup)
            if temp_distance > caldis:
                temp_distance = caldis  # calculate distance
                temp_point_num = j  # return closet point index

            else:
                pass

        # Adding regulator name , some description and  distance between the user and closest regulator
        userlistdata[i].append(reglistdata[temp_point_num][0])  # add regulator point name
        userlistdata[i].append(reglistdata[temp_point_num][3])  # add regulator point value
        userlistdata[i].append(temp_distance)
    for one_piece in userlistdata:
        for one_char in one_piece:
            scroll_text_tab3.insert(END,one_char)
            scroll_text_tab3.insert(END, ';')

        scroll_text_tab3.insert(END, '\n')


if __name__ == "__main__":
    root = Tk()

    Baidu_Lng = StringVar()
    Baidu_Lat = StringVar()


    after_deviation_baidu = StringVar()
    after_deviation_std_xy = StringVar()



    root.title("CoordValueTrans")
    root.geometry('1000x300')
    nb = ttk.Notebook(root)

    # tab1 标准转换 单点 界面
    tab1 = ttk.Frame(nb)
    nb.add(tab1, text='Standard Trans')

    frame_a = ttk.Frame(tab1)
    # label 模型的 x   y
    L1 = Label(frame_a, text="Model Coord X:", font=('Arial', 14))
    L1.grid(row=0, sticky=W)
    L2 = Label(frame_a, text="Model Coord Y:", font=('Arial', 14)).grid(row=1, sticky=W)
    # Entry 模型的 x  Y
    e1 = Entry(frame_a, show=None, font=('Arial', 14))
    e1.grid(row=0, column=1, sticky=E)
    e2 = Entry(frame_a, show=None, font=('Arial', 14))
    e2.grid(row=1, column=1, sticky=E)
    # 输入模型WKID
    L_wkid = Label(frame_a, text="Model's WKID:", font=('Arial', 14)).grid(row=2, column=2 , sticky=W)
    e_wkid = Entry(frame_a, show=None, font=('Arial', 14))
    e_wkid.grid(row=2, column=3, sticky=W)

    # 输入 Ak 码
    L_ak = Label(frame_a, text="Ak码:", font=('Arial', 14)).grid(row=2, sticky=W)
    e_ak = Entry(frame_a, show=None, font=('Arial', 14))
    e_ak.grid(row=2, column=1, sticky=W)
    # 转换
    b1 = Button(frame_a, text='Convert', command=one_point_convert, width=7, height=2, font=("Arial", "10")).grid(row = 5, column = 0, sticky =W)
    b2_tab1 = Button(frame_a, text="批量转墨卡托" ,command= stand_batch_trans_to_baidumc,width=10, height=2, font=("Arial", "10"))
    b2_tab1.grid(row = 5, column =1, sticky =E)
    result_label_1 = Label(frame_a, text="Baidu 经度:", font=('Arial', 14)).grid(row=3, column=0, sticky=W)
    result_label_2 = Label(frame_a, text="Baidu 纬度:", font=('Arial', 14)).grid(row=4, column=0, sticky=W)

    label_1_after_compute = Label(frame_a, textvariable=Baidu_Lng, font=('Arial', 14)).grid(row=3, column=1, sticky=W)
    label_1_after_compute_lat = Label(frame_a, textvariable=Baidu_Lat, font=('Arial', 14)).grid(row=4, column=1, sticky=W)

    frame_a.pack(anchor=CENTER, expand=1)

    # 非标准 转换   tab2 界面
    tab_2 = ttk.Frame(nb)
    nb.add(tab_2, text='UnStandard Trans')
    frame_b = ttk.Frame(tab_2)
    #建立对应的坐标点 2
    L1_tab2 = Label(frame_b, text="Model Coord X,Y :", font=('Arial', 14))
    L1_tab2.grid(row=0, sticky=W)
    e1_tab2 = Entry(frame_b, show=None, font=('Arial', 14))
    e1_tab2.grid(row=0, column=1, sticky=W)
    L2_tab2 = Label(frame_b, text = "对应的标准系 X,Y:", font=('Arial', 14))
    L2_tab2.grid(row=0,column=2, sticky=W)
    e2_tab2 = Entry(frame_b, show=None, font=('Arial', 14))
    e2_tab2.grid(row=0, column=3, sticky=W)

    L3_tab2 = Label(frame_b, text="Model Coord X,Y:", font=('Arial', 14))
    L3_tab2.grid(row=2, sticky=W)
    e3_tab2 = Entry(frame_b, show=None, font=('Arial', 14))
    e3_tab2.grid(row=2, column=1, sticky=W)
    L4_tab2 = Label(frame_b, text = "对应的标准系 X,Y:", font=('Arial', 14))
    L4_tab2.grid(row=2,column=2, sticky=W)
    e4_tab2 = Entry(frame_b, show=None, font=('Arial', 14))
    e4_tab2.grid(row=2, column=3, sticky=W)

    # 第三个点
    L5_tab2 = Label(frame_b, text="Model Coord X,Y:", font=('Arial', 14))
    L5_tab2.grid(row=3, sticky=W, pady=30)
    e5_tab2 = Entry(frame_b, show=None, font=('Arial', 14))
    e5_tab2.grid(row=3, column=1, sticky=W)
    #计算结果
    L6_tab2 = Label(frame_b, text="对应的标准系 X,Y:", font=('Arial', 14))
    L6_tab2.grid(row=3, column=2, sticky=W)
    L7_tab2 = Label(frame_b, textvariable=after_deviation_std_xy, font=('Arial', 14))
    L7_tab2.grid(row=3, column=3, sticky=W)

    L8_tab2 = Label(frame_b, text="百度经纬:", font=('Arial', 14))
    L8_tab2.grid(row=4, column=2, sticky=W)
    L9_tab2 = Entry(frame_b, textvariable=after_deviation_baidu, font=('Arial', 14))
    L9_tab2.grid(row=4, column=3, sticky=W)

    L10_tab2 = Label(frame_b, text="标准系WKID:", font=('Arial', 14))
    L10_tab2.grid(row=4, column=0, sticky=W)
    e10_tab2 = Entry(frame_b, show=None, font=('Arial', 14))
    e10_tab2.grid(row=4, column=1, sticky=W)

    Uns_trans_button = Button(frame_b, text='转换', command=one_point_convert_unstd, width=7, height=2, font=("Arial", "11"))
    Uns_trans_button.grid(row=6, column=0, sticky=W)

    Uns_batch_trans = Button(frame_b, text="批量转墨卡托", command= unstand_batch_trans_to_baidumc, width=20, height=2, font=("Arial", "11"))
    Uns_batch_trans.grid(row=6, column=2, sticky=W)
    frame_b.pack()


# 第三个界面
    tab_3 = ttk.Frame(nb)
    nb.add(tab_3, text='匹配')
    frame_c = ttk.Frame(tab_3)
    user_baidu_path_tab3 = StringVar()
    l1_tab3 = Label(frame_c, text="用户-百度经纬数据:", font=('Arial', 14))
    l1_tab3.grid(row=0, column=0, sticky=W)
    model_data_path_tab3 = StringVar()
    l2_tab3 = Label(frame_c, text="模型节点数据:", font=('Arial', 14))
    l2_tab3.grid(row=1, column=0, sticky=W)
    e1_tab3 = Entry(frame_c, textvariable=user_baidu_path_tab3, width=60)
    e1_tab3.grid(row=0, column=1, sticky=W)
    e2_tab3 = Entry(frame_c, textvariable=model_data_path_tab3, width=60)
    e2_tab3.grid(row=1, column=1, sticky=W)

    b1_tab3 = Button(frame_c, text='Load', command=tab3_Load_user_baidu, width=7, font=("Arial", "14"))
    b1_tab3.grid(row=0, column=2, sticky=W)
    b2_tab3 = Button(frame_c,  text='转墨卡托', command=tab3_userbaidu_trans_baidumc, width=7,
                     font=("Arial", "14"))
    b2_tab3.grid(row=0, column=3, sticky=W)
    b3_tab3 = Button(frame_c, text='Load', command=tab3_load_trandsed_regulator, width=7,
                     font=("Arial", "14"))
    b3_tab3.grid(row=1, column=2, sticky=W)
    b4_tab3 = Button(frame_c, text='匹配', command=match_user_regulator, width=7,
                     font=("Arial", "14"))
    b4_tab3.grid(row=3, column=1, sticky=W)

    l3_tab3 = Label(frame_c, text="用户-百度墨卡托数据:", font=('Arial', 14))
    l3_tab3.grid(row=2, column=0, sticky=W)
    load_baidumc_tab3 = Button(frame_c, text='Load', command=tab3_Load_user_baidu_mc, width=7, font=("Arial", "14"))
    load_baidumc_tab3.grid(row=2, column=2, sticky=W)
    user_baidu_path_mc_tab3 = StringVar()
    baidumc_tab3 = Entry(frame_c, textvariable=user_baidu_path_mc_tab3, width=60)
    baidumc_tab3.grid(row=2, column=1, sticky=W)



    scroll_text_tab3 = ScrolledText(frame_c, width=60, height=15)

    scroll_text_tab3.grid(row=5, column=1, sticky=W + E)

    frame_c.pack()
    nb.pack(anchor=NW,expand=1, fill="both")
    root.mainloop()



