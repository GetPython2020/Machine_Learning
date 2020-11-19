import tkinter as tk
import json
import model

window = tk.Tk()
window.geometry('500x600')
canvas = tk.Canvas(width=500,height=500,bg='light blue')
canvas.pack()

lb_title = tk.Label(text='House Price Predict',font=25,fg='red')
canvas.create_window(250,30,window=lb_title)

lb_location = tk.Label(text='Location',font=20)
canvas.create_window(100,100,window=lb_location)
lb_area = tk.Label(text='Area(sqft)',font=20)
canvas.create_window(100,150,window=lb_area)
lb_bhk = tk.Label(text='Bhk',font=20)
canvas.create_window(100,200,window=lb_bhk)
lb_bath = tk.Label(text='Bath',font=20)
canvas.create_window(100,250,window=lb_bath)

with open('columns.json','r') as f:
    location_list = json.load(f)['data_columns'][4:]
variable_loc = tk.StringVar()
drmn_loc = tk.OptionMenu(window,variable_loc,location_list[0],*location_list[1:])
canvas.create_window(300,100,window=drmn_loc)

ent_area = tk.Entry()
canvas.create_window(300,150,window=ent_area)

bhk_list = [1,2,3,4,5,6]
variable_bhk = tk.StringVar()
drmn_bhk = tk.OptionMenu(window,variable_bhk,bhk_list[0],*bhk_list[1:])
canvas.create_window(300,200,window=drmn_bhk)

bath_list = [1,2,3,4,5,6]
variable_bath = tk.StringVar()
drmn_bath = tk.OptionMenu(window,variable_bath,bath_list[0],*bath_list[1:])
canvas.create_window(300,250,window=drmn_bath)


drmn_loc.config(font=('calibri',(15)),bg='white',width=20)
drmn_bhk.config(font=('calibri',(15)),bg='white',width=20)
drmn_bath.config(font=('calibri',(15)),bg='white',width=20)
ent_area.config(font=('calibri',(15)),bg='white',width=24)

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
    canvas.create_window(100,400,window=lb_result)

    lb_result2 = tk.StringVar()
    lb_result2.set('')
    lb_result2 = result
    lb_result3 = tk.Label(text=lb_result2,font=20)
    canvas.create_window(300,400,window=lb_result3)

btn_estimate = tk.Button(text='Estimate',command=click,font=15,fg='orange')
canvas.create_window(250,300,window=btn_estimate)


window.mainloop()
