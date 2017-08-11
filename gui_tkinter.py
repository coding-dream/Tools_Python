#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import messagebox
import pickle # 提供简单的持久化功能可以将对象以文件的形式存放在磁盘上

class Sample(object):
    def __init__(self):
        print("__parent init__")
    def start(self):
        pass

class Sample1(Sample):
    def __init__(self):
        super().__init__()
        self.message = None
        self.isHit = False
    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        self.message = tk.StringVar()
        # self.message.set("this is a label")
        lable = tk.Label(window, textvariable=self.message, bg='green', font=('Arial', 12), width=15, height=2)
        lable.pack()  #

        button = tk.Button(window,text="hit me",width=15,height=2,command=self.hitMe)
        button.pack() #
        window.mainloop()

    def hitMe(self):
        if self.isHit == False:
            self.message.set("you hit me ")
            self.isHit = True
        else:
            self.message.set("")
            self.isHit = False

class Sample2(Sample):
    def __init__(self):
        super().__init__()
        self.editText = None
        self.button1 = None
        self.button2 = None
        self.textArea = None
    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        self.editText = tk.Entry(window) # show通常，用户键入的字符在EditText中显示，如果制作一个密码设置show ='*'。
        self.editText.pack()

        self.button1 = tk.Button(window,text="插入到当前光标处",width=15,height=2,command=self.insertPoint)
        self.button1.pack()
        self.button2 = tk.Button(window,text="插入到尾部",width=15,height=2,command=self.insertEnd)
        self.button2.pack()

        self.textArea = tk.Text(window,height=2)
        self.textArea.pack()

        window.mainloop()
    def insertPoint(self):
        msg = self.editText.get()
        self.textArea.insert('insert',msg)

    def insertEnd(self):
        msg = self.editText.get()
        self.textArea.insert('end',msg)

class Sample3(Sample):
    def __init__(self):
        super().__init__()
    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        tuple = tk.StringVar() # 元组
        tuple.set((11,22,33,44))
        list_box = tk.Listbox(window,listvariable=tuple)
        list_items = [1,2,3,4]
        for item in list_items:
            list_box.insert('end',item)

        list_box.insert(0,'first')
        list_box.insert(1,'second')
        list_box.delete(1)

        list_box.pack()

        # curValue = list_box.get(list_box.curselection())
        tk.mainloop()

class Sample4(Sample):
    def __init__(self):
        super().__init__()
        self.message = None
        self.label = None
    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        self.message = tk.StringVar()
        self.label = tk.Label(window, bg='yellow', width=20, text='empty')
        self.label.pack()

        r1 = tk.Radiobutton(window, text='Option A',
                            variable=self.message, value='A',# variable作用是-> 当选中radiobutton时，self.message 会被赋值 = 'A'
                            command=self.print_selection)
        r1.pack()
        r2 = tk.Radiobutton(window, text='Option B',
                            variable=self.message, value='B',
                            command=self.print_selection)
        r2.pack()
        r3 = tk.Radiobutton(window, text='Option C',
                            variable=self.message, value='C',
                            command=self.print_selection)
        r3.pack()

        tk.mainloop()

    def print_selection(self):
        self.label.config(text='you have selected ' + self.message.get()) # label.config() 相当于java 的setter和getter方法，可以修改构造函数初始化过的属性tk.Label(window, bg='yellow', width=20, text='empty')

class Sample5(Sample):
    def __init__(self):
        super().__init__()
    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')
        """ 类似SeekBar: showvalue(1或0即true或者false是否显示拖动的数值) tickinterval刻度间隔  resolution 显示数值的小数位数(0.01两位小数,0.1一位小数,1整数)"""
        scale = tk.Scale(window, label='try me', from_=1, to=10, orient=tk.VERTICAL,
                     length=300, showvalue=1, tickinterval=1, resolution=1, command=self.print_selection)
        scale.pack()
        tk.mainloop()
    def print_selection(self,value):
        print("the value is " + value)

class Sample6(Sample):
    def __init__(self):
        super().__init__()
    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        l = tk.Label(window, bg='yellow', width=20, text='empty')
        l.pack()

        var1 = tk.IntVar()
        var2 = tk.IntVar()
        c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                            command=lambda : self.print_selection(l=l, var1=var1, var2=var2))
        c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                            command=lambda : self.print_selection(l=l, var1=var1, var2=var2))
        c1.pack()
        c2.pack()

        tk.mainloop()
    def print_selection(self,l,var1,var2):
        if var1.get() == 1 and var2.get() == 0:
        # if (var1.get() == 1) & (var2.get() == 0):
            l.config(text='I love only Python ')
        elif (var1.get() == 0) & (var2.get() == 1):
            l.config(text='I love only C++')
        elif (var1.get() == 0) & (var2.get() == 0):
            l.config(text='I do not love either')
        else:
            l.config(text='I love both')

