# importing all modules
import customtkinter 
from tkinter import *
import func


# Starting the tk windows
window = customtkinter.CTk()
window.geometry("450x600")
window.title("Calculator")
window.resizable(width=0,height=0)
window.configure(fg_color='gray')

# defining the themes
dark_theme = {"text_color":"gray20","window_color":"gray",'main_calc_entry_color':'gray','toppanel_button_color':"gray15","toppanel_button_hovercolor":"gray18",
              "numbers_color":"gray30","numbers_color_hover":"gray33"}
light_theme = {"text_color":"black","window_color":"white",'main_calc_entry_color':'white','toppanel_button_color':'green'}

def App(THEME):
    theme = dark_theme
    if THEME == 'dark':
        theme=dark_theme
    else:
        theme = light_theme
    equation_entry = customtkinter.CTkEntry(master=window,width=440,height=50,justify="right",state="disabled",text_color=theme['text_color'],fg_color=theme['main_calc_entry_color'],font=("Helvetica",25))
    equation_entry.place(x=5,y=5)

    main_calc_entry = customtkinter.CTkEntry(master=window,font=("Helvetica",40),text_color=theme['text_color'],width=440,justify="right",height=80,border_color="white",border_width=1,fg_color=theme['main_calc_entry_color'])
    main_calc_entry.place(x=5,y=55)

    # define the function for calculation
    def Calculate():
        equation_entry.delete(0,END)
        equation = main_calc_entry.get()
        answer = eval(equation)
        main_calc_entry.delete(0,END)
        main_calc_entry.insert("end",answer)
        equation_entry.configure(state="normal")
        equation_entry.insert("end",equation)
        equation_entry.configure(state="disabled")
    


    # mentioning and defing the buttons
    def clear_button_f():
        main_calc_entry.delete(0,END)
        equation_entry.configure(state="normal")
        equation_entry.delete(0,END)
        equation_entry.configure(state="disabled")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='C',font=("DejaVu Sans Mono",35),hover_color=theme['toppanel_button_hovercolor'],fg_color=theme['toppanel_button_color'],command=clear_button_f,anchor='center').place(x=10,y=150)

    # defining the number buttons
    num7_button_f = lambda:main_calc_entry.insert("end","7")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='7',font=("DejaVu Sans Mono",35),hover_color=theme['numbers_color_hover'],fg_color=theme['numbers_color'],command=num7_button_f,anchor='center').place(x=10,y=230)
    num8_button_f = lambda:main_calc_entry.insert("end","8")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='8',font=("DejaVu Sans Mono",35),hover_color=theme['numbers_color_hover'],fg_color=theme['numbers_color'],command=num8_button_f,anchor='center').place(x=110,y=230)
    num9_button_f = lambda:main_calc_entry.insert("end","9")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='9',font=("DejaVu Sans Mono",35),hover_color=theme['numbers_color_hover'],fg_color=theme['numbers_color'],command=num9_button_f,anchor='center').place(x=210,y=230)
    num4_button_f = lambda:main_calc_entry.insert("end","4")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='4',font=("DejaVu Sans Mono",35),hover_color=theme['numbers_color_hover'],fg_color=theme['numbers_color'],command=num4_button_f,anchor='center').place(x=10,y=300)
    num5_button_f = lambda:main_calc_entry.insert("end","5")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='5',font=("DejaVu Sans Mono",35),hover_color=theme['numbers_color_hover'],fg_color=theme['numbers_color'],command=num5_button_f,anchor='center').place(x=110,y=300)
    num6_button_f = lambda:main_calc_entry.insert("end","6")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='6',font=("DejaVu Sans Mono",35),hover_color=theme['numbers_color_hover'],fg_color=theme['numbers_color'],command=num6_button_f,anchor='center').place(x=210,y=300)
    num1_button_f = lambda:main_calc_entry.insert("end","1")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='1',font=("DejaVu Sans Mono",35),hover_color=theme['numbers_color_hover'],fg_color=theme['numbers_color'],command=num1_button_f,anchor='center').place(x=10,y=370)
    num2_button_f = lambda:main_calc_entry.insert("end","2")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='2',font=("DejaVu Sans Mono",35),hover_color=theme['numbers_color_hover'],fg_color=theme['numbers_color'],command=num2_button_f,anchor='center').place(x=110,y=370)
    num3_button_f = lambda:main_calc_entry.insert("end","3")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='3',font=("DejaVu Sans Mono",35),hover_color=theme['numbers_color_hover'],fg_color=theme['numbers_color'],command=num3_button_f,anchor='center').place(x=210,y=370)
    num0_button_f = lambda:main_calc_entry.insert("end","0")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='0',font=("DejaVu Sans Mono",35),hover_color=theme['numbers_color_hover'],fg_color=theme['numbers_color'],command=num0_button_f,anchor='center').place(x=110,y=440)

    # defining all the symbols
    mult_button_f = lambda:main_calc_entry.insert("end","*")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='x',font=("DejaVu Sans Mono",35),hover_color=theme['toppanel_button_hovercolor'],fg_color=theme['toppanel_button_color'],command=mult_button_f,anchor='center').place(x=320,y=230)
    subt_button_f = lambda:main_calc_entry.insert("end","-")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='-',font=("DejaVu Sans Mono",35),hover_color=theme['toppanel_button_hovercolor'],fg_color=theme['toppanel_button_color'],command=subt_button_f,anchor='center').place(x=320,y=300)
    add_button_f = lambda:main_calc_entry.insert("end","+")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='+',font=("DejaVu Sans Mono",35),hover_color=theme['toppanel_button_hovercolor'],fg_color=theme['toppanel_button_color'],command=add_button_f,anchor='center').place(x=320,y=370)
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='=',font=("DejaVu Sans Mono",35),hover_color="RoyalBlue3",fg_color="RoyalBlue1",text_color="black",command=Calculate,anchor='center').place(x=320,y=440)
    point_button_f = lambda:main_calc_entry.insert("end",".")
    customtkinter.CTkButton(master=window,width=50,height=60,corner_radius=70,text='.',font=("DejaVu Sans Mono",35),hover_color=theme['numbers_color_hover'],fg_color=theme['numbers_color'],command=point_button_f,anchor='center').place(x=210,y=440)







App('dark')

window.mainloop()