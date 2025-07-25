
import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# Ініціалізація
ctk.set_appearance_mode("Dark")  # "Dark", "Light", "System"
ctk.set_default_color_theme("blue")  # Можна: "green", "dark-blue", "blue"

# Вікно
root = ctk.CTk()
root.geometry("800x500")
root.title("CustomTkinter Example")
root.attributes("-topmost", True)

def result():
    mnr = min_range.get()
    mxr = max_range.get()
    if type(mnr) == str or type(mxr) == str:
        mxr = int(mxr)
        mnr = int(mnr)
        print(mnr,mxr)
#Границі Проектування
def configurate_menu_range():
    global min_range
    global max_range
    # Рамка 
    Frame_range = ctk.CTkFrame(master=root,
        width=200,
        height=220,
        corner_radius=15,
        border_color="black",
        fg_color="#6969CF")
    Frame_range.place(x=10,y=10)

    # текст
    Text_title_range = ctk.CTkLabel(master=Frame_range,text="Границі проектування",font=("Arial",16,"bold"),text_color="#000000")
    Text_title_range.place(x=20,y=10)
    Text_min_range = ctk.CTkLabel(master=Frame_range, text="Введіть ліву границю", text_color="#000000")
    Text_min_range.place(x=20,y=40)
    Text_max_range = ctk.CTkLabel(master=Frame_range, text="Введіть праву границю", text_color="#000000")
    Text_max_range.place(x=20,y=90)
    # поле введення
    min_range = ctk.CTkEntry(master=Frame_range, fg_color="white",text_color="#000000")
    min_range.place(x=20,y=60)
    max_range = ctk.CTkEntry(master=Frame_range, fg_color="white",text_color="#000000")
    max_range.place(x=20,y=110)
    # кнопка
    range_limit = ctk.CTkButton(master=Frame_range,
        fg_color="#807D7D",
        text_color="#FF0000",
        font=("Arial",12,"bold"),
        text="вивести результат",
        corner_radius=5,
        border_width=2,
        border_color="black",
        width=140,
        height=25,
        command=result) 
    range_limit.place(x=20,y=150)
configurate_menu_range()
#Тип Функції
def configurate_menu_type():
    global Func_type
    global selected_trig
    # Рамка
    Frame_type = ctk.CTkFrame(master=root,
    width=250,
    corner_radius=12,
    height=350,
    fg_color="#8C8C8C")
    Frame_type.place(x=220,y=10)
    # Текст
    Text_title_func = ctk.CTkLabel(master=Frame_type,text="Оберіть тип функції",font=("Arial",16,"bold"),text_color="black")
    Text_title_func.place(x=10,y=10)
    # Радіо кнопки
    # #Тригонометричні функції які вспливатимуть
    selected_trig = tk.StringVar()
    sin_f = ctk.CTkRadioButton(master=Frame_type, text="sin(x)", variable=selected_trig, value="sin",command=lambda:(total_function()))
    cos_f = ctk.CTkRadioButton(master=Frame_type, text="cos(x)", variable=selected_trig, value="cos",command=lambda:(total_function()))
    tan_f = ctk.CTkRadioButton(master=Frame_type, text="tan(x)", variable=selected_trig, value="tan",command=lambda:(total_function()))
    cot_f = ctk.CTkRadioButton(master=Frame_type, text="con(x)", variable=selected_trig, value="con",command=lambda:(total_function()))
    trign_fun = [sin_f,cos_f,tan_f,cot_f]

    # #Логіка вспилу тригонометричних функцій
    def detc():
        if Func_type.get() == "Trig":
            for i in range(len(trign_fun)):
                trign_fun[i].place(x=10,y=190 +i*30)
                root.update()
        else:
            for i in range(len(trign_fun)):
                trign_fun[i].place_forget()
                root.update()
    # #Основні кнопки
    Func_type = tk.StringVar()
    Line_f = ctk.CTkRadioButton(master=Frame_type, text="Лінійна", variable=Func_type, value="Line",command=lambda:(detc(),total_function()))
    Koef_f = ctk.CTkRadioButton(master=Frame_type, text="Показникова", variable=Func_type, value="Koef",command=lambda:(detc(),total_function()))
    Log_f = ctk.CTkRadioButton(master=Frame_type, text="Логарифмічна", variable=Func_type, value="Log",command=lambda:(detc(),total_function()))
    Trig_f = ctk.CTkRadioButton(master=Frame_type, text="Тригонометрична", variable=Func_type, value="Trig",command=lambda:(detc(),total_function()))
    Line_f.place(x=10,y=50) 
    Koef_f.place(x=10,y=80)
    Log_f.place(x=10,y=110) 
    Trig_f.place(x=10,y=140)