class Sample7(Sample):
    def __init__(self):
        super().__init__()

    def moveit(self,canvas,rect,_from,_to):
        canvas.move(rect, _from, _to)

    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        canvas = tk.Canvas(window, bg='blue', height=100, width=200)
        image_file = tk.PhotoImage(file='test.png')
        image = canvas.create_image(10, 10, anchor='nw', image=image_file)
        x0, y0, x1, y1 = 50, 50, 80, 80
        line = canvas.create_line(x0, y0, x1, y1)
        oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
        arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)
        rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)
        canvas.pack()

        b = tk.Button(window, text='move', command=lambda : self.moveit(canvas=canvas,rect=rect, _from=0, _to=2)).pack()

        window.mainloop()

class Sample8(Sample):
    def __init__(self):
        super().__init__()

    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        l = tk.Label(window, text='the info', bg='yellow')
        l.pack()

        toolbar = tk.Menu(window)

        filemenu = tk.Menu(toolbar, tearoff=0)
        editmenu = tk.Menu(toolbar, tearoff=0)

        toolbar.add_cascade(label='File', menu=filemenu)
        toolbar.add_cascade(label='Edit', menu=editmenu)

        filemenu.add_command(label='New', command=lambda : self.do_job(l,"new"))
        filemenu.add_command(label='Open', command=lambda : self.do_job(l,"open"))
        filemenu.add_command(label='Save', command=lambda : self.do_job(l,"save"))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=window.quit)

        editmenu.add_command(label='Cut', command=lambda : self.do_job(l,"cut"))
        editmenu.add_command(label='Copy', command=lambda : self.do_job(l,"copy"))
        editmenu.add_command(label='Paste', command=lambda : self.do_job(l,"paste"))

        submenu = tk.Menu(filemenu)
        filemenu.add_cascade(label='Import', menu=submenu, underline=0)
        submenu.add_command(label="Submenu1", command=lambda : self.do_job(l,"submenu"))

        window.config(menu=toolbar)

        window.mainloop()
    def do_job(self,label,msg):
        label.config(text='do ' + msg)

class Sample9(Sample):
    def __init__(self):
        super().__init__()

    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        menubar = tk.Menu(window)  # 菜单条

        """将tearoff设置为1以后，就是表明这个菜单是可以独立出来的 多出来一条线(意义不大)"""
        fileMenu = tk.Menu(menubar, tearoff=0)  # 文件
        aboutMenu = tk.Menu(menubar, tearoff=0)  # 关于

        menubar.add_cascade(label='文件', menu=fileMenu)
        menubar.add_cascade(label='关于', menu=aboutMenu)

        fileMenu.add_command(label='打开', command=self.open)
        fileMenu.add_command(label='保存')
        fileMenu.add_separator()  # 添加分割线
        fileMenu.add_command(label='退出', command=window.quit)

        aboutMenu.add_command(label='关于作者', command=lambda : self.about(window))

        window.config(menu=menubar)
        window.mainloop() # 进入消息循环

    def open(self):
        print('open a file')

    def about(self,window):
        label = tk.Label(window, text='Limitless\n QQ:爱技术，爱分享！', fg='black', bg='white')
        label.pack(expand=tk.YES, fill=tk.BOTH)

class Sample10(Sample):
    def __init__(self):
        super().__init__()

    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        frame = tk.Frame(window)
        frame.pack()
        frame_left = tk.Frame(frame)
        frame_right = tk.Frame(frame)
        frame_left.pack(side='left')
        frame_right.pack(side='right')

        tk.Label(frame_left,text='on the frame left 1').pack()
        tk.Label(frame_left,text='on the frame left 2').pack()
        tk.Label(frame_right,text='on the frame right 1').pack()
        window.mainloop()


