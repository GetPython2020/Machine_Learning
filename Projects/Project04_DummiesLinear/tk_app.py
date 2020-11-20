import tkinter as tk
import pickle

with open('dummy.pickle','rb') as f:
    model = pickle.load(f)

root = tk.Tk()
root.geometry('500x500')
canvas = tk.Canvas(width=500,height=500)
canvas.pack()

towns = ['monroe township','robinsville','west windsor']

lbl_area = tk.Label(text='Area',font=20)
canvas.create_window(100,100,window=lbl_area)
lbl_town = tk.Label(text='Town',font=20)
canvas.create_window(100,200,window=lbl_town)
ent_area = tk.Entry(width=15,font=20)
canvas.create_window(300,100,window=ent_area)
variable = tk.StringVar()
drmu_town = tk.OptionMenu(root,variable,towns[0],*towns[1:])
drmu_town.config(width=12,font=20)
canvas.create_window(300,200,window=drmu_town)

def click():
    area = int(ent_area.get())
    town = variable.get()
    town_code1 = 0
    town_code2 = 0
    if town == 'monroe township':
        town_code1 = 1
    elif town == 'robinsville':
        town_code2 = 1
    result = model.predict([[area,town_code1,town_code2]])

    lbl_result = tk.Label(text='The estimated price is:',font=20)
    canvas.create_window(250,400,window=lbl_result)
    lbl_result2 = tk.Label(text=result,font=20,fg='orange')
    canvas.create_window(250,450,window=lbl_result2)

btn_estimate = tk.Button(text='Estimate',font=20,command=click)
canvas.create_window(250,300,window=btn_estimate)

root.mainloop()