configurate_menu_type()
#Коефіцієнти
def configurate_menu_coefficent():
    global total_function


    # Рамка
    Frame_coefficent = ctk.CTkFrame(master=root,
    width=250,
    corner_radius=12,
    height=350,
    fg_color="#90E5FF")
    Frame_coefficent.place(x=490,y=10)
    # Текст
    Text_title_ceeff = ctk.CTkLabel(master=Frame_coefficent,text="Оберіть коефіцієнти",font=("Arial",16,"bold"),text_color="#000000")
    Text_title_ceeff.place(x=20,y=10)
    # Коефіцієнти/прапорці
    def Checkbox():
        if koef_a.get() == True:
            plan_a.place(x=65,y=100)
            flag_a.configure(text="a")
        else:
            plan_a.place_forget()
            flag_a.configure(text="коеф. а")
        if koef_b.get() == True:
            flag_b.configure(text="b")
            plan_b.place(x=65,y=150)
        else:
            plan_b.place_forget()
            flag_b.configure(text="коеф. b")
        if koef_k.get() == True:
            flag_k.configure(text="k")
            plan_k.place(x=65,y=200)
        else:
            plan_k.place_forget()
            flag_k.configure(text="коеф. k")
    koef_a = tk.BooleanVar()
    koef_b = tk.BooleanVar()
    koef_k = tk.BooleanVar()
    flag_a = ctk.CTkCheckBox(master=Frame_coefficent,text="коеф. a", variable=koef_a,command=Checkbox,text_color="#000000",font=("Arial",14,"bold")) 
    flag_b = ctk.CTkCheckBox(master=Frame_coefficent,text="коеф. b", variable=koef_b,command=Checkbox,text_color="#000000",font=("Arial",14,"bold")) 
    flag_k = ctk.CTkCheckBox(master=Frame_coefficent,text="коеф. k", variable=koef_k,command=Checkbox,text_color="#000000",font=("Arial",14,"bold")) 
    flag_a.place(x=20,y=100)
    flag_b.place(x=20,y=150)
    flag_k.place(x=20,y=200)
    # # Поле для вводу коефіцієнтів
    plan_a = ctk.CTkEntry(master=Frame_coefficent,text_color="#000000",fg_color="white",border_width=1,border_color="#000000",corner_radius=3,height=22)
    plan_b = ctk.CTkEntry(master=Frame_coefficent,text_color="#000000",fg_color="white",border_width=1,border_color="#000000",corner_radius=3,height=22)
    plan_k = ctk.CTkEntry(master=Frame_coefficent,text_color="#000000",fg_color="white",border_width=1,border_color="#000000",corner_radius=3,height=22)
    # Фінальна функція
    Text_total_fun = ctk.CTkLabel(master=Frame_coefficent,text="Загальний вид функції",font=("Arial",16,"bold"),text_color="#000000")
    Text_total_fun.place(x=30,y=280)

    def_fun = ['x','a**x','Log(a)X','sin(x)','cos(x)','tan(x)','con(x)','no data']
    current_fun = def_fun[7]

    Text_Fun = ctk.CTkLabel(master=Frame_coefficent,text=current_fun,font=("Arial",15,"bold"),text_color="#000000") 
    Text_Fun.place(x=60,y=320)   
    def total_function():
        if Func_type.get() == "Line":
            current_fun = def_fun[0]
            print(current_fun)
        elif Func_type.get() == "Koef":
            current_fun = def_fun[1]
            print(current_fun)
        elif Func_type.get() == "Log":
            current_fun = def_fun[2]
            print(current_fun)
        elif Func_type.get() == "Trig" and selected_trig.get() == "sin":
            current_fun = def_fun[3]
            print(current_fun)
        elif Func_type.get() == "Trig" and selected_trig.get() == "cos":
            current_fun = def_fun[4]
            print(current_fun)
        elif Func_type.get() == "Trig" and selected_trig.get() == "tan":
            current_fun = def_fun[5]
            print(current_fun)
        elif Func_type.get() == "Trig" and selected_trig.get() == "con":
            current_fun = def_fun[6]
            print(current_fun) 
        Text_Fun.configure(text=current_fun)
       
configurate_menu_coefficent()
# Запуск
root.mainloop()