class Sample11(Sample):
    def __init__(self):
        super().__init__()

    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        tk.Button(window,text='hit me',command=self.hit_me).pack()

        tk.mainloop()

    def hit_me(self):
        # tk.messagebox.showinfo(title='Hi', message='hahahaha')
        # tk.messagebox.showwarning(title='Hi', message='nononono')
        # tk.messagebox.showerror(title='Hi', message='No!! never')
        print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))   # return 'yes' , 'no' 然后还可以打印出来或者处理
        # print(tk.messagebox.askyesno(title='Hi', message='hahahaha'))   # return True, False
        # print(tk.messagebox.asktrycancel(title='Hi', message='hahahaha'))  # return True, False
        # print(tk.messagebox.askokcancel(title='Hi', message='hahahaha'))  # return True, False
        # print(tk.messagebox.askyesnocancel(title="Hi", message="haha"))  # return, True, False, None

class Sample12(Sample):
    """ 位置 """
    def __init__(self):
        super().__init__()

    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        # canvas = tk.Canvas(window, height=150, width=500)
        # canvas.grid(row=1, column=1)
        # image_file = tk.PhotoImage(file='test.png')
        # image = canvas.create_image(0, 0, anchor='nw', image=image_file)

        # tk.Label(window, text='1').pack(side='top')
        # tk.Label(window, text='2').pack(side='bottom')
        # tk.Label(window, text='3').pack(side='left')
        # tk.Label(window, text='4').pack(side='right')

        for i in range(4):
            for j in range(3):
                tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

        tk.Label(window, text="I am a label").place(x=20, y=10, anchor='nw')

        window.mainloop()

class Sample13(Sample):
    """ 登录注册 """
    def __init__(self):
        super().__init__()

    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        canvas = tk.Canvas(window, height=200, width=500)
        image_file = tk.PhotoImage(file='welcome.gif')
        image = canvas.create_image(0, 0, anchor='nw', image=image_file)
        canvas.pack(side='top')

        # user information
        tk.Label(window, text='User name: ').place(x=50, y=150)
        tk.Label(window, text='Password: ').place(x=50, y=190)

        var_user_name = tk.StringVar()
        var_user_name.set('example@python.com')
        entry_usr_name = tk.Entry(window, textvariable=var_user_name)
        entry_usr_name.place(x=160, y=150)
        var_user_pwd = tk.StringVar()
        entry_usr_pwd = tk.Entry(window, textvariable=var_user_pwd, show='*')
        entry_usr_pwd.place(x=160, y=190)

        # login and sign up button
        btn_login = tk.Button(window, text='Login', command=lambda : self.usr_login(window,var_user_name,var_user_pwd))
        btn_login.place(x=170, y=230)
        btn_sign_up = tk.Button(window, text='Sign up', command=lambda : self.usr_sign_up(window))
        btn_sign_up.place(x=270, y=230)

        window.mainloop()

    def usr_login(self,window,var_user_name,var_user_pwd):
        username = var_user_name.get()
        password = var_user_pwd.get()

        try:
            with open('users_info.pickle','rb') as stream:
                users_info = pickle.load(stream)
        except FileNotFoundError:
            with open('users_info.pickle','wb') as stream:
                users_info = {'admin':'admin'}
                pickle.dump(users_info,stream)

        if username in users_info.keys():
            if password == users_info[username]:
                tk.messagebox.showinfo(title='Welcome',message='How are you ? ' + username)
            else:
                tk.messagebox.showerror(message="Error,your password is wrong, try again!!")
        else:
            is_sign_up = tk.messagebox.askyesno('Welcom','You have not signed up yet,Sign up now ?')
            if is_sign_up:
                self.usr_sign_up(window)

    def usr_sign_up(self,window):
        def submit():
            new_password = new_pwd.get()
            new_password_config = new_pwd_confirm.get()
            new_username = new_name.get()

            with open('users_info.pickle', 'rb') as stream:
                exist_usr_info = pickle.load(stream)
            if new_password != new_password_config:
                tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
            elif new_username in exist_usr_info:
                tk.messagebox.showerror('Error', 'The user has already signed up!')
            else:
                exist_usr_info[new_username] = new_password
                with open('users_info.pickle', 'wb') as stream:
                    pickle.dump(exist_usr_info, stream)
                tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
                window_sign_up.destroy()

        window_sign_up = tk.Toplevel(window)
        window_sign_up.geometry('350x200')
        window_sign_up.title('Sign up window')

        new_name = tk.StringVar()
        new_name.set('example@python.com')
        tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)
        entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
        entry_new_name.place(x=150, y=10)

        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
        entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
        entry_usr_pwd.place(x=150, y=50)

        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
        entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_usr_pwd_confirm.place(x=150, y=90)

        btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=submit)
        btn_comfirm_sign_up.place(x=150, y=130)

