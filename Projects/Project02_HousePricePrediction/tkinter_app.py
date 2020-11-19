import tkinter as tk
import json
import model
import numpy as np

window = tk.Tk()
window.geometry('500x500')

lb_location = tk.Label(text='location',font=20)
lb_location.grid(row=0,column=0)
lb_area = tk.Label(text='area(sqft)',font=20)
lb_area.grid(row=1,column=0)
lb_bhk = tk.Label(text='bhk',font=20)
lb_bhk.grid(row=2,column=0)
lb_bath = tk.Label(text='bath',font=20)
lb_bath.grid(row=3,column=0)

with open('columns.json','r') as f:
    location_list = json.load(f)['data_columns'][4:]
variable_loc = tk.StringVar()
drmn_loc = tk.OptionMenu(window,variable_loc,location_list[0],*location_list[1:])
drmn_loc.grid(row=0,column=1)

ent_area = tk.Entry()
ent_area.grid(row=1,column=1)

bhk_list = [1,2,3,4,5,6]
variable_bhk = tk.StringVar()
drmn_bhk = tk.OptionMenu(window,variable_bhk,bhk_list[0],*bhk_list[1:])
drmn_bhk.grid(row=2,column=1)

bath_list = [1,2,3,4,5,6]
variable_bath = tk.StringVar()
drmn_bath = tk.OptionMenu(window,variable_bath,bath_list[0],*bath_list[1:])
drmn_bath.grid(row=3,column=1)


drmn_loc.config(font=('calibri',(10)),bg='white',width=12)
drmn_bhk.config(font=('calibri',(10)),bg='white',width=12)
drmn_bath.config(font=('calibri',(10)),bg='white',width=12)

def click():
    global variable_loc
    global variable_bhk
    global  variable_bath

    location = variable_loc.get()
    area = ent_area.get()
    bhk = variable_bhk.get()
    bath = variable_bath.get()
   # parameters = []
    #parameters.append([location,area,bath,bhk])
    result = model.predict_price(location,area,bhk,bath)

    lb_result = tk.Label(text='The estimated price is:',font=20)
    lb_result.grid(row=5,column=0)

    lb_result2 = tk.StringVar()
    lb_result2.set('')
    lb_result2 = result
    lb_result3 = tk.Label(text=lb_result2,font=20)
    lb_result3.grid(row=5, column=1)

btn_estimate = tk.Button(text='estimate',command=click)
btn_estimate.grid(row=4,columnspan=2)


window.mainloop()