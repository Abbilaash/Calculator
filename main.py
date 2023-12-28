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
dark_theme = {"text_color":"gray20","window_color":"gray",'main_calc_entry_color':'gray','toppanel_button_color':"gray25","toppanel_button_hovercolor":"gray20"}
light_theme = {"text_color":"black","window_color":"white",'main_calc_entry_color':'white','toppanel_button_color':'green'}

def App(THEME):
    theme = dark_theme
    if THEME == 'dark':
        theme=dark_theme
    else:
        theme = light_theme
    equation_entry = customtkinter.CTkEntry(master=window,width=440,height=50,justify="right")
    equation_entry.place(x=5,y=5)

    # define the function for calculation
    def Calculate(eqn):
        pass
    

    main_calc_entry = customtkinter.CTkEntry(master=window,font=("Helvetica",40),text_color=theme['text_color'],width=440,justify="right",height=80,border_color="white",border_width=1,fg_color=theme['main_calc_entry_color'])
    main_calc_entry.place(x=5,y=55)

    # mentioning and defing the buttons
    clear_button_f = lambda:main_calc_entry.delete(0,END)
    customtkinter.CTkButton(master=window,width=60,height=60,corner_radius=70,text='C',font=("Helvetica",35),hover_color=theme['toppanel_button_hovercolor'],fg_color=theme['toppanel_button_color'],command=clear_button_f,anchor='e').place(x=10,y=150)







App('dark')

window.mainloop()