class Sample14(Sample):
    """
        text    显示文本内容
        command 指定Button的事件处理函数
        compound 指定文本与图像的位置关系
        bitmap 指定位图
        focus_set 设置当前组件得到的焦点
        master 代表了父窗口
        bg 设置背景颜色
        fg 设置前景颜色
        font 设置字体大小
        height 设置显示高度、如果未设置此项，其大小以适应内容标签
        relief 指定外观装饰边界附近的标签,默认是平的,可以设置的参数; flat、groove、raised、ridge、solid、sunken 
        width 设置显示宽度，如果未设置此项，其大小以适应内容标签
        wraplength 将此选项设置为所需的数量限制每行的字符,数默认为0
        state 设置组件状态;正常(normal),激活(active),禁用(disabled)
        anchor 设置Button文本在控件上的显示位置 ,可用值:n(north),s(south),w(west),e(east),和ne,nw,se,sw
        bd 设置Button的边框大小;bd(bordwidth)缺省为1或2个像素
        textvariable 设置Button与textvariable属性
    """
    def __init__(self):
        super().__init__()

    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x800')

        RELIEF = ["flat", "raised", "sunken", "solid", "ridge", "groove"]
        for i in range(len(RELIEF)):
            tk.Button(window, text='change foreground', fg='red',bg='gray',relief=RELIEF[i]).pack() # fg 字体颜色 bg 背景颜色 relief(flat, groove, raised, ridge, solid, or sunken)
            tk.Label(text='',padx=10,pady=10).pack() # 使用Label 作 margin

        tk.Button(window, text="外观装饰边界附近的标签", width=19, relief=tk.GROOVE, bg="red").pack()

        tk.Button(window, text="设置按钮状态", width=21, state=tk.DISABLED).pack()

        # bitmap 系统值 warning,error,gray75,gray25,gray12,hourglass,questhead,info,question,
        tk.Button(window, text="(compound属性)设置(bitmap属性)放到按钮左边位置", compound="left", bitmap="info").pack()

        tk.Button(window, text="设置高度宽度以及文字显示位置", anchor='w', width=30, height=2).pack() # 设置Button文本在控件上的显示位置可用值:n(north),s(south),w(west),e(east),和ne,nw,se,sw

        tk.mainloop()


class Sample15(Sample):
    """
    Grid布局 row第几行 column第几列 下标从0开始 
    注意：不要试图在一个主窗口中混合使用pack和grid。
    你不用事先指定每个网格的大小，布局管理器会自动根据里面的控件进行调节
    注意：1.在使用grid方法时，如果不指定column参数，则默认从0开始。
          2.没有被使用的行和列号将被忽略，在上面的例子中如果使用10行和20行，则运行效果是一样的。
          3.你同样可以指定控件跨越一个或者多个网格。columnspan选项可以指定控件跨越多列显示，而rowspan选项同样可以指定控件跨越多行显示。
          4.padx=5, pady=5 padding值
          5.sticky:设置对齐方式，如果未设置对齐方式，默认为将控件放置在窗体中间
                    如果未设置对齐方式，默认为将控件放置在窗体中间。对齐方式主要有如下几种：
                1） 通过使用sticky=NE(右上角)，SE（右下角），SW（左下角），NW（左上角）来设置控件位置
                2） 通过使用sticky=N（上中）,E（右中），S（底中）,W（左中）来设置控件放置中间位置
                3） sticky=N+S，向垂直方向拉升而保持水平中间对齐
                4） sticky=E+W，向水平方向拉升而保持垂直中间对齐
                5)   sticky=N+E+S+W，以水平方向和垂直方向拉升的方式填充单元格
    """
    def __init__(self):
        super().__init__()

    def start(self):
        window = tk.Tk()
        window.title("the window")
        window.geometry('500x500')

        tk.Label(window, text="First").grid(row=0)
        tk.Label(window, text="Second").grid(row=1)

        tk.Entry(window).grid(row=0,column=1)
        tk.Entry(window).grid(row=1,column=1)

        tk.Button(window,text='button').grid(row=2,column=1)

        var = tk.IntVar()
        tk.Checkbutton(window, text='Preserve aspect', variable=var).grid(columnspan=2, sticky=tk.W)

        photo = tk.PhotoImage(file='test.png')
        label = tk.Label(image=photo)
        label.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S, padx=5, pady=5) # pady padding

        button1 = tk.Button(window, text='Zoom in')
        button1.grid(row=2, column=2)

        button2 = tk.Button(window, text='Zoom out')
        button2.grid(row=2, column=3)

        tk.mainloop()

if __name__ == "__main__":
    sample = Sample7()
    sample.start()