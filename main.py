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

def App():
    equation_entry = customtkinter.CTkEntry(master=window,width=440,height=50,justify="right")
    equation_entry.place(x=5,y=5)

    # define the function for calculation
    def Calculate(eqn):
        pass
    
     
    main_calc_entry = customtkinter.CTkEntry(master=window,font=("Helvetica",40),text_color="gray20",width=440,justify="right",height=80,border_color="white",border_width=1,fg_color="gray")
    main_calc_entry.place(x=5,y=55)







App()

window.mainloop()