import pickle
import tkinter as tk

with open('clf_model.pickle','rb') as f:
    clfmodel = pickle.load(f)

root = tk.Tk()
root.geometry('500x500')
canvas = tk.Canvas(width=500,height=250)
canvas.pack()

lbl_age = tk.Label(text='Age',font=20)
canvas.create_window(150,100,window=lbl_age)

ent_age = tk.Entry()
ent_age.config(font=20)
canvas.create_window(300,100,window=ent_age)


def estimate():
    age = int(ent_age.get())
    result = clfmodel.predict([[age]]).tolist()
    lbl_result = tk.Label(text=str(result),font=20,fg='red')
    canvas.create_window(250,220,window=lbl_result)

btn_est = tk.Button(text='Predict',command=estimate,bg='light green',font=20)
canvas.create_window(250,150,window=btn_est)

root.mainloop()